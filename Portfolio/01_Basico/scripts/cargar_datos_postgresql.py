"""
Script para cargar datos CSV a PostgreSQL
Portfolio Data Analyst - Nivel Básico

Este script carga los datos de retail_sales a PostgreSQL
"""

import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
import sys

# Configuración de conexión
# IMPORTANTE: Cambiar 'password' por tu contraseña de PostgreSQL
DATABASE_URL = 'postgresql://postgres:123456@localhost:5432/retail_analysis_basico'

def cargar_datos():
    """Carga todos los datos CSV a PostgreSQL"""
    
    print("=" * 70)
    print("CARGANDO DATOS A POSTGRESQL - NIVEL BASICO")
    print("=" * 70)
    
    try:
        # Crear conexión con encoding UTF-8 para evitar errores UnicodeDecodeError
        engine = create_engine(
            DATABASE_URL,
            connect_args={
                'client_encoding': 'utf8'
            },
            pool_pre_ping=True
        )
        print("\n[OK] Conexión a PostgreSQL establecida con encoding UTF-8")
        
        # Obtener ruta base
        base_path = Path(__file__).parent.parent / 'data' / 'retail_sales'
        
        # 1. Cargar productos
        print("\n[1] Cargando productos...")
        df_productos = pd.read_csv(base_path / 'productos.csv')
        # Ajustar nombres de columnas
        df_productos.columns = ['producto_id', 'nombre', 'categoria', 'precio']
        df_productos.to_sql('productos', engine, if_exists='replace', index=False)
        print(f"   [OK] {len(df_productos)} productos cargados")
        print(f"   Columnas: {list(df_productos.columns)}")
        
        # 2. Cargar clientes
        print("\n[2] Cargando clientes...")
        df_clientes = pd.read_csv(base_path / 'clientes.csv')
        df_clientes.to_sql('clientes', engine, if_exists='replace', index=False)
        print(f"   [OK] {len(df_clientes)} clientes cargados")
        print(f"   Columnas: {list(df_clientes.columns)}")
        
        # 3. Cargar ventas
        print("\n[3] Cargando ventas...")
        df_ventas = pd.read_csv(base_path / 'ventas.csv')
        # Convertir fecha a formato datetime
        df_ventas['fecha'] = pd.to_datetime(df_ventas['fecha'])
        df_ventas.to_sql('ventas', engine, if_exists='replace', index=False)
        print(f"   [OK] {len(df_ventas)} ventas cargadas")
        print(f"   Columnas: {list(df_ventas.columns)}")
        print(f"   Rango de fechas: {df_ventas['fecha'].min()} a {df_ventas['fecha'].max()}")
        
        # Verificar carga
        print("\n[4] Verificando datos cargados...")
        from sqlalchemy import text
        with engine.connect() as conn:
            result = conn.execute(text("SELECT COUNT(*) FROM productos"))
            productos_count = result.scalar()
            result = conn.execute(text("SELECT COUNT(*) FROM clientes"))
            clientes_count = result.scalar()
            result = conn.execute(text("SELECT COUNT(*) FROM ventas"))
            ventas_count = result.scalar()
            
            print(f"   Productos en BD: {productos_count}")
            print(f"   Clientes en BD: {clientes_count}")
            print(f"   Ventas en BD: {ventas_count}")
        
        print("\n" + "=" * 70)
        print("[EXITO] Todos los datos cargados correctamente")
        print("=" * 70)
        print("\nPróximos pasos:")
        print("  1. Ejecutar consultas SQL: sql/consultas_ventas.sql")
        print("  2. Análisis con Python: scripts/exploracion_datos.py")
        print("  3. Crear notebook: notebooks/analisis_completo_basico.ipynb")
        
        return True
        
    except Exception as e:
        print(f"\n[ERROR] Error al cargar datos: {e}")
        print("\nVerifica:")
        print("  1. Que PostgreSQL esté ejecutándose")
        print("  2. Que la base de datos 'retail_analysis_basico' exista")
        print("  3. Que la contraseña en DATABASE_URL sea correcta")
        return False


if __name__ == "__main__":
    cargar_datos()

