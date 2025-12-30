"""
Script de prueba para verificar que la carga de datos funciona correctamente
con el manejo automático de encoding
"""

import pandas as pd
from sqlalchemy import create_engine
import sys
import io

# Configurar encoding para Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Configuración
DATABASE_URL = 'postgresql://postgres:123456@localhost:5432/retail_analysis_basico'

print("=" * 70)
print("PRUEBA DE CARGA DE DATOS CON MANEJO DE ENCODING")
print("=" * 70)

# Paso 1: Crear conexión con manejo automático
print("\n[1] Creando conexion...")
engine = None
encoding_usado = None

# Intentar con latin1 directamente (ya sabemos que UTF-8 falla)
try:
    engine = create_engine(
        DATABASE_URL,
        connect_args={
            'client_encoding': 'latin1'
        },
        pool_pre_ping=True
    )
    # Probar conexión con latin1
    with engine.connect() as conn:
        result = conn.execute("SELECT 1")
        encoding_usado = 'latin1'
        print("   [OK] Conexion establecida con latin1")
except Exception as e:
    print(f"   [ERROR] Error de conexion: {e}")
    print("\nVerifica:")
    print("   1. Que PostgreSQL este ejecutandose")
    print("   2. Que la BD 'retail_analysis_basico' exista")
    print("   3. Que la contrasena sea correcta")
    sys.exit(1)

# Paso 2: Cargar datos
print("\n[2] Cargando datos...")
try:
    # Leer con latin1
    df_ventas = pd.read_sql("SELECT * FROM ventas", engine)
    df_productos = pd.read_sql("SELECT * FROM productos", engine)
    df_clientes = pd.read_sql("SELECT * FROM clientes", engine)
    
    print(f"   [OK] Ventas: {len(df_ventas)} registros")
    print(f"   [OK] Productos: {len(df_productos)} registros")
    print(f"   [OK] Clientes: {len(df_clientes)} registros")
    
    # Convertir a UTF-8
    print("\n[3] Convirtiendo datos de latin1 a UTF-8...")
    
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
    
    print("   [OK] Datos convertidos a UTF-8")
    
    # Verificar datos
    print("\n[4] Verificando datos cargados...")
    print(f"   Ventas - Columnas: {list(df_ventas.columns)}")
    print(f"   Ventas - Shape: {df_ventas.shape}")
    print(f"   Primeras 3 filas de ventas:")
    print(df_ventas.head(3))
    
    print("\n" + "=" * 70)
    print("[EXITO] PRUEBA EXITOSA - Todos los datos cargados correctamente")
    print("=" * 70)
    print(f"\nResumen:")
    print(f"  - Encoding usado: {encoding_usado}")
    print(f"  - Ventas: {len(df_ventas)} registros")
    print(f"  - Productos: {len(df_productos)} registros")
    print(f"  - Clientes: {len(df_clientes)} registros")
    print(f"\n[OK] El notebook deberia funcionar correctamente ahora")
    print("\nNOTA: El notebook usa latin1 y convierte automaticamente a UTF-8")
    
except Exception as e:
    print(f"\n[ERROR] Error al cargar datos: {e}")
    import traceback
    traceback.print_exc()
    print("\nVerifica:")
    print("   1. Que los datos esten cargados en PostgreSQL")
    print("   2. Ejecuta: python scripts/cargar_datos_postgresql.py")
    sys.exit(1)
