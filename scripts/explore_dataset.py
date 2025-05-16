import pandas as pd

# Load original dataset
df = pd.read_csv("../data/electric_vehicle_population_raw.csv")

# First rows
print(" First rows:")
print(df.head())

# Columns
print("\n Dataset columns:")
print(df.columns.tolist())

# Data types
print("\n Data types:")
print(df.dtypes)

# Null values per column
print("\n Null values per column:")
print(df.isnull().sum())

# Unique values of some key columns
print("\n Electric Vehicle Types:")
print(df['Electric Vehicle Type'].unique())

print("\n Eligibility CAFV:")
print(df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'].unique())

print(df['Electric Vehicle Type'].isnull().sum())
print(df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'].isnull().sum())


print("\n Years:")
print(df['Model Year'].value_counts().sort_index())
