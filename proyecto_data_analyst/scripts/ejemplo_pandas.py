"""
Ejemplos básicos de pandas para Data Analyst
"""

import pandas as pd
import numpy as np

print("=" * 50)
print("EJEMPLOS DE PANDAS")
print("=" * 50)

# ============================================
# 1. CREAR DATAFRAMES
# ============================================

# Crear DataFrame desde diccionario
data = {
    'nombre': ['Juan', 'María', 'Carlos', 'Ana'],
    'edad': [25, 30, 35, 28],
    'ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla'],
    'salario': [3000, 3500, 4000, 3200]
}

df = pd.DataFrame(data)
print("\n1. DataFrame creado:")
print(df)

# ============================================
# 2. LECTURA DE DATOS
# ============================================

# Leer CSV
# df_csv = pd.read_csv('../data/ejemplo.csv')

# Leer Excel
# df_excel = pd.read_excel('../data/ejemplo.xlsx', sheet_name='Hoja1')

print("\n2. Información del DataFrame:")
print(df.info())

print("\n3. Estadísticas descriptivas:")
print(df.describe())

# ============================================
# 3. EXPLORACIÓN DE DATOS
# ============================================

print("\n4. Primeras 3 filas:")
print(df.head(3))

print("\n5. Últimas 2 filas:")
print(df.tail(2))

print("\n6. Forma del DataFrame (filas, columnas):")
print(df.shape)

print("\n7. Columnas:")
print(df.columns.tolist())

# ============================================
# 4. SELECCIÓN Y FILTRADO
# ============================================

print("\n8. Seleccionar columnas:")
print(df[['nombre', 'edad']])

print("\n9. Filtrar por condición:")
print(df[df['edad'] > 28])

print("\n10. Filtrar con múltiples condiciones:")
print(df[(df['edad'] > 28) & (df['salario'] > 3200)])

# ============================================
# 5. OPERACIONES
# ============================================

print("\n11. Agregar nueva columna:")
df['salario_anual'] = df['salario'] * 12
print(df[['nombre', 'salario', 'salario_anual']])

print("\n12. Estadísticas por grupo:")
print(df.groupby('ciudad')['salario'].mean())

print("\n13. Agregaciones múltiples:")
print(df.groupby('ciudad').agg({
    'salario': ['mean', 'sum', 'count'],
    'edad': 'mean'
}))

# ============================================
# 6. VALORES FALTANTES
# ============================================

# Crear DataFrame con valores faltantes
df_nan = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, np.nan]
})

print("\n14. DataFrame con valores faltantes:")
print(df_nan)

print("\n15. Verificar valores faltantes:")
print(df_nan.isna().sum())

print("\n16. Eliminar filas con NaN:")
print(df_nan.dropna())

print("\n17. Llenar NaN con valor:")
print(df_nan.fillna(0))

# ============================================
# 7. ORDENAR Y RANKING
# ============================================

print("\n18. Ordenar por columna:")
print(df.sort_values('salario', ascending=False))

print("\n19. Top 2 por salario:")
print(df.nlargest(2, 'salario'))

# ============================================
# 8. COMBINAR DATAFRAMES
# ============================================

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'nombre': ['A', 'B', 'C']
})

df2 = pd.DataFrame({
    'id': [2, 3, 4],
    'valor': [100, 200, 300]
})

print("\n20. Merge (JOIN):")
resultado = pd.merge(df1, df2, on='id', how='inner')
print(resultado)

# ============================================
# 9. EXPORTAR DATOS
# ============================================

# Exportar a CSV
# df.to_csv('../data/resultado.csv', index=False)

# Exportar a Excel
# df.to_excel('../data/resultado.xlsx', index=False)

print("\n" + "=" * 50)
print("¡Ejemplos completados!")
print("=" * 50)

