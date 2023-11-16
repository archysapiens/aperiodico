## General information
**Creation Date:** 2023-08-18\
**Author:** f61761\
**Description:** This document is created to explain how the class SparkData.py will work for future reference.
## Functions:
### 1. read_file
**Description:** This function will generate the schema for PySpark to be used for each column.\
**Parameters:**
* **json_schema:** The dictionary schema with the following format:
```
json_schema = [
                {
                  column_name,
                  data_type,
                  nullable,
                  date_format(if needed)
                }
              ]
```
  * **column_name(String):** The name of the column to be used in PySpark.
  * **data_type(String):** The datatype of the field, the value can be:
    * INTEGER
    * STRING
    * DOUBLE
    * FLOAT
    * BOOLEAN
    * TIMESTAMP
  * **nullable(bool):** Whether the column can be null or not.
  * **date_format(String):** In the case the data_type is timestamp, specifies the format of the datetime. For any reference about the date_format possible please check [PySpark Datetime Patterns](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html)

**General example:**
```
json_schema = [
                  {
                      'column_name': 'id_user', 
                      'data_type': 'STRING', 
                      'nullable': False
                  }, 
                  {
                      'column_name: 'report_date', 
                      'data_type': 'TIMESTAMP', 
                      'nullable': True,
                      'date_format': 'yyyy-MM-dd HH:mm:ss.SSS'
                  }
              ]
```
