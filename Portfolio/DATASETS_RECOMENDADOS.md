# 📊 Datasets Recomendados para Portfolio Data Analyst

Lista detallada de datasets reales y gratuitos perfectos para demostrar el stack completo.

---

## 🎯 CRITERIOS DE SELECCIÓN

Los datasets recomendados cumplen con:
- ✅ **Datos reales** (no sintéticos)
- ✅ **Tamaño adecuado** (10K - 1M registros)
- ✅ **Múltiples tablas/relaciones** (para JOINs)
- ✅ **Datos temporales** (para análisis de tendencias)
- ✅ **Fácil de descargar** (formato CSV, JSON, SQL)
- ✅ **Bien documentados**

---

## ⭐ TOP 10 DATASETS RECOMENDADOS

### 1. **Retail Sales Dataset** ⭐⭐⭐⭐⭐
**Fuente**: Kaggle  
**ID**: `imtkaggleteam/retail-sales-dataset`  
**URL**: https://www.kaggle.com/datasets/imtkaggleteam/retail-sales-dataset

**Características**:
- ✅ Datos de ventas retail reales
- ✅ Múltiples dimensiones (tiempo, producto, región, cliente)
- ✅ Tamaño: ~50K-100K registros
- ✅ Perfecto para análisis básico e intermedio

**Estructura típica**:
- `ventas.csv`: fecha, producto_id, cantidad, total, región
- `productos.csv`: producto_id, nombre, categoría, precio
- `clientes.csv`: cliente_id, nombre, ciudad, segmento

**Proyectos posibles**:
- Análisis de ventas por región/mes
- Performance de productos
- Análisis de tendencias temporales
- Segmentación de clientes

**Stack a demostrar**:
- PostgreSQL: JOINs, GROUP BY, Window Functions
- Python: pandas groupby, análisis temporal
- Jupyter: Dashboard interactivo
- Excel: Tablas dinámicas y gráficos

---

### 2. **E-commerce Customer Data** ⭐⭐⭐⭐⭐
**Fuente**: Kaggle  
**ID**: `carrie1/ecommerce-data`  
**URL**: https://www.kaggle.com/datasets/carrie1/ecommerce-data

**Características**:
- ✅ Datos de e-commerce reales
- ✅ Información de clientes y órdenes
- ✅ Tamaño: ~500K registros
- ✅ Excelente para análisis avanzado

**Estructura típica**:
- `customers.csv`: customer_id, nombre, email, país
- `orders.csv`: order_id, customer_id, fecha, total
- `order_items.csv`: item_id, order_id, product_id, cantidad
- `products.csv`: product_id, nombre, categoría, precio

**Proyectos posibles**:
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

### 3. **Online Retail Dataset (UCI)** ⭐⭐⭐⭐
**Fuente**: UCI Machine Learning Repository  
**URL**: https://archive.ics.uci.edu/ml/datasets/Online+Retail

**Características**:
- ✅ Dataset clásico y bien documentado
- ✅ Datos de transacciones online
- ✅ Tamaño: ~540K registros
- ✅ Perfecto para análisis temporal

**Estructura**:
- InvoiceNo, StockCode, Description, Quantity
- InvoiceDate, UnitPrice, CustomerID, Country

**Proyectos posibles**:
- Análisis de frecuencia de compra
- RFM Analysis (Recency, Frequency, Monetary)
- Análisis de productos por país
- Detección de anomalías

---

### 4. **Brazilian E-commerce** ⭐⭐⭐⭐⭐
**Fuente**: Kaggle  
**ID**: `olistbr/brazilian-ecommerce`  
**URL**: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

**Características**:
- ✅ Dataset grande y completo
- ✅ Múltiples tablas relacionadas
- ✅ Tamaño: ~100K órdenes, 1M+ items
- ✅ Excelente para proyectos avanzados

**Estructura**:
- `olist_customers_dataset.csv`
- `olist_orders_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_products_dataset.csv`
- `olist_sellers_dataset.csv`
- `olist_geolocation_dataset.csv`

**Proyectos posibles**:
- Análisis completo de e-commerce
- Performance de vendedores
- Análisis geográfico
- Optimización de envíos

---

### 5. **HR Analytics Dataset** ⭐⭐⭐⭐
**Fuente**: Kaggle  
**ID**: `arindam235/startup-investments-crunchbase`  
**URL**: https://www.kaggle.com/datasets/arindam235/startup-investments-crunchbase

**Características**:
- ✅ Datos de recursos humanos
- ✅ Análisis de empleados y performance
- ✅ Tamaño: ~15K registros
- ✅ Perfecto para análisis de negocio

**Proyectos posibles**:
- Análisis de rotación de empleados
- Performance por departamento
- Análisis de satisfacción
- Predicción de renuncias

---

### 6. **Superstore Sales Dataset** ⭐⭐⭐⭐
**Fuente**: Kaggle  
**Búsqueda**: "superstore sales"

**Características**:
- ✅ Dataset muy popular
- ✅ Datos de supermercado/retail
- ✅ Múltiples dimensiones
- ✅ Perfecto para dashboards

**Proyectos posibles**:
- Dashboard completo de ventas
- Análisis de profitabilidad
- Segmentación de productos
- Análisis de tendencias

---

