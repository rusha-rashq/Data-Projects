import pandas as pd

def filter_sales_by_date_range(input_file='sales_history.csv', start_date='2021-01-15', end_date='2021-02-15', output_file='sales_filtered.csv'):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Convert the 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Filter the DataFrame based on the date range
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

    # Save the filtered data to a new CSV file
    filtered_df.to_csv(output_file, index=False)
    print(f"Filtered data saved to {output_file}")

if __name__ == "__main__":
    filter_sales_by_date_range()

