import pandas as pd
from sqlalchemy import create_engine, text
import glob
from pathlib import Path
import os

# Configuración
DB_URL = "postgresql+psycopg2://postgres:123456@localhost:5432/portfolio_new_stack"
engine = create_engine(DB_URL)

BASE_DIR = Path("04_EXTREMO/data")

def load_csv_to_postgres(file_path, table_name, limit=10000):
    try:
        print(f"Cargando {file_path} en tabla {table_name} (max {limit} filas)...")
        
        # Opciones especiales de carga
        load_args = {'nrows': limit}
        
        # Fix para olist_order_items que parece no tener header
        if "order_items" in str(file_path):
            load_args['header'] = None
            load_args['names'] = ['order_id', 'order_item_id', 'product_id', 'seller_id', 'shipping_limit_date', 'price', 'freight_value']
            
        # Intentar utf-8 primero, luego latin1
        try:
            df = pd.read_csv(file_path, encoding='utf-8', **load_args)
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, encoding='latin1', **load_args)
        
        # Asegurar nombres de tabla en minúsculas
        table_name = table_name.lower()
        
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f" -> OK: {len(df)} filas cargadas.")
    except Exception as e:
        print(f" -> ERROR: {e}")

def main():
    print("Iniciando carga de datasets pesados a PostgreSQL...")
    
    # 1. Favorita (Ecuador)
    fav_path = BASE_DIR / "store_sales_completo"
    if fav_path.exists():
        for csv_file in fav_path.glob("*.csv"):
            table_name = f"favorita_{csv_file.stem}"
            load_csv_to_postgres(csv_file, table_name)
            
    # 2. Brazilian E-Commerce (Olist)
    olist_path = BASE_DIR / "brazilian_ecommerce_completo"
    if olist_path.exists():
        for csv_file in olist_path.glob("*.csv"):
            # Nombres más limpios para Olist
            clean_name = csv_file.stem.replace("olist_", "").replace("_dataset", "")
            table_name = f"olist_{clean_name}"
            load_csv_to_postgres(csv_file, table_name)

    # 3. YouTube Trending
    yt_path = BASE_DIR / "youtube_trending"
    if yt_path.exists():
        for csv_file in yt_path.glob("*.csv"):
            table_name = f"youtube_{csv_file.stem}"
            load_csv_to_postgres(csv_file, table_name)

    print("\nResumen de tablas en base de datos:")
    with engine.connect() as conn:
        res = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")).fetchall()
        for r in res:
            print(f" - {r[0]}")

if __name__ == "__main__":
    main()
