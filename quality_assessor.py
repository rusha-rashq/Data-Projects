import pandas as pd

def assess_data_quality(file_path):
    # Read the data
    df = pd.read_csv(file_path)

    # Initial Data Quality Report
    report = f"Initial Data Report:\n{df.describe(include='all')}\n\n"

    # Check for missing values
    missing_values = df.isnull().sum()
    report += f"Missing Values:\n{missing_values}\n\n"

    # Check for anomalies (e.g., negative values in certain columns)
    anomalies = df[(df['Heart Rate'] < 0) | (df['Temperature'] <= 0)]
    report += f"Anomalies Detected:\n{anomalies}\n\n"

    # Clean the data
    # Replace negative values with NaN
    df.loc[df['Heart Rate'] < 0, 'Heart Rate'] = None
    df.loc[df['Temperature'] <= 0, 'Temperature'] = None

    # Handle missing values (e.g., fill with mean or median)
    df['Blood Pressure'].fillna(df['Blood Pressure'].mean(), inplace=True)
    df['Heart Rate'].fillna(df['Heart Rate'].mean(), inplace=True)
    df['Temperature'].fillna(df['Temperature'].mean(), inplace=True)

    # Final Data Quality Report
    report += f"Final Data Report after Cleaning:\n{df.describe(include='all')}\n"

    # Save the cleaned data
    cleaned_file_path = file_path.replace('.csv', '_cleaned.csv')
    df.to_csv(cleaned_file_path, index=False)

    return report

# Example usage
file_path = 'patient_records.csv'
report = assess_data_quality(file_path)

# Save the report to a text file
with open('data_quality_report.txt', 'w') as file:
    file.write(report)
