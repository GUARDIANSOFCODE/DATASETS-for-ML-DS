import pandas as pd

# Step 1: Define the data for 150 countries
countries = [
    'USA', 'Canada', 'UK', 'Germany', 'France', 'Australia', 'India', 'China', 'Brazil', 
    'South Africa', 'Japan', 'South Korea', 'Italy', 'Spain', 'Russia', 'Mexico', 
    'Netherlands', 'Sweden', 'Norway', 'Argentina', 'Saudi Arabia', 'Turkey', 'Switzerland', 
    'Belgium', 'Austria', 'Denmark', 'Finland', 'Ireland', 'Portugal', 'Czech Republic', 
    'Greece', 'Hungary', 'Poland', 'Romania', 'Israel', 'Singapore', 'Malaysia', 'Indonesia', 
    'Thailand', 'Vietnam', 'Philippines', 'Nigeria', 'Kenya', 'Colombia', 'Chile', 'Peru', 
    'Egypt', 'Pakistan', 'Bangladesh', 'Iraq', 'Ukraine', 'Kazakhstan', 'Uzbekistan', 'Sri Lanka', 
    'Morocco', 'Algeria', 'Tanzania', 'Ethiopia', 'Angola', 'Zimbabwe', 'Ghana', 'Ivory Coast', 
    'Senegal', 'Cameroon', 'Uganda', 'Sudan', 'Jamaica', 'Dominican Republic', 'Costa Rica', 
    'Honduras', 'El Salvador', 'Nicaragua', 'Panama', 'Cuba', 'Puerto Rico', 'New Zealand', 
    'Fiji', 'Papua New Guinea', 'Samoa', 'Tonga', 'Vanuatu', 'Kiribati', 'Marshall Islands', 
    'Micronesia', 'Solomon Islands', 'Tuvalu', 'Bhutan', 'Maldives', 'Mongolia', 'Laos', 
    'Myanmar', 'Cambodia', 'Brunei', 'Timor-Leste', 'Kuwait', 'Qatar', 'Bahrain', 'Oman', 
    'Cyprus', 'Malta', 'Estonia', 'Latvia', 'Lithuania', 'Slovakia', 'Slovenia', 
    'Bosnia and Herzegovina', 'Serbia', 'Montenegro', 'North Macedonia', 'Albania', 
    'Georgia', 'Armenia', 'Azerbaijan', 'Kyrgyzstan', 'Tajikistan', 'Turkmenistan', 
    'Belarus', 'Moldova', 'Zambia', 'Malawi', 'Rwanda', 'Burundi', 
    'Gambia', 'Sierra Leone', 'Togo', 'Benin', 'Central African Republic', 'Chad', 
    'Republic of the Congo', 'Democratic Republic of the Congo', 'Equatorial Guinea', 
    'Gabon', 'Lesotho', 'Eswatini', 'Mauritius', 'Seychelles', 'Comoros', 'Djibouti'
]

# Step 2: Create the data dictionary with consistent lengths
num_entries_per_country = 10  # Number of entries per country
data = {
    'Country': [],
    'City': [],
    'Age': [],
    'Population_Density': [],
    'Wages': [],
    'Medicare_Eligibility': [],
    'Employees': []
}

# Populate the data dictionary with more realistic values
for country in countries:
    for i in range(num_entries_per_country):
        data['Country'].append(country)
        data['City'].append(f"{country} City {i + 1}")  # Example city name
        data['Age'].append(30 + i)  # Age between 30 and 39 (realistic range)
        data['Population_Density'].append(100 + (i * 20))  # Example density with incremental steps
        data['Wages'].append(40000 + (i * 2000))  # Example wage with realistic increments
        data['Medicare_Eligibility'].append('Yes' if i % 2 == 0 else 'No')  # Alternate eligibility
        data['Employees'].append(250 + (i * 5))  # Example employee count with small increments

# Step 3: Create DataFrame
df = pd.DataFrame(data)

# Step 4: Save DataFrame to CSV
output_file_path = 'country_data_large_150.csv'
df.to_csv(output_file_path, index=False)
print(f"CSV file '{output_file_path}' generated successfully!")
