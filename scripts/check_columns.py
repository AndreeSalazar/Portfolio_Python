from sqlalchemy import create_engine, text
import pandas as pd

DB_URL = "postgresql+psycopg2://postgres:123456@localhost:5432/portfolio_new_stack"
engine = create_engine(DB_URL)

def check_columns(table):
    try:
        df = pd.read_sql(f"SELECT * FROM {table} LIMIT 0", engine)
        print(f"Table {table} columns: {list(df.columns)}")
    except Exception as e:
        print(f"Error reading {table}: {e}")

check_columns("olist_products")
check_columns("olist_order_items")
check_columns("favorita_train")
check_columns("youtube_youtube_trending_US")
