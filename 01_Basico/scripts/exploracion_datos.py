"""
Exploración básica de datos con pandas y numpy
Portfolio Data Analyst - Nivel Básico

Este script demuestra cómo explorar y analizar datos básicos
"""

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from pathlib import Path

# Configuración
DATABASE_URL = 'postgresql://postgres:123456@localhost:5432/retail_analysis_basico'

def explorar_datos():
    """Explora los datos cargados en PostgreSQL"""
    
    print("=" * 70)
    print("EXPLORACION DE DATOS CON PANDAS Y NUMPY")
    print("=" * 70)
    
    try:
        # Conectar a PostgreSQL con encoding UTF-8
        engine = create_engine(
            DATABASE_URL,
            connect_args={
                'client_encoding': 'utf8'
            },
            pool_pre_ping=True
        )
        
        # 1. Cargar datos
        print("\n[1] Cargando datos desde PostgreSQL...")
        df_ventas = pd.read_sql("SELECT * FROM ventas", engine)
        df_productos = pd.read_sql("SELECT * FROM productos", engine)
        df_clientes = pd.read_sql("SELECT * FROM clientes", engine)
        
        print(f"   [OK] Ventas: {len(df_ventas)} registros")
        print(f"   [OK] Productos: {len(df_productos)} registros")
        print(f"   [OK] Clientes: {len(df_clientes)} registros")
        
        # 2. Información básica de ventas
        print("\n[2] INFORMACION BASICA - VENTAS")
        print("-" * 70)
        print(f"Shape: {df_ventas.shape} (filas, columnas)")
        print(f"\nColumnas: {list(df_ventas.columns)}")
        print(f"\nTipos de datos:")
        print(df_ventas.dtypes)
        
        # 3. Primeras y últimas filas
        print("\n[3] PRIMERAS 5 FILAS")
        print("-" * 70)
        print(df_ventas.head())
        
        print("\n[4] ULTIMAS 5 FILAS")
        print("-" * 70)
        print(df_ventas.tail())
        
        # 4. Estadísticas descriptivas
        print("\n[5] ESTADISTICAS DESCRIPTIVAS")
        print("-" * 70)
        print(df_ventas.describe())
        
        # 5. Valores únicos
        print("\n[6] VALORES UNICOS")
        print("-" * 70)
        print(f"Regiones: {df_ventas['region'].unique()}")
        print(f"Productos: {df_ventas['producto'].unique()}")
        print(f"Vendedores únicos: {df_ventas['vendedor'].nunique()}")
        print(f"Clientes únicos: {df_ventas['cliente_id'].nunique()}")
        
        # 6. Valores faltantes
        print("\n[7] VALORES FALTANTES")
        print("-" * 70)
        valores_faltantes = df_ventas.isna().sum()
        if valores_faltantes.sum() > 0:
            print(valores_faltantes[valores_faltantes > 0])
        else:
            print("   [OK] No hay valores faltantes")
        
        # 7. Estadísticas con numpy
        print("\n[8] ESTADISTICAS CON NUMPY")
        print("-" * 70)
        ventas_array = df_ventas['total'].values
        print(f"Media: {np.mean(ventas_array):.2f}")
        print(f"Mediana: {np.median(ventas_array):.2f}")
        print(f"Desviación estándar: {np.std(ventas_array):.2f}")
        print(f"Varianza: {np.var(ventas_array):.2f}")
        print(f"Mínimo: {np.min(ventas_array):.2f}")
        print(f"Máximo: {np.max(ventas_array):.2f}")
        print(f"Percentil 25: {np.percentile(ventas_array, 25):.2f}")
        print(f"Percentil 75: {np.percentile(ventas_array, 75):.2f}")
        
        # 8. Agrupaciones básicas
        print("\n[9] VENTAS POR REGION")
        print("-" * 70)
        ventas_region = df_ventas.groupby('region').agg({
            'total': ['sum', 'mean', 'count']
        }).round(2)
        ventas_region.columns = ['Total_Ventas', 'Promedio_Venta', 'Num_Ventas']
        print(ventas_region)
        
        print("\n[10] VENTAS POR PRODUCTO")
        print("-" * 70)
        ventas_producto = df_ventas.groupby('producto').agg({
            'cantidad': 'sum',
            'total': 'sum',
            'precio_unitario': 'mean'
        }).sort_values('total', ascending=False)
        ventas_producto.columns = ['Unidades_Vendidas', 'Ingresos_Totales', 'Precio_Promedio']
        print(ventas_producto.round(2))
        
        # 9. Análisis temporal
        print("\n[11] ANALISIS TEMPORAL")
        print("-" * 70)
        df_ventas['mes'] = pd.to_datetime(df_ventas['fecha']).dt.to_period('M')
        ventas_mensuales = df_ventas.groupby('mes').agg({
            'total': ['sum', 'mean', 'count']
        }).round(2)
        ventas_mensuales.columns = ['Total_Mes', 'Promedio_Mes', 'Num_Ventas']
        print(ventas_mensuales)
        
        # 10. Resumen final
        print("\n" + "=" * 70)
        print("RESUMEN FINAL")
        print("=" * 70)
        print(f"Total de ventas: {len(df_ventas):,}")
        print(f"Ingresos totales: {df_ventas['total'].sum():,.2f} €")
        print(f"Ticket promedio: {df_ventas['total'].mean():.2f} €")
        print(f"Región con más ventas: {df_ventas.groupby('region')['total'].sum().idxmax()}")
        print(f"Producto más vendido: {df_ventas.groupby('producto')['cantidad'].sum().idxmax()}")
        
        print("\n[EXITO] Exploración completada")
        print("=" * 70)
        
        return df_ventas, df_productos, df_clientes
        
    except Exception as e:
        print(f"\n[ERROR] Error al explorar datos: {e}")
        print("\nVerifica:")
        print("  1. Que los datos estén cargados en PostgreSQL")
        print("  2. Que la conexión sea correcta")
        return None, None, None


if __name__ == "__main__":
    explorar_datos()

