import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load Your IPL Dataset
file_path = r'C:\Users\Sankalp Sharma\Downloads\indian-premier-league-dataset\matches.csv'  # Update to the correct CSV file extracted from the zip

try:
    # Attempt to read the CSV file
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

# Step 2: Data Analysis and Visualization

# Example Analysis: Count of Matches by Season
matches_by_season = df['season'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
matches_by_season.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Count of Matches by Season", fontsize=16)
plt.xlabel("Season", fontsize=14)
plt.ylabel("Number of Matches", fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Example Analysis: Most Successful Teams (Matches Won)
most_successful_teams = df['winner'].value_counts().head(10)

plt.figure(figsize=(10, 5))
most_successful_teams.plot(kind='bar', color='orange', edgecolor='black')
plt.title("Top 10 Most Successful Teams (Matches Won)", fontsize=16)
plt.xlabel("Team", fontsize=14)
plt.ylabel("Matches Won", fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Example Analysis: Toss Decision Analysis
toss_decision_count = df['toss_decision'].value_counts()

plt.figure(figsize=(7, 5))
toss_decision_count.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
plt.title("Toss Decision Distribution", fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures pie chart is circular
plt.tight_layout()
plt.show()

# Example Analysis: Winning by Run Margin Distribution
plt.figure(figsize=(10, 5))
plt.hist(df['win_by_runs'], bins=30, edgecolor='blue', color='lightgreen')
plt.title("Distribution of Win by Runs", fontsize=16)
plt.xlabel("Win by Runs", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Example Analysis: Winning by Wickets Distribution
plt.figure(figsize=(10, 5))
plt.hist(df['win_by_wickets'], bins=11, edgecolor='red', color='lightblue')
plt.title("Distribution of Win by Wickets", fontsize=16)
plt.xlabel("Win by Wickets", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
