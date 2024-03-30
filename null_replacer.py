import pandas as pd

def replace_nulls(file_path, output_path):
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Replace nulls in numerical columns with 0
    for col in df.select_dtypes(include=['float64', 'int64']):
        df[col].fillna(0, inplace=True)

    # Replace nulls in object (text) columns with 'Unknown'
    for col in df.select_dtypes(include=['object']):
        df[col].fillna('Unknown', inplace=True)

    # Save the updated DataFrame
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_file_path = 'employee_records.csv'
    output_file_path = 'employees_updated.csv'
    replace_nulls(input_file_path, output_file_path)
