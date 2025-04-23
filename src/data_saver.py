from config import *
import os
import csv
import datetime

class DataSaver:
    def __init__(self, label: str = "unlabeled"):
        self.label = label
        self.raw_tracking_fields = RAW_TRACKING_FIELDS
        self.connected_devices = CONNECTED_DEVICES
        self.data_directories = DATA_DIRECTORIES
        self.csv_writers = {}
        self.file_handles = {}
        self._create_raw_data_files()

    def save_raw_data(self, raw_data: dict):
        for device, data in raw_data.items():
            writer = self.csv_writers.get(device)
            writer.writerow(data)

    def _create_raw_data_files(self):
        directory_name = f'{self.label}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}'
        self.raw_directory_path = self.data_directories['raw'] + directory_name
        self._make_directory(self.raw_directory_path)

        for device in self.connected_devices:
            file_path = f'{self.raw_directory_path}/{device}.csv'
            csv_file = open(file_path, 'w', newline='')
            self.file_handles[device] = csv_file

            writer = csv.DictWriter(csv_file, fieldnames=self.raw_tracking_fields)
            writer.writeheader()
            self.csv_writers[device] = writer

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

