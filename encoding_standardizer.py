import pandas as pd
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read(50000)  # Read first 50,000 bytes to guess encoding
    return chardet.detect(raw_data)['encoding']

def read_and_convert(file_path, encoding):
    try:
        # Read the file with the detected encoding
        df = pd.read_csv(file_path, encoding=encoding)
        return df
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

def main():
    input_file = 'international_data.csv'
    output_file = 'data_utf8.csv'

    # Detect encoding
    encoding = detect_encoding(input_file)
    print(f"Detected encoding: {encoding}")

    # Read and convert
    df = read_and_convert(input_file, encoding)
    if df is not None:
        # Save to new file with UTF-8 encoding
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"File saved with UTF-8 encoding: {output_file}")

if __name__ == "__main__":
    main()
