import pandas as pd

def correct_dtypes(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Correcting data types
    df['Quantity'] = df['Quantity'].astype(int)
    df['Price'] = df['Price'].astype(float)

    # Saving the corrected DataFrame
    df.to_csv('inventory_corrected.csv', index=False)

if __name__ == "__main__":
    correct_dtypes('inventory_data.csv')
