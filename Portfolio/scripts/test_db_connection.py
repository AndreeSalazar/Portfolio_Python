from sqlalchemy import create_engine, text

try:
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/portfolio_new_stack')
    with engine.connect() as conn:
        print("Conexión exitosa via SQLAlchemy!")
        res = conn.execute(text("SELECT 1")).scalar()
        print(f"Resultado: {res}")
except Exception as e:
    print(f"Error SQLAlchemy: {e}")

import psycopg2
try:
    conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/portfolio_new_stack")
    print("Conexión exitosa via psycopg2 directo!")
    conn.close()
except Exception as e:
    print(f"Error psycopg2: {e}")
