from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, FloatType, BooleanType, DateType, TimestampType
from pyspark.sql import *
from pyspark.sql.functions import col
from pyspark.sql.functions import to_timestamp, to_date

# For any question regarding how to use the functions please check SparkData.md
# Definition of the class SparkData
class SparkData:
    # Init method to instance one object of this class
    # @param spark_session<SparkSession>: The current Spark session
    def __init__(self, spark_session):
        self.spark_session = spark_session
        self.to_spark_date_type = {
            'INTEGER': IntegerType(),
            'STRING': StringType(),
            'DOUBLE': DoubleType(),
            'FLOAT': FloatType(),
            'BOOLEAN': BooleanType()
        }

    # Reads the file and gets it as a spark dataframe
    # @param filepath<str>: The filepath
    # @param filename<str>: The fine name
    # @param format<str>: The format from the data, usually being csv
    # @param header<bool>: If we want to add the header
    # @param delimiter<str>: The delimiter for each field
    # @param json_schema<list>: A list containing the schema for each column
    # return: The DataFrame with the specified schema
    def read_data(self, filepath='', filename='', format='csv', header=False,
                  delimiter=',', schema=None, mockup=False):
        # Sets the full filepath
        full_filepath = filepath + filename
        # If we have mockup
        if mockup:
            # Creates the empty schema
            df_with_schema = self.spark_session.read \
                        .format(format) \
                        .option('header', header) \
                        .option('delimiter', delimiter) \
                        .load(full_filepath)
            # Gets the name of the columns
            column_names = [x['column_name'] for x in schema]
            # Sets the column names
            df_with_schema = df_with_schema.toDF(*column_names)

            # For all columns in the schema
            for column in schema:
                # If the column is type DATE
                if column['data_type'] == 'DATE':
                    # Sets the column type to date using the given format
                    df_with_schema = df_with_schema.withColumn(
                        column['column_name'],
                        to_date(
                            column['column_name'],
                            column['date_format']
                        )
                    )
                elif column['data_type'] == 'TIMESTAMP':
                    # Sets the column type to date using the given format
                    df_with_schema = df_with_schema.withColumn(
                        column['column_name'],
                        to_timestamp(
                            column['column_name'],
                            column['date_format']
                        )
                    )
                # Else, sets directly the format
                else:
                    # Casts the column to the format
                    df_with_schema = df_with_schema.withColumn(
                        column['column_name'],
                        col(column['column_name']).cast(self.to_spark_date_type[column['data_type']])
                    )
        else:
            # Reads the csv file with the columns
            df_with_schema = self.spark_session.read \
                .format(format) \
                .option('header', header) \
                .option('delimiter', delimiter) \
                .schema(schema) \
                .load(full_filepath)

        # Returns the dataframe with the schema
        return df_with_schema
