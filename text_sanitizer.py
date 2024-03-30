import pandas as pd
import re

def clean_text(text):
    """
    Clean the text data by removing special characters and correcting common typos.
    """
    # Correcting common typos
    corrections = {
        "recomended": "recommended",
        "coud": "could",
        "satisfi3d": "satisfied",
        "Excelent": "Excellent"
    }

    for typo, correct in corrections.items():
        text = text.replace(typo, correct)

    # Removing special characters (excluding common punctuation)
    text = re.sub(r'[^A-Za-z0-9\s.,;:!?\'\"]', '', text)

    return text

def main():
    # Read the customer_feedback.csv file
    feedback_df = pd.read_csv('customer_feedback.csv')

    # Apply the cleaning function to the Feedback column
    feedback_df['Feedback'] = feedback_df['Feedback'].apply(clean_text)

    # Save the cleaned data to a new CSV file
    feedback_df.to_csv('feedback_cleaned.csv', index=False)

    print("Data cleaning completed. The cleaned data is saved as feedback_cleaned.csv")

if __name__ == "__main__":
    main()
