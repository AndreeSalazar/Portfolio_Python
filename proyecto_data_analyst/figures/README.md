# 📈 Figures - Gráficos y Visualizaciones

Esta carpeta contiene todas las visualizaciones y gráficos generados en tus análisis.

## 📊 Tipos de Archivos

- **PNG**: Para presentaciones y documentos
- **PDF**: Para publicaciones de alta calidad
- **SVG**: Para escalabilidad perfecta
- **HTML**: Para dashboards interactivos

## 🚀 Generar Gráficos

### Desde Python/pandas
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Crear gráfico
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='categoria', y='ventas')
plt.title('Ventas por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Ventas')

# Guardar
plt.savefig('figures/ventas_por_categoria.png', dpi=300, bbox_inches='tight')
plt.show()
```

### Desde Jupyter Notebooks
```python
# En tu notebook
import matplotlib.pyplot as plt

# Tu código de gráfico
fig, ax = plt.subplots(figsize=(10, 6))
# ... código del gráfico ...

# Guardar
plt.savefig('../figures/mi_analisis.png', dpi=300, bbox_inches='tight')
```

### Con plotly (interactivos)
```python
import plotly.express as px

fig = px.bar(df, x='categoria', y='ventas')
fig.write_html('figures/ventas_interactivo.html')
```

## 📁 Organización

Organiza tus gráficos por análisis:
```
figures/
├── exploracion/      # Gráficos exploratorios
├── analisis/         # Gráficos de análisis
├── presentacion/     # Gráficos para presentar
└── dashboards/       # Dashboards completos
```

## 💡 Mejores Prácticas

### Nombres Descriptivos
- ✅ `ventas_mensuales_2024.png`
- ❌ `grafico1.png`

### Resolución
- **Presentaciones**: 300 DPI
- **Web**: 150-200 DPI
- **Publicaciones**: 600 DPI

### Formatos
- **PNG**: Para la mayoría de casos
- **PDF**: Para documentos profesionales
- **SVG**: Para escalabilidad
- **HTML**: Para interactividad

### Tamaños Estándar
```python
# Presentación
plt.figure(figsize=(10, 6))

# Dashboard
plt.figure(figsize=(16, 9))

# Publicación
plt.figure(figsize=(8, 6))
```

## 📚 Librerías Recomendadas

- **matplotlib**: Gráficos básicos
- **seaborn**: Gráficos estadísticos bonitos
- **plotly**: Gráficos interactivos
- **pandas**: `.plot()` para gráficos rápidos

## ✅ Checklist

- [ ] Gráficos guardados con nombres descriptivos
- [ ] Resolución adecuada (300 DPI mínimo)
- [ ] Formato apropiado para el uso
- [ ] Organizados por análisis/proyecto

---

**¡Visualiza tus datos de forma impactante!** 📊✨

