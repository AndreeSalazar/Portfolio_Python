"""
Conectar Python con PostgreSQL usando pandas
"""

import pandas as pd
import psycopg2
from sqlalchemy import create_engine

print("=" * 50)
print("CONECTAR PYTHON CON POSTGRESQL")
print("=" * 50)

# ============================================
# CONFIGURACIÓN DE CONEXIÓN
# ============================================

# Ajusta estos valores según tu configuración
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'practica_data_analyst',  # Cambia por tu base de datos
    'user': 'postgres',
    'password': 'TU_CONTRASEÑA_AQUI'  # ⚠️ Cambia esto
}

# ============================================
# MÉTODO 1: Usando psycopg2 + pandas
# ============================================

def conectar_psycopg2():
    """Conectar usando psycopg2"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("\n✅ Conexión exitosa con psycopg2")
        
        # Ejecutar consulta y obtener DataFrame
        query = "SELECT * FROM productos LIMIT 5;"
        df = pd.read_sql_query(query, conn)
        
        print("\nProductos (primeros 5):")
        print(df)
        
        conn.close()
        return df
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return None

# ============================================
# MÉTODO 2: Usando SQLAlchemy (recomendado)
# ============================================

def conectar_sqlalchemy():
    """Conectar usando SQLAlchemy (más fácil con pandas)"""
    try:
        # Crear string de conexión
        connection_string = (
            f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
            f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        )
        
        # Crear engine
        engine = create_engine(connection_string)
        
        print("\n✅ Conexión exitosa con SQLAlchemy")
        
        # Leer datos directamente a DataFrame
        query = "SELECT * FROM ventas LIMIT 10;"
        df = pd.read_sql(query, engine)
        
        print("\nVentas (primeras 10):")
        print(df)
        
        return df, engine
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return None, None

# ============================================
# FUNCIONES ÚTILES
# ============================================

def leer_tabla_completa(tabla, engine):
    """Leer una tabla completa"""
    try:
        df = pd.read_sql(f"SELECT * FROM {tabla};", engine)
        print(f"\n✅ Tabla '{tabla}' leída: {len(df)} registros")
        return df
    except Exception as e:
        print(f"\n❌ Error leyendo tabla {tabla}: {e}")
        return None

def ejecutar_consulta(query, engine):
    """Ejecutar consulta SQL y obtener DataFrame"""
    try:
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        print(f"\n❌ Error ejecutando consulta: {e}")
        return None

def escribir_a_postgresql(df, tabla, engine, if_exists='replace'):
    """Escribir DataFrame a tabla de PostgreSQL"""
    try:
        df.to_sql(tabla, engine, if_exists=if_exists, index=False)
        print(f"\n✅ DataFrame escrito en tabla '{tabla}'")
    except Exception as e:
        print(f"\n❌ Error escribiendo a PostgreSQL: {e}")

# ============================================
# EJEMPLO DE USO
# ============================================

if __name__ == "__main__":
    print("\n⚠️  IMPORTANTE: Actualiza DB_CONFIG con tus credenciales")
    print("\nPara usar este script:")
    print("1. Instala: pip install psycopg2-binary sqlalchemy pandas")
    print("2. Actualiza DB_CONFIG con tu contraseña")
    print("3. Asegúrate de que la base de datos existe")
    print("\n" + "=" * 50)
    
    # Descomenta para probar:
    # df, engine = conectar_sqlalchemy()
    # 
    # if engine:
    #     # Leer tabla completa
    #     productos = leer_tabla_completa('productos', engine)
    #     
    #     # Ejecutar consulta personalizada
    #     query = """
    #         SELECT 
    #             p.nombre,
    #             SUM(v.total) as total_ventas
    #         FROM ventas v
    #         JOIN productos p ON v.producto_id = p.id
    #         GROUP BY p.nombre
    #         ORDER BY total_ventas DESC;
    #     """
    #     resultado = ejecutar_consulta(query, engine)
    #     print("\nVentas por producto:")
    #     print(resultado)

