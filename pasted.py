import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load Your IPL Datasets
player_file_path = r'C:\Users\Sankalp Sharma\Downloads\indian-premier-league-dataset\Player.csv'  # Update this path
team_file_path = r'C:\Users\Sankalp Sharma\Downloads\indian-premier-league-dataset\Team.csv'  # Update this path

try:
    # Load Player data
    player_df = pd.read_csv(player_file_path, sep=',', on_bad_lines='skip', encoding='utf-8')
    print("Player CSV file read successfully!")
    print(player_df.head())  # Display the first few rows of the Player dataset

    # Load Team data
    team_df = pd.read_csv(team_file_path, sep=',', on_bad_lines='skip', encoding='utf-8')
    print("Team CSV file read successfully!")
    print(team_df.head())  # Display the first few rows of the Team dataset

except FileNotFoundError as e:
    print(f"Error: {e}")
except pd.errors.ParserError as e:
    print("ParserError: ", e)
    print("Please check the file for formatting issues.")
except Exception as e:
    print("An unexpected error occurred: ", e)

# Proceed only if player_df and team_df are defined
if 'player_df' in globals() and 'team_df' in globals():
    # Convert DOB to datetime and calculate age
    player_df['DOB'] = pd.to_datetime(player_df['DOB'], format='%d-%b-%y', errors='coerce')  # Specified format
    player_df['Age'] = (pd.Timestamp.now() - player_df['DOB']).dt.days // 365  # Calculate age in years

    # Define players_by_country
    players_by_country = player_df['Country'].value_counts()

    # Visualization 1: Count of Players by Team (Bar Chart)
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

    # Visualization 2: Players Overview (Pie Chart)
    plt.figure(figsize=(8, 8))
    player_df['Batting_Hand'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['gold', 'lightblue'])
    plt.title("Batting Hand Distribution", fontsize=16)
    plt.ylabel("")  # Hide y-label
    plt.savefig('batting_hand_distribution.png')  # Save as PNG
    plt.show()

    # Visualization 3: Players Age Distribution (Histogram)
    plt.figure(figsize=(10, 5))
    plt.hist(player_df['Age'].dropna(), bins=10, color='orange', edgecolor='black')
    plt.title("Age Distribution of Players", fontsize=16)
    plt.xlabel("Age", fontsize=14)
    plt.ylabel("Number of Players", fontsize=14)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig('age_distribution.png')  # Save as PNG
    plt.show()

    # Visualization 4: Scatter Plot (Age vs Number of Players)
    plt.figure(figsize=(10, 5))
    age_counts = player_df['Age'].value_counts().reset_index()
    age_counts.columns = ['Age', 'Count']
    plt.scatter(age_counts['Age'], age_counts['Count'], color='purple', alpha=0.6)
    plt.title("Age vs Number of Players", fontsize=16)
    plt.xlabel("Age", fontsize=14)
    plt.ylabel("Number of Players", fontsize=14)
    plt.grid()
    plt.tight_layout()
    plt.savefig('age_vs_players.png')  # Save as PNG
    plt.show()

    # Visualization 5: Box Plot (Age Distribution by Country)
    plt.figure(figsize=(10, 5))
    player_df.boxplot(column='Age', by='Country', grid=False)
    plt.title("Age Distribution by Country", fontsize=16)
    plt.suptitle("")  # Suppress the default title
    plt.xlabel("Country", fontsize=14)
    plt.ylabel("Age", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('age_distribution_by_country.png')  # Save as PNG
    plt.show()

    # Visualization 6: Area Plot (Age Distribution)
    plt.figure(figsize=(10, 5))
    age_distribution = player_df['Age'].value_counts().sort_index()
    age_distribution.plot(kind='area', color='lightgreen', alpha=0.5)
    plt.title("Area Plot of Age Distribution", fontsize=16)
    plt.xlabel("Age", fontsize=14)
    plt.ylabel("Number of Players", fontsize=14)
    plt.grid()
    plt.tight_layout()
    plt.savefig('age_area_plot.png')  # Save as PNG
    plt.show()

    # Visualization 7: Hexbin Plot (Age vs Number of Players)
    plt.figure(figsize=(10, 5))
    plt.hexbin(age_counts['Age'], age_counts['Count'], gridsize=20, cmap='Blues')
    plt.colorbar(label='Number of Players')
    plt.title("Hexbin Plot of Age vs Number of Players", fontsize=16)
    plt.xlabel("Age", fontsize=14)
    plt.ylabel("Number of Players", fontsize=14)
    plt.tight_layout()
    plt.savefig('hexbin_plot.png')  # Save as PNG
    plt.show()

    # Visualization 8: Subplots
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    
    # Bar chart
    players_by_country.plot(kind='bar', ax=axs[0, 0], color='skyblue', edgecolor='black')
    axs[0, 0].set_title("Count of Players by Country", fontsize=12)
    axs[0, 0].set_xlabel("Country", fontsize=10)
    axs[0, 0].set_ylabel("Number of Players", fontsize=10)
    
    # Pie chart
    player_df['Batting_Hand'].value_counts().plot(kind='pie', ax=axs[0, 1], autopct='%1.1f%%', startangle=90, colors=['gold', 'lightblue'])
    axs[0, 1].set_title("Batting Hand Distribution", fontsize=12)
    axs[0, 1].set_ylabel("")  # Hide y-label
    
    # Histogram
    axs[1, 0].hist(player_df['Age'].dropna(), bins=10, color='orange', edgecolor='black')
    axs[1, 0].set_title("Age Distribution of Players", fontsize=12)
    axs[1, 0].set_xlabel("Age", fontsize=10)
    axs[1, 0].set_ylabel("Number of Players", fontsize=10)

    # Scatter Plot
    axs[1, 1].scatter(age_counts['Age'], age_counts['Count'], color='purple', alpha=0.6)
    axs[1, 1].set_title("Age vs Number of Players", fontsize=12)
    axs[1, 1].set_xlabel("Age", fontsize=10)
    axs[1, 1].set_ylabel("Number of Players", fontsize=10)

    plt.tight_layout()
    plt.savefig('subplots_overview.png')  # Save as PNG
    plt.show()

else:
    print("DataFrames not loaded. Please check the file paths and try again.")
