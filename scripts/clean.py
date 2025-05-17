import pandas as pd

# Load local CSV
df = pd.read_csv("data/electric_vehicle_population_raw.csv")

# Standardize column names: lowercase, underscores, no special characters
df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace("[^a-z0-9_]", "", regex=True)

# Ensure model_year is numeric
df['model_year'] = pd.to_numeric(df['model_year'], errors='coerce')

# Filter out invalid years: keep only rows with model_year <= 2025
df = df[df['model_year'] <= 2025]

# Drop rows with missing critical information
df = df.dropna(subset=['model_year', 'county'])

# Optional: strip whitespace in object columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()

# Save cleaned dataset
df.to_csv("data/cleaned_ev_data.csv", index=False)


print("Cleaned data saved to 'data/cleaned_ev_data.csv'")
print(f" Final number of records: {len(df)}")
print(f" Columns: {list(df.columns)}")
