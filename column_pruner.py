import pandas as pd

def prune_columns(file_path, columns_to_remove, output_file_path):
    """
    Removes specified columns from a CSV file and saves the pruned data to a new file.

    Parameters:
    file_path (str): Path to the input CSV file.
    columns_to_remove (list): List of columns to be removed.
    output_file_path (str): Path to save the output CSV file.
    """
    # Reading the data
    data = pd.read_csv(file_path)

    # Removing specified columns
    pruned_data = data.drop(columns=columns_to_remove, errors='ignore')

    # Saving the pruned data
    pruned_data.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    # Example usage
    file_path = 'survey_data_large.csv'
    columns_to_remove = ['Opinion1', 'Opinion2', 'Opinion3', 'Opinion4']  # Example columns to remove
    output_file_path = 'survey_data_pruned.csv'

    prune_columns(file_path, columns_to_remove, output_file_path)
