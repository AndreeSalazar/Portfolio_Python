"""
PROYECTO BÁSICO: Limpieza de Datos
Portfolio Data Analyst - Nivel Básico

Objetivo: Demostrar proceso de limpieza de datos con valores faltantes
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("LIMPIEZA DE DATOS - Nivel Básico")
print("=" * 60)

# ============================================
# 1. CREAR DATOS CON VALORES FALTANTES
# ============================================

# Simular datos con problemas comunes
np.random.seed(42)
datos = {
    'id': range(1, 101),
    'nombre': [f'Cliente_{i}' for i in range(1, 101)],
    'edad': np.random.choice([20, 25, 30, 35, 40, None], 100, p=[0.15, 0.15, 0.15, 0.15, 0.15, 0.25]),
    'salario': np.random.normal(3000, 1000, 100),
    'ciudad': np.random.choice(['Madrid', 'Barcelona', 'Valencia', None], 100, p=[0.4, 0.3, 0.2, 0.1])
}

df = pd.DataFrame(datos)

# Introducir algunos valores faltantes adicionales
df.loc[df.sample(frac=0.1).index, 'salario'] = np.nan
df.loc[df.sample(frac=0.05).index, 'nombre'] = None

print("\n1. DATOS ORIGINALES")
print(f"Filas: {len(df)}")
print(f"Columnas: {len(df.columns)}")
print("\nPrimeras 10 filas:")
print(df.head(10))

# ============================================
# 2. EXPLORACIÓN DE VALORES FALTANTES
# ============================================

print("\n2. ANÁLISIS DE VALORES FALTANTES")
print("\nValores faltantes por columna:")
valores_faltantes = df.isna().sum()
print(valores_faltantes)

print("\nPorcentaje de valores faltantes:")
porcentaje = (valores_faltantes / len(df)) * 100
print(porcentaje)

# ============================================
# 3. ESTRATEGIAS DE LIMPIEZA
# ============================================

print("\n3. PROCESO DE LIMPIEZA")

# Opción 1: Eliminar filas con valores faltantes
df_limpio_1 = df.dropna()
print(f"\nOpción 1 - Eliminar todas las filas con NaN:")
print(f"Filas originales: {len(df)}")
print(f"Filas después de dropna(): {len(df_limpio_1)}")
print(f"Filas eliminadas: {len(df) - len(df_limpio_1)}")

# Opción 2: Llenar con valores específicos
df_limpio_2 = df.copy()
df_limpio_2['edad'].fillna(df_limpio_2['edad'].median(), inplace=True)
df_limpio_2['salario'].fillna(df_limpio_2['salario'].mean(), inplace=True)
df_limpio_2['ciudad'].fillna('Desconocida', inplace=True)
df_limpio_2['nombre'].fillna('Sin nombre', inplace=True)

print(f"\nOpción 2 - Llenar con valores:")
print(f"Valores faltantes después de fillna():")
print(df_limpio_2.isna().sum())

# Opción 3: Eliminar solo columnas con muchos faltantes
df_limpio_3 = df.dropna(axis=1, thresh=len(df)*0.5)
print(f"\nOpción 3 - Eliminar columnas con >50% faltantes:")
print(f"Columnas originales: {len(df.columns)}")
print(f"Columnas después: {len(df_limpio_3.columns)}")

# ============================================
# 4. VALIDACIÓN DE DATOS
# ============================================

print("\n4. VALIDACIÓN DE DATOS LIMPIOS")

# Validar rangos
df_validado = df_limpio_2.copy()

# Validar edad (18-100)
df_validado = df_validado[(df_validado['edad'] >= 18) & (df_validado['edad'] <= 100)]

# Validar salario (positivo)
df_validado = df_validado[df_validado['salario'] > 0]

print(f"Filas después de validación: {len(df_validado)}")
print(f"Filas eliminadas por validación: {len(df_limpio_2) - len(df_validado)}")

# ============================================
# 5. RESULTADO FINAL
# ============================================

print("\n5. DATOS LIMPIOS Y VALIDADOS")
print(df_validado.head(10))
print(f"\nResumen final:")
print(f"Filas: {len(df_validado)}")
print(f"Valores faltantes: {df_validado.isna().sum().sum()}")

print("\n✅ Limpieza completada - Nivel Básico")
print("=" * 60)

