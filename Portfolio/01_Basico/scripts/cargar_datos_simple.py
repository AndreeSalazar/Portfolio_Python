"""
Cargar datos usando psycopg2 directamente - Solución robusta al problema de encoding
"""

import pandas as pd
import psycopg2
from psycopg2.extras import RealDictCursor
import sys
import io

# Configurar encoding para Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

print("=" * 70)
print("CARGANDO DATOS DESDE POSTGRESQL - SOLUCION ROBUSTA")
print("=" * 70)

# Conectar usando psycopg2 directamente con encoding explícito
print("\n[1] Conectando a PostgreSQL...")
try:
    # Usar psycopg2 directamente con encoding latin1
    conn = psycopg2.connect(
        host='localhost',
        database='retail_analysis_basico',
        user='postgres',
        password='123456',
        client_encoding='latin1'
    )
    print("   [OK] Conexion establecida")
    
    # Cargar datos usando cursor
    print("\n[2] Cargando datos...")
    
    # Ventas
    df_ventas = pd.read_sql("SELECT * FROM ventas", conn)
    print(f"   [OK] Ventas: {len(df_ventas)} registros")
    
    # Productos
    df_productos = pd.read_sql("SELECT * FROM productos", conn)
    print(f"   [OK] Productos: {len(df_productos)} registros")
    
    # Clientes
    df_clientes = pd.read_sql("SELECT * FROM clientes", conn)
    print(f"   [OK] Clientes: {len(df_clientes)} registros")
    
    # Convertir a UTF-8
    print("\n[3] Convirtiendo a UTF-8...")
    for col in df_ventas.select_dtypes(include=['object']).columns:
        df_ventas[col] = df_ventas[col].apply(
            lambda x: x.encode('latin1').decode('utf-8', errors='ignore') if isinstance(x, str) else x
        )
    
    for col in df_productos.select_dtypes(include=['object']).columns:
        df_productos[col] = df_productos[col].apply(
            lambda x: x.encode('latin1').decode('utf-8', errors='ignore') if isinstance(x, str) else x
        )
    
    for col in df_clientes.select_dtypes(include=['object']).columns:
        df_clientes[col] = df_clientes[col].apply(
            lambda x: x.encode('latin1').decode('utf-8', errors='ignore') if isinstance(x, str) else x
        )
    
    print("   [OK] Conversion completada")
    
    # Mostrar resumen
    print("\n" + "=" * 70)
    print("RESUMEN")
    print("=" * 70)
    print(f"Ventas: {len(df_ventas)} registros")
    print(f"Productos: {len(df_productos)} registros")
    print(f"Clientes: {len(df_clientes)} registros")
    print("\nPrimeras 3 filas de ventas:")
    print(df_ventas.head(3))
    
    conn.close()
    print("\n[EXITO] Datos cargados correctamente")
    
except Exception as e:
    print(f"\n[ERROR] Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

