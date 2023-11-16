from pyspark.sql import SparkSession
from pyspark.sql.functions import concat_ws, col, md5, lit, translate, when, current_date, to_date
from pyspark.sql.types import StringType
from datetime import datetime
import signal

from cardif_pyspark_library.classes.Database import DataBase
from cardif_pyspark_library.classes.SparkData import SparkData
from automotriz.models.ModelAutomotriz import ModelAutomotriz
from cardif_pyspark_library.classes.Security import Vault
from cardif_pyspark_library.classes.HadoopFile import HadoopFile
from utils.prints import *


# Main class for the ETL
class AutomotrizETL:
    # Init class
    def __init__(self, filesystem_directory='/opt/sources/masters/', hadoop_directory='/masters/to_be_processed/'):
        self.spark_session = None
        self.database_conn = None
        self.hadoop_file = None
        self.csv_filenames = None
        self.list_tables = None
        self.vault = Vault()
        self.filesystem_directory = filesystem_directory
        self.hadoop_directory = hadoop_directory

    # Handles the signal in case spark is offline
    def signal_handler(self, signal, frame):
        print(f'Deteniendo proceso')
        exit(0)

    # Sets the Spark session
    def set_spark_session(self, spark_session):
        self.spark_session = spark_session

    # Gets the spark session
    def get_spark_session(self):
        return self.spark_session

    # Create the Spark Session
    def create_spark_session(self):
        # Checks the signal is fine
        signal.signal(signal.SIGINT, self.signal_handler)
        # Creates or gets the Spark session
        self.spark_session = SparkSession.builder \
            .appName("master_socios") \
            .getOrCreate()

    # Creates the oracle session
    # @param layer<str>: The layer in DWH
    # return: The database connection
    def create_oracle_session(self, layer='lnd'):
        # Creates the database connection
        self.database_conn = DataBase(*self.vault.getUPS(layer), self.spark_session)

    def move_files_to_hadoop(self):
        # Sets the configuration for Hadoop class
        self.hadoop_file = HadoopFile(
            filesystem_directory=self.filesystem_directory,
            hadoop_directory=self.hadoop_directory
        )
        # Save all filenames
        self.csv_filenames = self.hadoop_file.get_filenames()
        # Move files to hadoop
        self.hadoop_file.move_new_files_to_hadoop()

    def insert_data_to_landing(self, mockup=False, layer=None, header=False):
        # Creates the Spark Session
        self.create_spark_session()
        # Creates the spark_data that will create the DataFrame
        spark_data = SparkData(self.spark_session)
        # Creates the models class
        models = ModelAutomotriz()
        # If we have mockup
        if mockup:
            blue_print('Mockup enabled, schemas will be gotten from ModelsAutomotriz')
        else:
            blue_print('Mockup disabled, schemas will be gotten from Oracle Database')

        counter = 0
        # For all files found
        for csv_filename in self.csv_filenames:
            """
            INSERTING DATA TO LANDING
            """
            # Creates the database session for landing
            self.create_oracle_session(layer[0])
            # Makes login to the database
            self.database_conn.login()
            # Gets the type
            master_type = csv_filename.split('_')[2]
            try:
                # Gets the table name based on the filename
                table_name = models.get_from_filename_to_tablename()[master_type]
                # Prints the file to be inserted and the target table
                blue_print('Inserting file {} to Landing on table {}'.format(csv_filename, table_name))
                # Sets the schema
                schema = None
                # If we want to use the mockup, then we use the static schema
                if mockup:
                    if table_name == 'tbl_msb_cuidados' or table_name == 'tbl_msb_cuidados_ob':
                        schema = models.get_schema_cuidados()
                    elif table_name == 'tbl_msb_valor_factura':
                        schema = models.get_schema_valor_factura()
                    elif table_name == 'tbl_msb_proteccion_financiera':
                        schema = models.get_schema_proteccion_financiera()
                    elif table_name == 'tbl_msb_vida':
                        schema = models.get_schema_vida()
                    elif table_name == 'tbl_msb_vital_plus_ob':
                        schema = models.get_schema_vital_plus_ob()
                    elif table_name == 'tbl_msb_valora':
                        schema = models.get_schema_valora()

                # Else, we get the schema from the database
                else:
                    schema = self.database_conn.get_schema(table_name)
                # Reads the file and gets the DataFrame
                df = spark_data.read_data(
                    filepath=self.hadoop_directory,
                    filename=csv_filename,
                    format='csv',
                    header=header,
                    delimiter=',',
                    schema=schema,
                    mockup=mockup
                )
                # Replaces the special characters for column policy_number to be none
                df = df.withColumn('policy_number', translate('policy_number', '="', ''))
                # Set the column names
                column_names = [x['column_name'] for x in schema]
                # Set the hash value
                df = df.withColumn('md_hash', md5(concat_ws('', *[col(col_name) for col_name in column_names])))
                # Prints the number of rows to verify
                blue_print('Number of rows to verify: {}'.format(df.count()))
                # Gets the md_hash from the table
                df_md_hash = self.database_conn.read_table('SELECT md_hash FROM {}'.format(table_name))
                # Filters for the md_hash that are not already inserted
                df = df.filter(~col('md_hash').isin(df_md_hash.rdd.map(lambda x: x[0]).collect()))
                # Prints the final number of rows to be inserted
                blue_print('Number of rows to be inserted in Landing: {}'.format(df.count()))
                # If the number of rows is more than 0
                if df.count() > 0:
                    # Sets the user load
                    df = df.withColumn('md_user_load', lit(' '))
                    # Sets the origin as the filename
                    df = df.withColumn('md_origin', lit(csv_filename))
                    # Prints the schema just to make sure we're using the right schema
                    blue_print('Schema to be used to insert the data in Landing: {}'.format(df.schema))
                    # Prints the layer
                    blue_print('The target layer is: {}'.format(layer[0]))
                    # Inserts the dataframe to the database in landing
                    self.database_conn.insert_dataframe(df, table_name)
                    # Prints success
                    green_print('File {} inserted on table {} in Landing'.format(csv_filename, table_name))
                    # Closes database connection
                    self.database_conn.logout()
                    """
                    FINISH INSERTING DATA TO LANDING
                    
                    
                    INSERTING DATA TO STAGING
                    """
                    # Creates the database session for staging
                    self.create_oracle_session(layer[1])
                    # Makes login to the database
                    self.database_conn.login()
                    # Drops the column of the user load
                    df = df.drop('md_user_load')
                    # Drops the column of the origin
                    df = df.drop('md_origin')
                    # Drops the column of the md_hash
                    df = df.drop('md_hash')
                    # Extracts the operation date from the filename
                    if table_name == 'tbl_msb_valor_factura':
                        operation_date = csv_filename.split('_')[4]
                    else:
                        operation_date = csv_filename.split('_')[3]
                    # Removes .csv termination
                    operation_date = operation_date.replace('.csv', '')
                    # Gets the date as datetime object
                    operation_date = datetime.strptime(operation_date, '%Y%m%d')
                    # Sets the operation_date value
                    df = df.withColumn('operation_date', to_date(lit(operation_date.strftime('%Y-%m-%d')), 'yyyy-MM-dd'))
                    # Sets the load date as the current date
                    df = df.withColumn('load_date', current_date())
                    # Prints number of rows to be inserted
                    blue_print('Number of rows to be inserted in Staging: {}'.format(df.count()))
                    # Prints the schema just to make sure we're using the right schema
                    blue_print('Schema to be used to insert the data in Staging: {}'.format(df.schema))
                    # Prints the layer
                    blue_print('The target layer is: {}'.format(layer[1]))
                    # Inserts the dataframe to the database in staging
                    self.database_conn.insert_dataframe(df, table_name)
                    # Prints success
                    green_print('File {} inserted on table {} in Staging'.format(csv_filename, table_name))
                    # Closes database connection
                    self.database_conn.logout()
                    """
                    FINISH INSERTING DATA TO STAGING
        
        
                    INSERTING DATA TO ODS
                    """
                    # Creates the database session for ODS
                    self.create_oracle_session(layer[2])
                    # Makes login to the database
                    self.database_conn.login()
                    # Prints number of rows to be inserted
                    blue_print('Number of rows to be inserted in ODS: {}'.format(df.count()))
                    # Prints the schema just to make sure we're using the right schema
                    blue_print('Schema to be used to insert the data in ODS: {}'.format(df.schema))
                    # Prints the layer
                    blue_print('The target layer is: {}'.format(layer[2]))
                    # Inserts the dataframe to the database in ODS
                    self.database_conn.insert_dataframe(df, table_name)
                    # Prints success
                    green_print('File {} inserted on table {} in ODS'.format(csv_filename, table_name))
                    # Closes database connection
                    self.database_conn.logout()
                    """
                    FINISH INSERTING DATA TO ODS
                    """
                else:
                    # Prints we're skipping file since we don't have new rows
                    green_print('Number of rows to insert is 0, skipping file {}'.format(csv_filename))
                    # Closes database connection
                    self.database_conn.logout()

                # Deletes the file in Hadoop
                self.hadoop_file.delete_one_hadoop_file(csv_filename)
                # Deletes file in filesystem
                self.hadoop_file.delete_one_filesystem(csv_filename)
            except:
                # Prints exception, we don't have that model yet
                red_print('File {} is not yet in the model, skipping'.format(csv_filename))
                # Deletes the file in Hadoop
                self.hadoop_file.delete_one_hadoop_file(csv_filename)

            counter = counter + 1
            if counter > 20:
                break

        # Finishes spark session
        self.spark_session.stop()
