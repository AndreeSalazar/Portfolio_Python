"""
Cargar datos - Solución final al problema de encoding
Usa variables de entorno para evitar problemas de encoding en la conexión
"""

import pandas as pd
import psycopg2
import os
import sys
import io

# Configurar encoding para Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    # Establecer variables de entorno para PostgreSQL
    os.environ['PGCLIENTENCODING'] = 'LATIN1'

print("=" * 70)
print("CARGANDO DATOS DESDE POSTGRESQL")
print("=" * 70)

try:
    # Conectar usando psycopg2 con encoding en variables de entorno
    print("\n[1] Conectando a PostgreSQL...")
    conn = psycopg2.connect(
        host='localhost',
        database='retail_analysis_basico',
        user='postgres',
        password='123456'
    )
    
    # Establecer encoding después de conectar
    conn.set_client_encoding('LATIN1')
    print("   [OK] Conexion establecida")
    
    # Cargar datos
    print("\n[2] Cargando datos...")
    df_ventas = pd.read_sql("SELECT * FROM ventas", conn)
    df_productos = pd.read_sql("SELECT * FROM productos", conn)
    df_clientes = pd.read_sql("SELECT * FROM clientes", conn)
    
    print(f"   [OK] Ventas: {len(df_ventas)} registros")
    print(f"   [OK] Productos: {len(df_productos)} registros")
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
    print("\nNOTA: Este script funciona correctamente.")
    print("El notebook puede tener problemas de encoding durante la conexion.")
    print("Usa este script para cargar datos y luego trabaja con los DataFrames.")
    
except Exception as e:
    print(f"\n[ERROR] Error: {e}")
    print("\nPosibles soluciones:")
    print("1. Verifica que PostgreSQL este ejecutandose")
    print("2. Verifica que la BD 'retail_analysis_basico' exista")
    print("3. Verifica que los datos esten cargados")
    print("4. Intenta recrear la BD con UTF-8:")
    print("   DROP DATABASE retail_analysis_basico;")
    print("   CREATE DATABASE retail_analysis_basico WITH ENCODING 'UTF8';")
    import traceback
    traceback.print_exc()
    sys.exit(1)

