"""
Script para cargar TODOS los datos de 02_Intermedio a PostgreSQL
Portfolio Data Analyst - Nivel Intermedio

Este script prepara una base de datos analítica unificada con:
- Datos de e-commerce (customers, orders, order_items, products)
- Datos de marketing (marketing_analytics)
- Datos de ventas online (online_retail)
"""

import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path
import sys


# ============================================================
# 🔐 Configuración de conexión
# ============================================================
# Usamos tu contraseña de PostgreSQL: 123456
# Puedes cambiar el nombre de la base de datos si lo prefieres.
DATABASE_URL = "postgresql://postgres:123456@localhost:5432/portfolio_intermedio"


def cargar_datos():
    """Carga todos los datasets de 02_Intermedio a PostgreSQL."""

    print("=" * 80)
    print("CARGANDO DATOS A POSTGRESQL - NIVEL INTERMEDIO (PORTFOLIO DATA ANALYST)")
    print("=" * 80)

    try:
        # Crear conexión (UTF-8 por defecto)
        engine = create_engine(
            DATABASE_URL,
            connect_args={"client_encoding": "utf8"},
            pool_pre_ping=True,
        )
        print("\n[OK] Conexión a PostgreSQL establecida")

        base_path = Path(__file__).parent.parent / "data"

        # ============================================================
        # 1. E-COMMERCE: customers, orders, order_items, products
        # ============================================================
        ecommerce_path = base_path / "ecommerce"
        print("\n[1] Cargando datos de E-COMMERCE desde:", ecommerce_path)

        # customers
        df_customers = pd.read_csv(ecommerce_path / "customers.csv")
        df_customers.to_sql("ecom_customers", engine, if_exists="replace", index=False)
        print(f"   [OK] ecom_customers -> {len(df_customers)} registros")

        # orders
        df_orders = pd.read_csv(ecommerce_path / "orders.csv")
        # Intentar convertir columnas de fecha si existen
        for col in df_orders.columns:
            if "date" in col.lower() or "fecha" in col.lower():
                try:
                    df_orders[col] = pd.to_datetime(df_orders[col])
                except Exception:
                    pass
        df_orders.to_sql("ecom_orders", engine, if_exists="replace", index=False)
        print(f"   [OK] ecom_orders -> {len(df_orders)} registros")

        # order_items
        df_order_items = pd.read_csv(ecommerce_path / "order_items.csv")
        df_order_items.to_sql(
            "ecom_order_items", engine, if_exists="replace", index=False
        )
        print(f"   [OK] ecom_order_items -> {len(df_order_items)} registros")

        # products
        df_products = pd.read_csv(ecommerce_path / "products.csv")
        df_products.to_sql(
            "ecom_products", engine, if_exists="replace", index=False
        )
        print(f"   [OK] ecom_products -> {len(df_products)} registros")

        # ============================================================
        # 2. MARKETING: marketing_analytics
        # ============================================================
        marketing_path = base_path / "marketing"
        print("\n[2] Cargando datos de MARKETING desde:", marketing_path)

        df_marketing = pd.read_csv(marketing_path / "marketing_analytics.csv")
        df_marketing.to_sql(
            "marketing_analytics", engine, if_exists="replace", index=False
        )
        print(f"   [OK] marketing_analytics -> {len(df_marketing)} registros")

        # ============================================================
        # 3. ONLINE RETAIL: online_retail
        # ============================================================
        online_path = base_path / "online_retail"
        print("\n[3] Cargando datos de ONLINE RETAIL desde:", online_path)

        # El archivo original suele ser Excel, aquí trabajamos con CSV ya generado
        df_online = pd.read_csv(online_path / "online_retail.csv")
        # Intentar convertir la columna de fecha si existe
        for col in df_online.columns:
            if "InvoiceDate".lower() in col.lower() or "date" in col.lower():
                try:
                    df_online[col] = pd.to_datetime(df_online[col])
                except Exception:
                    pass
        df_online.to_sql(
            "online_retail", engine, if_exists="replace", index=False
        )
        print(f"   [OK] online_retail -> {len(df_online)} registros")

        # ============================================================
        # 4. Verificación rápida en BD
        # ============================================================
        print("\n[4] Verificando tablas en PostgreSQL...")
        with engine.connect() as conn:
            tablas = [
                "ecom_customers",
                "ecom_orders",
                "ecom_order_items",
                "ecom_products",
                "marketing_analytics",
                "online_retail",
            ]
            for tabla in tablas:
                try:
                    res = conn.execute(text(f"SELECT COUNT(*) FROM {tabla}"))
                    count = res.scalar()
                    print(f"   - {tabla}: {count} registros")
                except Exception as e:
                    print(f"   [WARNING] No se pudo contar registros en {tabla}: {e}")

        print("\n" + "=" * 80)
        print("[EXITO] TODOS los datos de 02_Intermedio fueron cargados correctamente")
        print("=" * 80)
        print("\nPróximos pasos recomendados:")
        print("  1. Ejecutar consultas SQL: sql/performance_vendedores.sql")
        print("  2. Crear/usar notebooks de análisis (cohortes, RFM, ROI, etc.)")
        print("  3. Construir dashboards con Plotly/Dash o Excel")

        return True

    except Exception as e:
        print(f"\n[ERROR] Error al cargar datos: {e}")
        print("\nVerifica:")
        print("  1. Que PostgreSQL esté ejecutándose")
        print("  2. Que la base de datos 'portfolio_intermedio' exista")
        print("  3. Que la contraseña en DATABASE_URL sea correcta (actual: 123456)")
        return False


if __name__ == "__main__":
    cargar_datos()


