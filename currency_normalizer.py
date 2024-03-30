
import pandas as pd
from forex_python.converter import CurrencyRates

def normalize_currencies(file_path, output_path):
    # Load the data
    df = pd.read_csv(file_path)

    # Initialize the currency converter
    c = CurrencyRates()

    # Normalize currencies to USD
    df['Amount'] = df.apply(lambda row: round(c.convert(row['Currency'], 'USD', row['Amount']), 2) 
                            if row['Currency'] != 'USD' else row['Amount'], axis=1)
    df['Currency'] = 'USD'

    # Save the normalized data
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_path = 'financial_data.csv'
    output_path = 'financial_data_normalized.csv'
    normalize_currencies(input_path, output_path)
