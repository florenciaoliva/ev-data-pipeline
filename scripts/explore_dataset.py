import pandas as pd

# Load original dataset
df = pd.read_csv("../data/electric_vehicle_population_raw.csv")

# Primeras filas
print(" Primeras filas:")
print(df.head())

# Columnas
print("\n Columnas del dataset:")
print(df.columns.tolist())

# Tipos de datos
print("\n Tipos de datos:")
print(df.dtypes)

# Recuento de nulos
print("\n Valores nulos por columna:")
print(df.isnull().sum())

# Valores únicos de algunas columnas clave
print("\n Tipos de vehículos eléctricos:")
print(df['Electric Vehicle Type'].unique())

print("\n Elegibilidad CAFV:")
print(df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'].unique())

print("\n Años disponibles:")
print(df['Model Year'].value_counts().sort_index())
