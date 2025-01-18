import os
import csv

class CSVHandler:
    def __init__(self, output_dir='../data/csv', file_name='output.csv'):
        self.output_dir = output_dir
        self.file_name = file_name
        self.file_path = os.path.join(self.output_dir, self.file_name)
        self.fieldnames = None
        
        os.makedirs(self.output_dir, exist_ok=True)

    def save_data(self, data):
        """Save a dictionary of data to the CSV file."""
        file_exists = os.path.exists(self.file_path)
        with open(self.file_path, mode='a', newline='', encoding='utf-8-sig') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if not file_exists:
                 writer.writeheader()
            writer.writerow(data)