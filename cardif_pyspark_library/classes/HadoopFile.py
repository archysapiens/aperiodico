import os
from utils.logger import *
from utils.prints import *


# Class for moving files from the filesystem to hadoop
class HadoopFile:
    # Init class
    def __init__(self, filesystem_directory, hadoop_directory):
        self.filesystem_directory = filesystem_directory
        self.hadoop_directory = hadoop_directory

    def get_filenames(self):
        # List all files on the source directory
        all_files = os.listdir(self.filesystem_directory)
        # Returns the list of all filenames
        file_list = [file for file in all_files if file.endswith('.csv')]
        counter = 0
        files = []
        for file in file_list:
            if ('MOMENTOS' not in file) and ('PLENITUD' not in file):
                files.append(file)
                counter = counter + 1
            if counter > 20:
                break

        return files

    # Moves the current files from the filesystem to hadoop
    def move_new_files_to_hadoop(self):
        # Gets all CSV files
        csv_files = self.get_filenames()
        counter = 0
        # Goes through all files
        for file in csv_files:
            if ('MOMENTOS' not in file) and ('PLENITUD' not in file):
                # Prints the file we're moving
                blue_print('Moving file {} to hdfs'.format(file))
                # Sets source directory
                source_file_path = self.filesystem_directory + str(file)
                # Sets destination path
                destination_file_path = self.hadoop_directory + str(file)
                # Moves the file to hdfs
                os.system('hadoop fs -appendToFile {} {}'.format(source_file_path, destination_file_path))
                # Prints success
                green_print('Successful operation. File copied to {} in Hadoop File System'.format(destination_file_path))
                # Adds one entry to the system log file
                #add_syslog_entry('Masters: File {} successfully moved to hdfs'.format(file))
                counter = counter + 1
                if counter > 20:
                    break
            else:
                blue_print('Skipping file {}'.format(file))

    def delete_one_hadoop_file(self, csv_filename):
        # Deletes all files from the hadoop filesystem
        os.system('hadoop fs -rm {}'.format(self.hadoop_directory + csv_filename))
        # Prints success
        green_print('File {} deleted from Hadoop'.format(csv_filename))

    def delete_one_filesystem(self, csv_filename):
        # Creates the full filepath for the filesystem
        filesystem_path = self.filesystem_directory + str(csv_filename)
        # Deletes the file from the file system
        os.remove(filesystem_path)
        # Prints success
        green_print('File {} deleted from FileSystem'.format(csv_filename))
