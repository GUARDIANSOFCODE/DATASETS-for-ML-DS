import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load Your IPL Datasets
player_file_path = r'C:\Users\Sankalp Sharma\Downloads\indian-premier-league-dataset\Player.csv'  # Path to Player.csv
team_file_path = r'C:\Users\Sankalp Sharma\Downloads\indian-premier-league-dataset\Team.csv'  # Path to Team.csv

try:
    # Load Player data
    player_df = pd.read_csv(player_file_path, sep=',', on_bad_lines='skip', encoding='utf-8')
    print("Player CSV file read successfully!")
    print(player_df.head())  # Display the first few rows of the Player dataset
    print("Player Columns:", player_df.columns)  # Display all columns

    # Load Team data
    team_df = pd.read_csv(team_file_path, sep=',', on_bad_lines='skip', encoding='utf-8')
    print("Team CSV file read successfully!")
    print(team_df.head())  # Display the first few rows of the Team dataset
    print("Team Columns:", team_df.columns)  # Display all columns

except FileNotFoundError as e:
    print(f"Error: {e}")
except pd.errors.ParserError as e:
    print("ParserError: ", e)
    print("Please check the file for formatting issues.")
except Exception as e:
    print("An unexpected error occurred: ", e)

# Proceed only if player_df and team_df are defined
if 'player_df' in globals() and 'team_df' in globals():
    # Check if there's a column in player_df that can link to team_df
    # This is where you need to have a common column, such as 'Country' or create a manual mapping.
    
    # Example: Create a mapping if possible (this is hypothetical, adjust accordingly)
    # Assuming you want to count players by country or any other linking criteria
    players_by_country = player_df['Country'].value_counts()  # Using 'Country' as an example

    plt.figure(figsize=(10, 5))
    players_by_country.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Count of Players by Country", fontsize=16)
    plt.xlabel("Country", fontsize=14)
    plt.ylabel("Number of Players", fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('players_by_country.png')  # Save as PNG
    plt.show()

    # Additional analysis can go here as per your requirements

else:
    print("DataFrames not loaded. Please check the file paths and try again.")
