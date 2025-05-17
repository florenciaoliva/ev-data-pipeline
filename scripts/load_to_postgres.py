import pandas as pd
from sqlalchemy import create_engine

# Read cleaned dataset
df = pd.read_csv("data/cleaned_ev_data.csv")

DB_USER = "ev_data_user"
DB_PASSWORD = "ev_password"

# PostgreSQL connection (adjust with your user/password)
engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost:5432/ev_data"
)

# Load data to PostgreSQL
df.to_sql("vehicles", engine, if_exists="replace", index=False)

print(" Data loaded into PostgreSQL table 'vehicles'")
