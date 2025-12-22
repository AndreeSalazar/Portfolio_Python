# 📊 Datasets - Nivel Básico

Esta carpeta contiene los datasets descargados para proyectos de nivel básico.

## 📦 Datasets Incluidos

### 1. Retail Sales Dataset
**Fuente**: Kaggle  
**ID**: `rohitsahoo/sales-forecasting`  
**Carpeta**: `retail_sales/`

**Descripción**:
- Datos de ventas retail reales
- Múltiples dimensiones (tiempo, producto, región, cliente)
- Tamaño: ~50K-100K registros
- Perfecto para análisis básico e intermedio

**Estructura esperada**:
- `ventas.csv`: fecha, producto_id, cantidad, total, región
- `productos.csv`: producto_id, nombre, categoría, precio
- `clientes.csv`: cliente_id, nombre, ciudad, segmento

**Uso en proyectos**:
- Análisis de ventas por región/mes
- Performance de productos
- Análisis de tendencias temporales
- Segmentación de clientes

---

### 2. Superstore Sales Dataset
**Fuente**: Kaggle  
**ID**: `vivek468/superstore-dataset-final`  
**Carpeta**: `superstore/`

**Descripción**:
- Dataset muy popular de supermercado/retail
- Múltiples dimensiones
- Perfecto para dashboards

**Estructura esperada**:
- `Superstore.xlsx` o `Superstore.csv`
- Columnas: Order ID, Order Date, Ship Date, Customer Name, Segment, Country, City, State, Region, Product ID, Category, Sub-Category, Product Name, Sales, Quantity, Discount, Profit

**Uso en proyectos**:
- Dashboard completo de ventas
- Análisis de profitabilidad
- Segmentación de productos
- Análisis de tendencias

---

### 3. HR Analytics Dataset
**Fuente**: Kaggle  
**ID**: `arindam235/startup-investments-crunchbase`  
**Carpeta**: `hr_analytics/`

**Descripción**:
- Datos de recursos humanos
- Análisis de empleados y performance
- Tamaño: ~15K registros
- Perfecto para análisis de negocio

**Estructura esperada**:
- Archivos CSV con información de empleados
- Columnas: Employee ID, Department, Position, Salary, Performance, etc.

**Uso en proyectos**:
- Análisis de rotación de empleados
- Performance por departamento
- Análisis de satisfacción
- Predicción de renuncias

---

## 🚀 Cómo Usar Estos Datasets

### Paso 1: Verificar Descarga
```bash
# Verificar que los datasets estén descargados
ls -la Portfolio/01_Basico/data/
```

### Paso 2: Explorar Datos
```python
import pandas as pd

# Cargar dataset
df = pd.read_csv('data/retail_sales/archivo.csv')
print(df.head())
print(df.info())
```

### Paso 3: Cargar a PostgreSQL
```python
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:password@localhost:5432/retail_analysis')
df.to_sql('ventas', engine, if_exists='replace', index=False)
```

### Paso 4: Análisis en Jupyter
- Crear notebook en `notebooks/analisis_ventas.ipynb`
- Documentar todo el proceso
- Crear visualizaciones

---

## 📝 Notas Importantes

- ⚠️ Los archivos grandes pueden estar en `.gitignore`
- ✅ Siempre documenta la fuente de los datos
- ✅ Incluye fecha de descarga en tu análisis
- ✅ Verifica la calidad de los datos antes de usar

---

## 🔗 Enlaces Útiles

- **Kaggle**: https://www.kaggle.com/datasets
- **Documentación del Portfolio**: ../FUENTES_DATOS_Y_PROYECTOS.md
- **Guía de Datasets**: ../DATASETS_RECOMENDADOS.md

---

**Última actualización**: Diciembre 2024

