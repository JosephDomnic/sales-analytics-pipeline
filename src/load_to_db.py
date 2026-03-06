import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv('data/processed/clean_sales.csv')

# Connect to database (creates the file automatically)
conn = sqlite3.connect('data/sales.db')

# Load data into database
df.to_sql('sales', conn, if_exists='replace', index=False)

print(f"Done! {len(df)} rows loaded into database.")
conn.close()