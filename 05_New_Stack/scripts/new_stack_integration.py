from pathlib import Path
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
from datetime import datetime, timedelta
import psycopg2
from urllib.parse import urlparse
try:
    import polars as pl
    _HAS_PL = True
except Exception:
    _HAS_PL = False
try:
    import faststack
    _HAS_FAST = True
except Exception:
    _HAS_FAST = False

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/portfolio_new_stack"

def _read_csv(path):
    if _HAS_PL:
        return pl.read_csv(path).to_pandas()
    return pd.read_csv(path)

def ensure_database_exists(db_url: str):
    parsed = urlparse(db_url)
    dbname = parsed.path.lstrip("/")
    admin_url = f"postgresql://{parsed.username}:{parsed.password}@{parsed.hostname}:{parsed.port}/postgres"
    try:
        conn = psycopg2.connect(admin_url)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = %s;", (dbname,))
        exists = cur.fetchone() is not None
        if not exists:
            cur.execute(f'CREATE DATABASE "{dbname}";')
        cur.close()
        conn.close()
    except Exception:
        pass

def generar_train_csv(out_path, start_date, days, stores, items):
    fechas = [start_date + timedelta(days=i) for i in range(days)]
    rows = []
    for fecha in fechas:
        dow = fecha.weekday()
        for s in range(1, stores + 1):
            for item in range(1, items + 1):
                if _HAS_FAST:
                    unit_sales = int(faststack.generar_unit_sales(dow, False))
                else:
                    base = np.random.randint(0, 100)
                    if dow in [5, 6]:
                        base = int(base * 1.5)
                    unit_sales = int(base * np.random.uniform(0.5, 1.5))
                if unit_sales > 0:
                    rows.append({
                        "date": fecha.strftime("%Y-%m-%d"),
                        "store_nbr": s,
                        "item_nbr": item,
                        "unit_sales": int(unit_sales),
                        "onpromotion": bool(np.random.randint(0, 2))
                    })
    df = pd.DataFrame(rows)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    return df

def cargar_a_postgresql(df):
    ensure_database_exists(DATABASE_URL)
    engine = create_engine(DATABASE_URL, connect_args={"client_encoding": "utf8"}, pool_pre_ping=True)
    df.to_sql("train_new_stack", engine, if_exists="replace", index=False, method="multi", chunksize=5000)
    with engine.connect() as conn:
        count = conn.execute(text("SELECT COUNT(*) FROM train_new_stack")).scalar()
        schema_path = Path("05_New_Stack/sql/schema_new_stack.sql")
        if schema_path.exists():
            sql_text = schema_path.read_text(encoding="utf-8")
            try:
                conn.execute(text(sql_text))
            except Exception:
                pass
    return count

def main():
    base_path = Path("05_New_Stack/data")
    csv_path = base_path / "train.csv"
    df = generar_train_csv(csv_path, datetime(2024, 1, 1), 7, 10, 50)
    count = cargar_a_postgresql(df)
    print(str(csv_path))
    print(str(count))

if __name__ == "__main__":
    main()
