"""
PROYECTO BÁSICO: Estadísticas Descriptivas
Portfolio Data Analyst - Nivel Básico

Objetivo: Demostrar cálculo de estadísticas básicas con pandas y numpy
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("ESTADÍSTICAS DESCRIPTIVAS - Nivel Básico")
print("=" * 60)

# ============================================
# 1. CREAR DATOS DE EJEMPLO
# ============================================

# Generar datos de ventas
np.random.seed(42)
datos = {
    'ventas': np.random.normal(1000, 200, 100),
    'cantidad': np.random.randint(1, 20, 100),
    'descuento': np.random.uniform(0, 0.3, 100)
}

df = pd.DataFrame(datos)

print("\n1. DATOS DE EJEMPLO")
print(df.head(10))

# ============================================
# 2. ESTADÍSTICAS BÁSICAS
# ============================================

print("\n2. ESTADÍSTICAS DESCRIPTIVAS")
print(df.describe())

# ============================================
# 3. CÁLCULOS INDIVIDUALES
# ============================================

print("\n3. ESTADÍSTICAS DE VENTAS")
print(f"Media: {df['ventas'].mean():.2f}")
print(f"Mediana: {df['ventas'].median():.2f}")
print(f"Moda: {df['ventas'].mode()[0]:.2f}")
print(f"Desviación estándar: {df['ventas'].std():.2f}")
print(f"Varianza: {df['ventas'].var():.2f}")
print(f"Mínimo: {df['ventas'].min():.2f}")
print(f"Máximo: {df['ventas'].max():.2f}")

# Percentiles
print(f"\nPercentiles:")
print(f"25%: {df['ventas'].quantile(0.25):.2f}")
print(f"50%: {df['ventas'].quantile(0.50):.2f}")
print(f"75%: {df['ventas'].quantile(0.75):.2f}")

# ============================================
# 4. VISUALIZACIONES BÁSICAS
# ============================================

# Configurar matplotlib
plt.style.use('default')
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Histograma
axes[0, 0].hist(df['ventas'], bins=20, edgecolor='black')
axes[0, 0].set_title('Distribución de Ventas')
axes[0, 0].set_xlabel('Ventas')
axes[0, 0].set_ylabel('Frecuencia')
axes[0, 0].axvline(df['ventas'].mean(), color='r', linestyle='--', label='Media')
axes[0, 0].legend()

# Box plot
axes[0, 1].boxplot(df['ventas'])
axes[0, 1].set_title('Box Plot de Ventas')
axes[0, 1].set_ylabel('Ventas')

# Gráfico de barras (cantidad)
axes[1, 0].bar(range(len(df['cantidad'].value_counts().head(10))), 
               df['cantidad'].value_counts().head(10).values)
axes[1, 0].set_title('Top 10 Cantidades más Frecuentes')
axes[1, 0].set_xlabel('Cantidad')
axes[1, 0].set_ylabel('Frecuencia')

# Gráfico de líneas (tendencia)
axes[1, 1].plot(df['ventas'].head(30))
axes[1, 1].set_title('Tendencia de Ventas (primeras 30)')
axes[1, 1].set_xlabel('Índice')
axes[1, 1].set_ylabel('Ventas')

plt.tight_layout()
plt.savefig('figures/estadisticas_basicas.png', dpi=300, bbox_inches='tight')
print("\n✅ Gráfico guardado en: figures/estadisticas_basicas.png")

# ============================================
# 5. RESUMEN
# ============================================

print("\n" + "=" * 60)
print("RESUMEN DEL ANÁLISIS")
print("=" * 60)
print(f"Total de registros: {len(df)}")
print(f"Rango de ventas: {df['ventas'].min():.2f} - {df['ventas'].max():.2f}")
print(f"Promedio de ventas: {df['ventas'].mean():.2f}")
print(f"Desviación estándar: {df['ventas'].std():.2f}")

print("\n✅ Análisis completado - Nivel Básico")
print("=" * 60)

