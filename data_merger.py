import pandas as pd

def load_and_prepare_csv(file_path, online=False):
    '''
    Load CSV file and prepare it for merging.
    This function will handle different column names and formats.
    '''
    df = pd.read_csv(file_path)

    # Rename columns if necessary
    if online:
        df.rename(columns={'Online_Price': 'Price', 'Quantity_Sold_Online': 'Quantity_Sold'}, inplace=True)
    else:
        df.rename(columns={'Offline_Price': 'Price', 'Quantity_Sold_Offline': 'Quantity_Sold'}, inplace=True)

    # Ensure consistent date format (if necessary)
    df['Sale_Date'] = pd.to_datetime(df['Sale_Date']).dt.strftime('%Y-%m-%d')

    return df

def merge_datasets(online_file, offline_file, output_file):
    '''
    Merge online and offline sales datasets.
    '''
    # Load and prepare datasets
    online_sales = load_and_prepare_csv(online_file, online=True)
    offline_sales = load_and_prepare_csv(offline_file, online=False)

    # Merge datasets
    total_sales = pd.concat([online_sales, offline_sales], ignore_index=True)

    # Save the merged dataset
    total_sales.to_csv(output_file, index=False)
    print(f"Merged dataset saved as {output_file}")

if __name__ == "__main__":
    merge_datasets('online_sales.csv', 'offline_sales.csv', 'total_sales.csv')
