"""
Ejecutar carga de datos - Equivalente a la celda del notebook
"""

import pandas as pd
from sqlalchemy import create_engine
import sys
import io

# Configurar encoding para Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Configuración (usar el mismo engine que se creó en el notebook)
DATABASE_URL = 'postgresql://postgres:123456@localhost:5432/retail_analysis_basico'

print("=" * 70)
print("CARGANDO DATOS DESDE POSTGRESQL")
print("=" * 70)

# Crear engine con latin1 (ya sabemos que UTF-8 falla)
print("\n[1] Creando conexion con latin1...")
engine = create_engine(
    DATABASE_URL,
    connect_args={
        'client_encoding': 'latin1'
    },
    pool_pre_ping=True
)
print("   [OK] Conexion establecida")

# Cargar todas las tablas con manejo de encoding
print("\n[2] Cargando datos...")
try:
    # Leer datos con latin1
    df_ventas = pd.read_sql("SELECT * FROM ventas", engine)
    df_productos = pd.read_sql("SELECT * FROM productos", engine)
    df_clientes = pd.read_sql("SELECT * FROM clientes", engine)
    
    print(f"   [OK] Ventas: {len(df_ventas)} registros")
    print(f"   [OK] Productos: {len(df_productos)} registros")
    print(f"   [OK] Clientes: {len(df_clientes)} registros")
    
except UnicodeDecodeError as e:
    print(f"   [WARNING] Error de encoding al leer datos: {e}")
    print("   Convirtiendo datos de latin1 a UTF-8...")
    
    # Leer datos usando conexión directa
    with engine.connect() as conn:
        result_ventas = conn.execute("SELECT * FROM ventas")
        result_productos = conn.execute("SELECT * FROM productos")
        result_clientes = conn.execute("SELECT * FROM clientes")
        
        # Convertir a DataFrames
        df_ventas = pd.DataFrame(result_ventas.fetchall(), columns=result_ventas.keys())
        df_productos = pd.DataFrame(result_productos.fetchall(), columns=result_productos.keys())
        df_clientes = pd.DataFrame(result_clientes.fetchall(), columns=result_clientes.keys())
    
    # Convertir columnas de texto de latin1 a UTF-8
    print("   Convirtiendo columnas de texto...")
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
    
    print(f"   [OK] Ventas: {len(df_ventas)} registros (convertidos a UTF-8)")
    print(f"   [OK] Productos: {len(df_productos)} registros (convertidos a UTF-8)")
    print(f"   [OK] Clientes: {len(df_clientes)} registros (convertidos a UTF-8)")
    
except Exception as e:
    print(f"   [ERROR] Error al cargar datos: {e}")
    import traceback
    traceback.print_exc()
    print("\nVerifica:")
    print("   1. Que los datos esten cargados en PostgreSQL")
    print("   2. Ejecuta: python scripts/cargar_datos_postgresql.py")
    sys.exit(1)

# Mostrar resumen
print("\n" + "=" * 70)
print("RESUMEN DE DATOS CARGADOS")
print("=" * 70)
print(f"\nVentas:")
print(f"  - Registros: {len(df_ventas)}")
print(f"  - Columnas: {list(df_ventas.columns)}")
print(f"  - Shape: {df_ventas.shape}")
print(f"\nPrimeras 3 filas:")
print(df_ventas.head(3))

print(f"\nProductos:")
print(f"  - Registros: {len(df_productos)}")
print(f"  - Columnas: {list(df_productos.columns)}")

print(f"\nClientes:")
print(f"  - Registros: {len(df_clientes)}")
print(f"  - Columnas: {list(df_clientes.columns)}")

print("\n" + "=" * 70)
print("[EXITO] Datos cargados correctamente")
print("=" * 70)
print("\nLos DataFrames estan listos para usar:")
print("  - df_ventas")
print("  - df_productos")
print("  - df_clientes")

