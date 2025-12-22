# 📊 Datasets - Nivel Avanzado

Esta carpeta contiene los datasets descargados para proyectos de nivel avanzado.

## 📦 Datasets Incluidos

### 1. Brazilian E-commerce Dataset
**Fuente**: Kaggle  
**ID**: `olistbr/brazilian-ecommerce`  
**Carpeta**: `brazilian_ecommerce/`

**Descripción**:
- Dataset grande y completo
- Múltiples tablas relacionadas
- Tamaño: ~100K órdenes, 1M+ items
- Excelente para proyectos avanzados

**Estructura**:
- `olist_customers_dataset.csv` - Información de clientes
- `olist_orders_dataset.csv` - Órdenes completas
- `olist_order_items_dataset.csv` - Items de cada orden
- `olist_products_dataset.csv` - Catálogo de productos
- `olist_sellers_dataset.csv` - Información de vendedores
- `olist_geolocation_dataset.csv` - Datos geográficos

**Uso en proyectos**:
- Análisis completo de e-commerce
- Performance de vendedores
- Análisis geográfico
- Optimización de envíos
- Análisis de cohortes avanzado

**Stack a demostrar**:
- PostgreSQL: Optimización avanzada, particionado, vistas materializadas
- Python: ETL robusto, feature engineering avanzado
- Jupyter: Análisis predictivo completo
- Excel: Reportes ejecutivos automatizados

---

### 2. Store Sales Time Series Forecasting
**Fuente**: Kaggle  
**ID**: `competitions/store-sales-time-series-forecasting`  
**Carpeta**: `store_sales/`

**Descripción**:
- Datos temporales extensos
- Perfecto para análisis predictivo
- Tamaño: ~1M+ registros
- Excelente para nivel avanzado

**Estructura esperada**:
- `train.csv` - Datos de entrenamiento
- `test.csv` - Datos de prueba
- `stores.csv` - Información de tiendas
- `oil.csv` - Precios de petróleo (variable externa)
- `holidays_events.csv` - Días festivos

**Uso en proyectos**:
- Forecasting de ventas
- Análisis de estacionalidad
- Modelos predictivos
- Optimización de inventario
- Análisis de factores externos

---

### 3. Banking Dataset
**Fuente**: Kaggle  
**ID**: `sriharipramod/bank-customer-data`  
**Carpeta**: `banking/`

**Descripción**:
- Datos financieros
- Información de clientes bancarios
- Transacciones
- Excelente para análisis de riesgo

**Estructura esperada**:
- `customers.csv` - Información de clientes
- `transactions.csv` - Transacciones
- `accounts.csv` - Información de cuentas
- `loans.csv` - Información de préstamos

**Uso en proyectos**:
- Análisis de clientes
- Detección de fraude
- Segmentación de productos
- Análisis de churn
- Predicción de riesgo crediticio

---

## 🚀 Cómo Usar Estos Datasets

### Paso 1: ETL Robusto
```python
# scripts/etl_avanzado.py
import pandas as pd
from sqlalchemy import create_engine
import numpy as np

# Cargar datos en chunks para datasets grandes
chunk_size = 10000
engine = create_engine('postgresql://postgres:password@localhost:5432/ecommerce_analysis')

for chunk in pd.read_csv('data/brazilian_ecommerce/olist_order_items_dataset.csv', chunksize=chunk_size):
    chunk.to_sql('order_items', engine, if_exists='append', index=False)
```

### Paso 2: Optimización de PostgreSQL
```sql
-- Crear índices para optimizar consultas
CREATE INDEX idx_orders_customer ON olist_orders_dataset(customer_id);
CREATE INDEX idx_orders_date ON olist_orders_dataset(order_purchase_timestamp);
CREATE INDEX idx_items_order ON olist_order_items_dataset(order_id);

-- Crear vistas materializadas
CREATE MATERIALIZED VIEW ventas_mensuales AS
SELECT 
    DATE_TRUNC('month', order_purchase_timestamp) AS mes,
    COUNT(*) AS num_ordenes,
    SUM(price) AS ingresos_totales
FROM olist_orders_dataset o
JOIN olist_order_items_dataset oi ON o.order_id = oi.order_id
GROUP BY mes;
```

### Paso 3: Análisis Predictivo
```python
# notebooks/modelo_predictivo.ipynb
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

# Feature engineering
# Entrenar modelo
# Validar resultados
```

---

## 📝 Notas Importantes

- ⚠️ Estos datasets son MUY grandes - usa procesamiento en chunks
- ✅ Optimiza PostgreSQL con índices y vistas materializadas
- ✅ Considera usar muestreo para análisis exploratorio
- ✅ Documenta todas las optimizaciones realizadas
- ✅ Mide el tiempo de ejecución de queries

---

## 🔗 Enlaces Útiles

- **Kaggle**: https://www.kaggle.com/datasets
- **Documentación del Portfolio**: ../FUENTES_DATOS_Y_PROYECTOS.md
- **Guía de Optimización**: Ver sección Avanzado en FUENTES_DATOS_Y_PROYECTOS.md

---

**Última actualización**: Diciembre 2024

