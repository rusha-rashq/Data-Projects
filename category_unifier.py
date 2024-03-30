import pandas as pd

def standardize_categories(file_path):
    # Load data
    df = pd.read_csv(file_path)

    # Standardize category data
    df['category'] = df['category'].str.lower().str.strip()

    # Save the updated dataset
    df.to_csv('products_standardized.csv', index=False)

if __name__ == "__main__":
    standardize_categories('product_data.csv')
