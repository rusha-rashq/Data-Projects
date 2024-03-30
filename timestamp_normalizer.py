import pandas as pd
from dateutil import parser

def normalize_timestamps(input_file, output_file):
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)

        # Normalize timestamp format
        df['Timestamp'] = df['Timestamp'].apply(lambda x: parser.parse(x).strftime('%Y-%m-%d %H:%M:%S'))

        # Save the cleaned data
        df.to_csv(output_file, index=False)
        print(f"File '{output_file}' has been saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    normalize_timestamps('event_logs.csv', 'events_normalized.csv')
