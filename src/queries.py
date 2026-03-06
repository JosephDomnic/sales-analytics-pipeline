import sqlite3
import pandas as pd

conn = sqlite3.connect('data/sales.db')

# Sales by Region
region_sales = pd.read_sql("""
  SELECT region, ROUND(SUM(sales),2) as total_sales
  FROM sales GROUP BY region ORDER BY total_sales DESC
""", conn)

# Profit by Category
category_profit = pd.read_sql("""
  SELECT category, ROUND(SUM(profit),2) as total_profit
  FROM sales GROUP BY category ORDER BY total_profit DESC
""", conn)

# Monthly Sales Trend
monthly_trend = pd.read_sql("""
  SELECT strftime('%Y-%m', order_date) as month,
  ROUND(SUM(sales),2) as total_sales
  FROM sales GROUP BY month ORDER BY month
""", conn)

conn.close()

print("=== Sales by Region ===")
print(region_sales)
print("\n=== Profit by Category ===")
print(category_profit)