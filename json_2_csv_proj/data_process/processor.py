import csv
import os
import json
from datetime import datetime

class DataProcessor:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def process_json(self, data):
        """
        Process incoming JSON and convert it to CSV rows.
        """
        timestamp = data.get("timestamp")
        event_name = data.get("event_name")
        payload = data.get("payload")

        # Create a row to insert into CSV
        row = {
            "timestamp": timestamp,
            "event_name": event_name,
            **payload  # Spread the payload into individual columns
        }

        # Save to CSV based on event_name
        self.save_to_csv(event_name, row)

    def save_to_csv(self, event_name, row):
        """
        Save the processed row to a CSV file named after the event_name.
        """
        csv_file = os.path.join(self.output_dir, f"{event_name}.csv")
        file_exists = os.path.isfile(csv_file)

        # Write the row to CSV file
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=row.keys())
            if not file_exists:
                writer.writeheader()  # Write header only if file is new
            writer.writerow(row)