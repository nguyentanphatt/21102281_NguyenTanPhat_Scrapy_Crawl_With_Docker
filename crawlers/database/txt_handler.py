import os

class TXTHandler:
    def __init__(self, output_dir='../data/txt', file_name='output.txt'):
        self.output_dir = output_dir
        self.file_name = file_name
        self.file_path = os.path.join(self.output_dir, self.file_name)
        
        os.makedirs(self.output_dir, exist_ok=True)

        open(self.file_path, mode='w', encoding='utf-8').close()

    def save_data(self, data):
        """Save a dictionary of data to the TXT file in a human-readable format."""
        with open(self.file_path, mode='a', encoding='utf-8') as file:
            for key, value in data.items():
                file.write(f"{key.capitalize()}: {value}\n")
            file.write("-" * 40 + "\n")