
from config import DATA_DIRECTORIES
import datetime
import csv
import os

directory_name = f'test_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}'
directory_path = DATA_DIRECTORIES['raw'] + directory_name
file_name = 'test.csv'
file_path = f'{directory_path}/{file_name}'
print(f'PATH: {directory_path}/{file_name}')

def make_directory(path):
    try:
        os.mkdir(path)
        print(f"Directory '{path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{path}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# make_directory(directory_path)

def make_csv(path):
    with open(path, 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

# make_csv(file_path)

        # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
