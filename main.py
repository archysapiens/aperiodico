from etl.AutomotrizETL import AutomotrizETL
import time


def main():
    # Creates the ETL object
    etl = AutomotrizETL(
        filesystem_directory='/opt/sources/masters/',
        hadoop_directory='/masters/to_be_processed/'
    )
    # Moves the files from the filesystem to hadoop
    etl.move_files_to_hadoop()
    # Inserts the data to landing
    etl.insert_data_to_landing(
        mockup=True,
        layer=['euc', 'stg', 'ods'],
        header=True
    )


if __name__ == '__main__':
    while True:
        main()
        time.sleep(1)
