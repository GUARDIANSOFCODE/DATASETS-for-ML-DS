import zipfile
import os
import pandas as pd

# Define the path to your downloaded zip file
zip_file_path = r'C:\Users\Sankalp Sharma\Downloads\archive.zip'  # Update this path as needed

# Step 1: Extract the zip file
try:
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(r'C:\Users\Sankalp Sharma\Downloads\indian-premier-league-dataset')  # Specify the directory where you want to extract
    print("Zip file extracted successfully!")
except FileNotFoundError:
    print(f"Error: The file '{zip_file_path}' does not exist. Please check the path and try again.")
    exit()

# Step 2: Load the extracted CSV file
file_path = r'C:\Users\Sankalp Sharma\Downloads\indian-premier-league-dataset\ipl_dataset.csv'  # Update this to the actual extracted CSV file
try:
    df = pd.read_csv(file_path, sep=',', on_bad_lines='skip', encoding='utf-8')
    print("CSV file read successfully!")
    print("\nSample Data:")
    print(df.head())  # Display the first few rows of the dataset

except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist. Please check the path and try again.")
    exit()
except pd.errors.ParserError as e:
    print("ParserError: ", e)
    print("Please check the file for formatting issues.")
    exit()
except Exception as e:
    print("An unexpected error occurred: ", e)
    exit()
