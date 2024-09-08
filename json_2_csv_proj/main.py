import os
import json
from data_process.processor import DataProcessor
from data_process.utils import validate_json

def main():
    # Define the path to the JSON file
    json_file_path = os.path.join("raw_data", "case.json")
    
    # Check if the file exists
    if not os.path.exists(json_file_path):
        print(f"File {json_file_path} not found.")
        return
    
    # Read the JSON file
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return
    
    # Validate the JSON data
    try:
        validate_json(data)
    except ValueError as e:
        print(f"Validation failed: {e}")
        return

    # Initialize Data Processor
    processor = DataProcessor(output_dir="csv_output")

    # Process the data and store to CSV
    processor.process_json(data)

if __name__ == "__main__":
    main()