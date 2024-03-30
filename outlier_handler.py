import pandas as pd

def handle_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Replacing outliers with the median
    outliers = ((df[column] < lower_bound) | (df[column] > upper_bound))
    df.loc[outliers, column] = df[column].median()
    return df

def main():
    # Load the data
    df = pd.read_csv('sales_data.csv')

    # Handle outliers in the 'Sales' column
    df_refined = handle_outliers(df, 'Sales')

    # Save the refined data
    df_refined.to_csv('sales_refined.csv', index=False)

if __name__ == "__main__":
    main()
