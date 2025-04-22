from config import *
import os
import csv
import datetime

class DataSaver:
    def __init__(self, label: str):
        self.label = label
        self._create_raw_data_files()

    def save_raw_data(self, data: dict):
        return 0
        # fill the files

    def _create_raw_data_files(self):
        directory_name = f'{self.label}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}'
        directory_path = DATA_DIRECTORIES['raw'] + directory_name
        self._make_directory(directory_path)
        # print(f'Directory: {directory_path}')

        for device in CONNECTED_DEVICES:
            file_name = f'{device}.csv'
            file_path = f'{directory_path}/{file_name}'
            self._make_csv(file_path)
            # print(f'File: {file_path}')

    def _make_directory(self, path):
        try:
            os.mkdir(path)
            print(f"Directory '{path}' created successfully.")
        except FileExistsError:
            print(f"Directory '{path}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{path}'.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def _make_csv(self, path):
        with open(path, 'w', newline='') as csvfile:
            fieldnames = RAW_TRACKING_FIELDS
            self.csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            self.csv_writer.writeheader()
    
