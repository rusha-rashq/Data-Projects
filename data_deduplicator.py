import pandas as pd

def remove_duplicates(file_path, columns, output_file):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Remove duplicates
    df_unique = df.drop_duplicates(subset=columns)

    # Save the deduplicated DataFrame
    df_unique.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Define the input and output file paths
    input_file = 'customer_orders.csv'
    output_file = 'orders_unique.csv'

    # Columns to consider for deduplication
    columns = ['CustomerID', 'OrderDate']

    # Run the deduplication function
    remove_duplicates(input_file, columns, output_file)
