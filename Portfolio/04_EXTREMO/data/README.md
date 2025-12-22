# 📊 Datasets - Nivel EXTREMO

Esta carpeta contiene los datasets descargados para proyectos de nivel EXTREMO.

## 📦 Datasets Incluidos

### 1. Store Sales Time Series Forecasting (COMPLETO)
**Fuente**: Kaggle  
**ID**: `competitions/store-sales-time-series-forecasting`  
**Carpeta**: `store_sales_completo/`

**Descripción**:
- Dataset COMPLETO de series temporales
- Big Data - Múltiples millones de registros
- Perfecto para análisis predictivo avanzado
- Requiere optimización extrema

**Estructura**:
- `train.csv` - Datos completos de entrenamiento (millones de registros)
- `test.csv` - Datos de prueba
- `stores.csv` - Información de tiendas
- `oil.csv` - Precios de petróleo históricos
- `holidays_events.csv` - Calendario completo de festivos
- `transactions.csv` - Transacciones detalladas

**Uso en proyectos**:
- Forecasting avanzado de ventas
- Análisis de estacionalidad compleja
- Modelos de Machine Learning avanzados
- Optimización de inventario a gran escala
- Análisis de factores externos múltiples

**Stack a demostrar**:
- PostgreSQL: Particionado, índices avanzados, paralelización
- Python: Procesamiento eficiente, optimización de memoria
- Jupyter: Pipeline ML completo documentado
- Excel: Reportes ejecutivos automatizados

---

### 2. Brazilian E-commerce (COMPLETO)
**Fuente**: Kaggle  
**ID**: `olistbr/brazilian-ecommerce`  
**Carpeta**: `brazilian_ecommerce_completo/`

**Descripción**:
- Dataset COMPLETO de e-commerce brasileño
- Todas las tablas relacionadas
- Múltiples millones de registros
- Excelente para proyectos end-to-end

**Estructura completa**:
- `olist_customers_dataset.csv` - Base completa de clientes
- `olist_orders_dataset.csv` - Todas las órdenes
- `olist_order_items_dataset.csv` - Todos los items (1M+)
- `olist_products_dataset.csv` - Catálogo completo
- `olist_sellers_dataset.csv` - Todos los vendedores
- `olist_geolocation_dataset.csv` - Datos geográficos completos
- `olist_order_reviews_dataset.csv` - Reviews completas
- `olist_order_payments_dataset.csv` - Pagos completos

**Uso en proyectos**:
- Sistema completo de análisis de e-commerce
- Análisis de cohortes a gran escala
- Optimización de logística
- Análisis predictivo completo
- Detección de anomalías avanzada

---

### 3. YouTube Trending Dataset
**Fuente**: Kaggle  
**ID**: `datasnaek/youtube-new`  
**Carpeta**: `youtube_trending/`

**Descripción**:
- Dataset grande de videos de YouTube
- Datos de trending por país
- Múltiples años de datos
- Perfecto para análisis de Big Data

**Estructura esperada**:
- Archivos CSV por país/región
- Columnas: video_id, title, channel_title, category_id, views, likes, dislikes, comment_count, trending_date, etc.

**Uso en proyectos**:
- Análisis de tendencias de contenido
- Predicción de viralidad
- Análisis de engagement
- Optimización de contenido
- Análisis de comportamiento de usuarios

---

## 🚀 Cómo Usar Estos Datasets

### Paso 1: Procesamiento en Chunks
```python
# scripts/procesamiento_big_data.py
import pandas as pd
from sqlalchemy import create_engine
import numpy as np

# Procesar en chunks pequeños
chunk_size = 5000
engine = create_engine('postgresql://postgres:password@localhost:5432/big_data_analysis')

# Procesar archivo grande
for i, chunk in enumerate(pd.read_csv('data/store_sales_completo/train.csv', chunksize=chunk_size)):
    print(f"Procesando chunk {i+1}...")
    # Transformaciones
    chunk_processed = transform_chunk(chunk)
    # Cargar a PostgreSQL
    chunk_processed.to_sql('ventas', engine, if_exists='append', index=False, method='multi')
```

### Paso 2: Optimización Extrema de PostgreSQL
```sql
-- Particionado de tablas por fecha
CREATE TABLE ventas (
    id SERIAL,
    fecha DATE NOT NULL,
    -- otras columnas
) PARTITION BY RANGE (fecha);

-- Crear particiones
CREATE TABLE ventas_2020 PARTITION OF ventas
    FOR VALUES FROM ('2020-01-01') TO ('2021-01-01');

CREATE TABLE ventas_2021 PARTITION OF ventas
    FOR VALUES FROM ('2021-01-01') TO ('2022-01-01');

-- Índices avanzados
CREATE INDEX CONCURRENTLY idx_ventas_fecha_store ON ventas(fecha, store_id);
CREATE INDEX CONCURRENTLY idx_ventas_producto ON ventas(product_id) WHERE cantidad > 0;

-- Vistas materializadas con refresh automático
CREATE MATERIALIZED VIEW ventas_agregadas AS
SELECT 
    DATE_TRUNC('month', fecha) AS mes,
    store_id,
    SUM(total) AS ingresos,
    COUNT(*) AS transacciones
FROM ventas
GROUP BY mes, store_id;

CREATE UNIQUE INDEX ON ventas_agregadas(mes, store_id);
```

### Paso 3: Pipeline ML Completo
```python
# notebooks/pipeline_ml_extremo.ipynb
# Feature engineering avanzado
# Validación cruzada
# Optimización de hiperparámetros
# Deployment básico
```

---

## 📝 Notas Importantes

- ⚠️ Estos datasets son EXTREMADAMENTE grandes
- ✅ SIEMPRE usa procesamiento en chunks
- ✅ Optimiza PostgreSQL con particionado
- ✅ Usa índices CONCURRENTLY para no bloquear
- ✅ Considera usar muestreo para análisis exploratorio
- ✅ Mide y documenta tiempos de ejecución
- ✅ Considera usar paralelización (multiprocessing)
- ✅ Monitorea el uso de memoria

---

## 🔗 Enlaces Útiles

- **Kaggle**: https://www.kaggle.com/datasets
- **Documentación del Portfolio**: ../FUENTES_DATOS_Y_PROYECTOS.md
- **Guía de Big Data**: Ver sección EXTREMO en FUENTES_DATOS_Y_PROYECTOS.md

---

**Última actualización**: Diciembre 2024

**Nota**: Estos proyectos están diseñados para demostrar expertise y capacidad de trabajar con Big Data.

