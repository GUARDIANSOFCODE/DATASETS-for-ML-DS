import pandas as pd
import numpy as np

# Random data generation
np.random.seed(42)

# Sample data arrays
species_names = [
    "Bengal Tiger", "Blue Whale", "Red Maple", "African Elephant", "Rose Bush",
    "Golden Eagle", "Giant Sequoia", "Orca", "Cactus", "King Cobra"
]
species_types = ["Mammal", "Bird", "Tree", "Shrub", "Fish", "Reptile", "Flower"]
colors = ["Green", "Red", "Blue", "Yellow", "Brown", "White", "Black", "Purple"]
countries = ["India", "USA", "Australia", "Brazil", "China", "South Africa", "Canada", "Japan"]
avg_heights = np.random.randint(10, 400, size=200)
lifespans = np.random.randint(1, 150, size=200)
temperatures = np.random.randint(-10, 45, size=200)

# Create the DataFrame
data = {
    "Species Name": np.random.choice(species_names, 200),
    "Type": np.random.choice(species_types, 200),
    "Average Height (cm)": avg_heights,
    "Lifespan (years)": lifespans,
    "Temperature Range (°C)": temperatures,
    "Country": np.random.choice(countries, 200),
    "Colors": [", ".join(np.random.choice(colors, size=np.random.randint(1, 4), replace=False)) for _ in range(200)],
}

df = pd.DataFrame(data)

# Save to CSV
file_path = r'/mnt/data/flora_fauna_enhanced_data.csv'
df.to_csv(file_path, index=False)

print(f"Dataset created and saved to {file_path}!")
