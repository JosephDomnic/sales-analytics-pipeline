# Sales Analytics Pipeline

An end-to-end data pipeline that ingests, cleans, stores and visualizes
retail sales data — with an AI agent for natural language querying.

## Architecture
Raw CSV -> Python Cleaning -> SQLite Database -> SQL Queries -> Streamlit Dashboard -> AI Agent

## Dashboard
![Dashboard Screenshot](dashboard.png)

## How to Run

### 1. Install dependencies
pip install pandas streamlit matplotlib seaborn requests

### 2. Run the full pipeline
python pipeline.py

### 3. Launch dashboard
streamlit run app.py

### 4. Run the AI agent
python agent.py

## AI Agent Setup
Ask questions about the data in plain English. The agent writes SQL automatically and returns business insights.

Get a free Gemini key from: https://aistudio.google.com
Get an Anthropic key from: https://console.anthropic.com

Open agent.py and set your key and preferred provider at the top of the file.

Example questions:
- which region has the highest profit?
- what is the best performing category?
- show me the top 5 sub-categories by sales

## Tech Stack
- Python + Pandas (data cleaning)
- SQLite (data warehouse)
- Streamlit (dashboard)
- GitHub Actions (automated CI/CD)
- Gemini / Anthropic API (AI agent)

## Key Learnings
- Built an automated ETL pipeline from scratch
- Modelled a data warehouse using SQL
- Automated pipeline runs using GitHub Actions CI/CD
- Visualized business KPIs for stakeholder consumption
- Built an AI agent for natural language data querying