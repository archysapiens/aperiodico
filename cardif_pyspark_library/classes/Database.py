import cx_Oracle
from pyspark.sql.functions import *
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Creates a class to connect to the Oracle Database
class DataBase:
    # Defines the class
    # @param user<str>: The username for the connection
    # @param password<str>: The password for the connection
    # @param host<str>: The host of the database
    # @param port<str>: The port, usually being 22
    # @param service<str>: The service name of the connection
    # @param spark<SparkSession>: The spark session
    def __init__(self, user, password, host, port, service, spark):
        # Sets all variables
        self.host = host
        self.port = port
        self.user = user
        self.service = service
        self.password = password
        self.driver = 'oracle.jdbc.driver.OracleDriver'
        # Creates the URL for connection
        self.url = f"jdbc:oracle:thin:@{self.host}:{self.port}/{self.service}"
        # Sets the properties of the connection
        self.properties = {"user": self.user, "password": self.password, "driver": "oracle.jdbc.driver.OracleDriver"}
        # Sets the Spark session
        self.spark = spark
        # Sets the connection to None
        self.connection = None
        # Sets the date format
        self.dateFormat = '%d-%m-%Y %H:%M:%S.%f'

    # Makes the login to the database
    def login(self):
        # Makes the DNS
        dsn_tns = cx_Oracle.makedsn(self.host, self.port, service_name=self.service)
        # Sets the connection object to the class
        self.connection = cx_Oracle.connect(user=self.user, password=self.password, dsn=dsn_tns)

    # Makes the logout to the database
    def logout(self):
        self.connection.close()

    # Gets the schema for the table
    # @param table_name<str>: The table name on the database
    # return: The database schema
    def get_schema(self, table_name):
        # With the spark session reads the table
        df = self.spark.read.jdbc(url=self.url, table=table_name, properties=self.properties)
        # Gets the schema
        return df.schema

    # Inserts the Spark dataframe to the database
    # @param df<DataFrame>: The DataFrame to be inserted
    # @param table_name<str>: The name of the table to insert the data
    def insert_dataframe(self, df, table_name):
        # Writes on the database to the target table
        df.write.jdbc(
            url=self.url,
            table=table_name,
            properties=self.properties,
            mode='append'
        )

    # Reads the data from a table
    # @param query<str>: The query to be executed to get the data
    # return: The DataFrame with the data
    def read_table(self, query):
        df = self.spark.read \
            .format('jdbc') \
            .option('url', self.url) \
            .option('driver', self.driver) \
            .option('query', query) \
            .option('user', self.user) \
            .option('password', self.password) \
            .load()

        return df