### 7. **Store Sales Time Series** ⭐⭐⭐⭐⭐
**Fuente**: Kaggle  
**ID**: `competitions/store-sales-time-series-forecasting`

**Características**:
- ✅ Datos temporales extensos
- ✅ Perfecto para análisis predictivo
- ✅ Tamaño: ~1M+ registros
- ✅ Excelente para nivel avanzado

**Proyectos posibles**:
- Forecasting de ventas
- Análisis de estacionalidad
- Modelos predictivos
- Optimización de inventario

---

### 8. **Marketing Analytics** ⭐⭐⭐⭐
**Fuente**: Kaggle  
**ID**: `datasnaek/marketing-analytics`

**Características**:
- ✅ Datos de marketing digital
- ✅ Múltiples canales
- ✅ Métricas de conversión
- ✅ Perfecto para análisis de ROI

**Proyectos posibles**:
- Análisis de campañas
- ROI por canal
- Segmentación de audiencia
- Optimización de presupuesto

---

### 9. **Banking Dataset** ⭐⭐⭐⭐
**Fuente**: Kaggle  
**Búsqueda**: "banking dataset" o "bank customer data"

**Características**:
- ✅ Datos financieros
- ✅ Información de clientes bancarios
- ✅ Transacciones
- ✅ Excelente para análisis de riesgo

**Proyectos posibles**:
- Análisis de clientes
- Detección de fraude
- Segmentación de productos
- Análisis de churn

---

### 10. **Airline Passenger Satisfaction** ⭐⭐⭐⭐
**Fuente**: Kaggle  
**Búsqueda**: "airline passenger satisfaction"

**Características**:
- ✅ Datos de satisfacción de clientes
- ✅ Múltiples variables categóricas
- ✅ Perfecto para análisis de calidad
- ✅ Tamaño: ~100K registros

**Proyectos posibles**:
- Análisis de satisfacción
- Identificación de problemas
- Predicción de satisfacción
- Mejora de servicios

---

## 📥 CÓMO DESCARGAR DATASETS

### Método 1: Kaggle (Recomendado)
```python
# Usar el script incluido
python Portfolio/scripts/descargar_datos_kaggle.py

# O manualmente:
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
api.dataset_download_files('usuario/dataset-name', path='./data', unzip=True)
```

### Método 2: Descarga Manual
1. Ir a la página del dataset en Kaggle
2. Click en "Download"
3. Descomprimir en la carpeta `data/`

### Método 3: UCI Repository
1. Ir a https://archive.ics.uci.edu/ml/index.php
2. Buscar dataset
3. Click en "Data Folder"
4. Descargar archivos CSV

---

## 🎯 SELECCIÓN POR NIVEL

### 📘 Nivel Básico
**Recomendados**:
1. Retail Sales Dataset (pequeño)
2. Superstore Sales Dataset
3. HR Analytics Dataset

**Razón**: Datasets pequeños, bien estructurados, fáciles de entender

---

### 📗 Nivel Intermedio
**Recomendados**:
1. E-commerce Customer Data
2. Online Retail Dataset (UCI)
3. Marketing Analytics

**Razón**: Múltiples tablas, relaciones complejas, análisis más profundos

---

### 📙 Nivel Avanzado
**Recomendados**:
1. Brazilian E-commerce
2. Store Sales Time Series
3. Banking Dataset

**Razón**: Datasets grandes, análisis predictivo, optimización necesaria

---

### 📕 Nivel EXTREMO
**Recomendados**:
1. Store Sales Time Series (completo)
2. Múltiples datasets integrados
3. Datasets de 1M+ registros

**Razón**: Big Data, optimización avanzada, proyectos end-to-end

---

## 📋 CHECKLIST ANTES DE USAR UN DATASET

Antes de empezar un proyecto, verifica:

- [ ] ✅ El dataset tiene suficientes registros (mínimo 10K)
- [ ] ✅ Hay múltiples tablas/columnas para JOINs
- [ ] ✅ Los datos tienen fechas (para análisis temporal)
- [ ] ✅ El dataset está bien documentado
- [ ] ✅ Los datos son reales (no sintéticos)
- [ ] ✅ El formato es compatible (CSV, JSON, SQL)
- [ ] ✅ Hay datos faltantes (para demostrar limpieza)
- [ ] ✅ El dataset es relevante para el nivel del proyecto

---

## 🔗 ENLACES DIRECTOS

### Kaggle
- Retail Sales: https://www.kaggle.com/datasets?search=retail+sales
- E-commerce: https://www.kaggle.com/datasets?search=ecommerce
- Customer Data: https://www.kaggle.com/datasets?search=customer

### UCI
- Online Retail: https://archive.ics.uci.edu/ml/datasets/Online+Retail
- Customer Segmentation: https://archive.ics.uci.edu/ml/datasets

### Data.gov
- Business Data: https://data.gov/browse?category=Business

---

## 💡 CONSEJOS FINALES

1. **Empieza pequeño**: Usa datasets de 10K-50K registros primero
2. **Documenta la fuente**: Siempre menciona de dónde vienen los datos
3. **Limpia los datos**: Muestra el proceso de limpieza
4. **Usa datos reales**: No uses solo datasets de ejemplo
5. **Varía los datasets**: Muestra experiencia en diferentes industrias

---

**Última actualización**: Diciembre 2024

