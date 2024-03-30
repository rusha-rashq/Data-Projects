import pandas as pd
import glob

def combine_csv_files(files):
    # Combine multiple CSV files into a single DataFrame
    combined_df = pd.concat([pd.read_csv(f) for f in files])
    # Drop duplicates
    combined_df.drop_duplicates(inplace=True)
    return combined_df

def main():
    # List of CSV files to combine
    csv_files = glob.glob('data_part*.csv')
    # Combine files
    combined_df = combine_csv_files(csv_files)
    # Save the combined data to a new CSV file
    combined_df.to_csv('data_full.csv', index=False)
    print("Combined dataset saved as data_full.csv")

if __name__ == "__main__":
    main()
