"""
Ejemplos básicos de numpy para Data Analyst
"""

import numpy as np

print("=" * 50)
print("EJEMPLOS DE NUMPY")
print("=" * 50)

# ============================================
# 1. CREAR ARRAYS
# ============================================

# Array desde lista
arr1 = np.array([1, 2, 3, 4, 5])
print("\n1. Array desde lista:")
print(arr1)

# Array 2D
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2. Array 2D:")
print(arr2d)

# Arrays con funciones
zeros = np.zeros(5)
ones = np.ones((3, 3))
arange = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)

print("\n3. Arrays especiales:")
print(f"Zeros: {zeros}")
print(f"Ones:\n{ones}")
print(f"Arange: {arange}")
print(f"Linspace: {linspace}")

# ============================================
# 2. PROPIEDADES DE ARRAYS
# ============================================

print("\n4. Propiedades del array:")
print(f"Shape: {arr2d.shape}")
print(f"Size: {arr2d.size}")
print(f"Dimensiones: {arr2d.ndim}")
print(f"Tipo de datos: {arr2d.dtype}")

# ============================================
# 3. OPERACIONES MATEMÁTICAS
# ============================================

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print("\n5. Operaciones básicas:")
print(f"Suma: {a + b}")
print(f"Resta: {b - a}")
print(f"Multiplicación: {a * b}")
print(f"División: {b / a}")
print(f"Potencia: {a ** 2}")

# ============================================
# 4. FUNCIONES ESTADÍSTICAS
# ============================================

datos = np.array([23, 45, 67, 34, 56, 78, 12, 45, 67, 89])

print("\n6. Estadísticas:")
print(f"Media: {np.mean(datos)}")
print(f"Mediana: {np.median(datos)}")
print(f"Desviación estándar: {np.std(datos)}")
print(f"Varianza: {np.var(datos)}")
print(f"Mínimo: {np.min(datos)}")
print(f"Máximo: {np.max(datos)}")
print(f"Percentil 25: {np.percentile(datos, 25)}")
print(f"Percentil 75: {np.percentile(datos, 75)}")

# ============================================
# 5. OPERACIONES CON ARRAYS
# ============================================

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("\n7. Operaciones con arrays:")
print(f"Suma de todos los elementos: {np.sum(arr)}")
print(f"Suma por filas: {np.sum(arr, axis=1)}")
print(f"Suma por columnas: {np.sum(arr, axis=0)}")
print(f"Promedio: {np.mean(arr)}")
print(f"Promedio por filas: {np.mean(arr, axis=1)}")

# ============================================
# 6. INDEXACIÓN Y SLICING
# ============================================

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("\n8. Indexación:")
print(f"Primer elemento: {arr[0]}")
print(f"Último elemento: {arr[-1]}")
print(f"Elementos del 2 al 5: {arr[1:5]}")
print(f"Cada 2 elementos: {arr[::2]}")

# Indexación 2D
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nArray 2D:\n{arr2d}")
print(f"Elemento [1, 2]: {arr2d[1, 2]}")
print(f"Primera fila: {arr2d[0, :]}")
print(f"Primera columna: {arr2d[:, 0]}")

# ============================================
# 7. FILTRADO Y CONDICIONES
# ============================================

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("\n9. Filtrado:")
print(f"Elementos mayores a 5: {arr[arr > 5]}")
print(f"Elementos pares: {arr[arr % 2 == 0]}")
print(f"Elementos entre 3 y 7: {arr[(arr >= 3) & (arr <= 7)]}")

# ============================================
# 8. RESHAPE Y TRANSFORMACIONES
# ============================================

arr = np.arange(12)

print("\n10. Reshape:")
print(f"Array original: {arr}")
print(f"Reshape a 3x4:\n{arr.reshape(3, 4)}")
print(f"Flatten: {arr.reshape(3, 4).flatten()}")

# ============================================
# 9. GENERACIÓN DE DATOS ALEATORIOS
# ============================================

print("\n11. Datos aleatorios:")
print(f"Números aleatorios (0-1): {np.random.random(5)}")
print(f"Enteros aleatorios: {np.random.randint(1, 100, 5)}")
print(f"Distribución normal: {np.random.normal(0, 1, 5)}")

# ============================================
# 10. OPERACIONES AVANZADAS
# ============================================

arr = np.array([1, 2, 3, 4, 5])

print("\n12. Operaciones avanzadas:")
print(f"Suma acumulada: {np.cumsum(arr)}")
print(f"Producto acumulado: {np.cumprod(arr)}")
print(f"Diferencias: {np.diff(arr)}")

print("\n" + "=" * 50)
print("¡Ejemplos completados!")
print("=" * 50)

