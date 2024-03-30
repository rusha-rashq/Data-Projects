import pandas as pd

def standardize_coordinates(coord_str):
    '''
    Standardize the format of geographical coordinates.
    Accepts a string in the format 'latitude, longitude' and returns a standardized version.
    '''
    try:
        lat, lon = map(float, coord_str.split(','))
        return f'{lat:.6f}, {lon:.6f}'
    except ValueError:
        return None

def process_dataset(file_path, output_file_path):
    '''
    Process the dataset to standardize the coordinates and address inconsistencies.
    '''
    # Read the dataset
    df = pd.read_csv(file_path)

    # Standardize coordinates
    df['Coordinates'] = df['Coordinates'].apply(standardize_coordinates)

    # Drop rows with invalid coordinates
    df = df.dropna(subset=['Coordinates'])

    # Save the processed dataset
    df.to_csv(output_file_path, index=False)

if __name__ == '__main__':
    input_file_path = 'location_data.csv'
    output_file_path = 'location_data_standardized.csv'
    process_dataset(input_file_path, output_file_path)
