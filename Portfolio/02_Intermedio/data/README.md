# 📊 Datasets - Nivel Intermedio

Esta carpeta contiene los datasets descargados para proyectos de nivel intermedio.

## 📦 Datasets Incluidos

### 1. E-commerce Customer Data
**Fuente**: Kaggle  
**ID**: `carrie1/ecommerce-data`  
**Carpeta**: `ecommerce/`

**Descripción**:
- Datos de e-commerce reales
- Información de clientes y órdenes
- Tamaño: ~500K registros
- Excelente para análisis avanzado

**Estructura esperada**:
- `customers.csv`: customer_id, nombre, email, país
- `orders.csv`: order_id, customer_id, fecha, total
- `order_items.csv`: item_id, order_id, product_id, cantidad
- `products.csv`: product_id, nombre, categoría, precio

**Uso en proyectos**:
- Análisis de cohortes de clientes
- Customer Lifetime Value (CLV)
- Análisis de productos más vendidos
- Predicción de ventas

**Stack a demostrar**:
- PostgreSQL: CTEs complejos, Window Functions
- Python: Análisis de cohortes, feature engineering
- Jupyter: Análisis predictivo
- Excel: Dashboard ejecutivo

---

### 2. Online Retail Dataset (UCI)
**Fuente**: UCI Machine Learning Repository  
**URL**: https://archive.ics.uci.edu/ml/datasets/Online+Retail  
**Carpeta**: `online_retail/`

**Descripción**:
- Dataset clásico y bien documentado
- Datos de transacciones online
- Tamaño: ~540K registros
- Perfecto para análisis temporal

**Estructura**:
- `OnlineRetail.xlsx`
- Columnas: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

**Uso en proyectos**:
- Análisis de frecuencia de compra
- RFM Analysis (Recency, Frequency, Monetary)
- Análisis de productos por país
- Detección de anomalías

---

### 3. Marketing Analytics Dataset
**Fuente**: Kaggle  
**ID**: `datasnaek/marketing-analytics`  
**Carpeta**: `marketing/`

**Descripción**:
- Datos de marketing digital
- Múltiples canales
- Métricas de conversión
- Perfecto para análisis de ROI

**Estructura esperada**:
- Archivos CSV con datos de campañas
- Columnas: Campaign ID, Channel, Impressions, Clicks, Conversions, Cost, Revenue, etc.

**Uso en proyectos**:
- Análisis de campañas
- ROI por canal
- Segmentación de audiencia
- Optimización de presupuesto

---

## 🚀 Cómo Usar Estos Datasets

### Paso 1: Preparar Datos para PostgreSQL
```python
import pandas as pd
from sqlalchemy import create_engine

# Cargar múltiples archivos
customers = pd.read_csv('data/ecommerce/customers.csv')
orders = pd.read_csv('data/ecommerce/orders.csv')
order_items = pd.read_csv('data/ecommerce/order_items.csv')
products = pd.read_csv('data/ecommerce/products.csv')

# Conectar a PostgreSQL
engine = create_engine('postgresql://postgres:password@localhost:5432/ecommerce_analysis')

# Cargar tablas
customers.to_sql('clientes', engine, if_exists='replace', index=False)
orders.to_sql('ordenes', engine, if_exists='replace', index=False)
order_items.to_sql('order_items', engine, if_exists='replace', index=False)
products.to_sql('productos', engine, if_exists='replace', index=False)
```

### Paso 2: Consultas SQL Avanzadas
```sql
-- Ver archivo: sql/performance_analysis.sql
-- Incluye JOINs múltiples, Window Functions, CTEs
```

### Paso 3: Análisis en Jupyter
- Dashboard interactivo con widgets
- Análisis de cohortes
- Visualizaciones avanzadas

---

## 📝 Notas Importantes

- ⚠️ Estos datasets son más grandes que los básicos
- ✅ Usa índices en PostgreSQL para optimizar consultas
- ✅ Considera usar muestreo para análisis exploratorio inicial
- ✅ Documenta todas las transformaciones

---

## 🔗 Enlaces Útiles

- **Kaggle**: https://www.kaggle.com/datasets
- **UCI Repository**: https://archive.ics.uci.edu/ml/index.php
- **Documentación del Portfolio**: ../FUENTES_DATOS_Y_PROYECTOS.md

---

**Última actualización**: Diciembre 2024

