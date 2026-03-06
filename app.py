import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Sales Analytics Pipeline", page_icon="📊")

st.title("📊 Sales Analytics Pipeline")
st.caption("Built by Ayush Singh | TPM Project")

conn = sqlite3.connect('data/sales.db')

# KPI Cards
df = pd.read_sql("SELECT * FROM sales", conn)
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${df['sales'].sum():,.0f}")
col2.metric("Total Profit", f"${df['profit'].sum():,.0f}")
col3.metric("Total Orders", f"{len(df):,}")

st.divider()

# Sales by Region
st.subheader("Sales by Region")
region_data = pd.read_sql("""
  SELECT region, ROUND(SUM(sales),2) as total_sales
  FROM sales GROUP BY region ORDER BY total_sales DESC
""", conn)
st.bar_chart(region_data.set_index('region'))

# Profit by Category
st.subheader("Profit by Category")
cat_data = pd.read_sql("""
  SELECT category, ROUND(SUM(profit),2) as total_profit
  FROM sales GROUP BY category ORDER BY total_profit DESC
""", conn)
st.bar_chart(cat_data.set_index('category'))

conn.close()