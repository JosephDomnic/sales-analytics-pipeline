import pandas as pd

# Load raw data
df = pd.read_csv('data/raw/superstore.csv', encoding='latin1')

# Basic cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df['order_date'] = pd.to_datetime(df['order_date'])
df = df.dropna()

# Save cleaned data
df.to_csv('data/processed/clean_sales.csv', index=False)
print(f"Done! {len(df)} rows cleaned and saved.")