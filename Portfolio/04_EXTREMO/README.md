# 📕 Portfolio - Nivel EXTREMO (Big Data para Data Analyst)

Este nivel muestra tu capacidad como **Data Analyst trabajando con Big Data y proyectos de máxima complejidad**: datasets de millones de filas, optimización extrema en PostgreSQL, procesamiento en chunks y pipelines de Machine Learning avanzados.

## 🎯 Rol y objetivos como Data Analyst (Nivel EXTREMO)

- **Diseñar y operar soluciones analíticas sobre Big Data** (e-commerce masivo, series temporales de ventas, datos de vídeo/engagement)
- **Construir ETL y modelos de datos optimizados** con particionado, índices avanzados y vistas materializadas
- **Procesar datos en chunks y de forma eficiente** desde Python (memoria, tiempo de ejecución, paralelización básica)
- **Desarrollar pipelines ML avanzados** (feature engineering, validación cruzada, tuning) aplicados a problemas de negocio
- **Comunicar insights complejos** a stakeholders no técnicos, con dashboards y reportes ejecutivos

## 📦 Datasets y casos de negocio (vista Data Analyst)

Basado en `data/README.md`, este nivel trabaja con:

- `store_sales_completo/` – forecasting de ventas a gran escala (Kaggle Store Sales)
- `brazilian_ecommerce_completo/` – e-commerce brasileño completo (Olist)
- `youtube_trending/` – datos masivos de vídeos en tendencia (YouTube)

Cada uno sirve como base para diferentes proyectos de alto nivel.

---

### 1. Store Sales Time Series Forecasting (COMPLETO)

**Rol como Data Analyst**: Diseñar un sistema de forecasting de ventas a gran escala que soporte planificación de inventario, staffing y estrategia comercial.

**Contexto de negocio**  
- Cadenas de tiendas con ventas diarias por tienda/producto  
- Necesidad de anticipar la demanda futura para **reducir roturas de stock y exceso de inventario**

**Preguntas clave**:
- ¿Cómo se comportan las ventas por tienda y por familia de productos a lo largo del tiempo?  
- ¿Qué impacto tienen festivos, precios del petróleo y otros factores externos?  
- ¿Qué ventas esperamos en los próximos meses por tienda / categoría?

**Tecnologías**:
- PostgreSQL: tablas particionadas, índices avanzados, vistas materializadas
- Python: procesamiento en chunks, optimización de memoria
- ML: `scikit-learn` / `statsmodels` para modelos de series temporales / regresión
- Jupyter: pipeline de forecasting documentado

**Entregables (esperados)**:
- `scripts/procesamiento_big_data.py` (u otro ETL similar para `store_sales_completo/`)
- `sql/schema_store_sales_extremo.sql` y scripts de particionado/índices
- `notebooks/pipeline_ml_extremo.ipynb`
- `figures/forecasting_store_sales.png`

**Habilidades demostradas**:
- Trabajo con **millones de registros** sin romper memoria
- Diseño de pipeline de forecasting con variables externas
- Optimización de consultas para análisis y modelos
- Comunicación de escenarios de demanda a negocio

---

### 2. Brazilian E-commerce (COMPLETO)

**Rol como Data Analyst**: Liderar un **proyecto end-to-end de e-commerce** con todas las tablas (clientes, órdenes, reviews, pagos, logística, geolocalización).

**Contexto de negocio**  
- Marketplace grande con múltiples vendedores y regiones  
- Interés en entender **performance global**, satisfacción (reviews), logística y comportamiento de clientes

**Preguntas clave**:
- ¿Qué segmentos de clientes y productos generan más valor a largo plazo?  
- ¿Cómo se relacionan tiempos de entrega y reviews con churn/retención?  
- ¿Qué regiones / vendedores requieren acciones de mejora?

**Tecnologías**:
- PostgreSQL: modelo relacional completo y optimizado
- Python: ETL avanzado, feature engineering a gran escala
- Jupyter: análisis de cohortes, LTV, logística, satisfacción

**Entregables (esperados)**:
- `scripts/etl_brazilian_ecommerce_extremo.py`
- `sql/schema_olist_extremo.sql`, `sql/queries_avanzadas_olist.sql`
- `notebooks/analisis_extremo_ecommerce.ipynb`

**Habilidades demostradas**:
- Integración de múltiples tablas grandes
- Métricas avanzadas de negocio (LTV, NPS proxy via reviews, tiempos de entrega)
- Análisis de cohortes y retención a gran escala
- Identificación de oportunidades de mejora operativa

---

### 3. YouTube Trending Big Data

**Rol como Data Analyst**: Analizar grandes volúmenes de datos de vídeos de YouTube para entender **tendencias de contenido y engagement**.

**Contexto de negocio**  
- Grandes volúmenes de vídeos trending por país y fecha  
- Objetivo: identificar **patrones de viralidad**, categorías ganadoras y comportamiento de usuarios

**Preguntas clave**:
- ¿Qué tipos de contenido tienden a volverse virales por país / periodo?  
- ¿Qué factores (categoría, duración, título, canal) se asocian a mayor engagement?  
- ¿Cómo cambian las tendencias a lo largo del tiempo?

**Tecnologías**:
- Python: procesamiento de múltiples archivos CSV grandes (chunking)
- PostgreSQL (opcional): almacenamiento y agregaciones para análisis
- Jupyter: análisis y visualización de tendencias

**Entregables (esperados)**:
- `scripts/etl_youtube_trending_extremo.py`
- `notebooks/analisis_youtube_trending.ipynb`
- `figures/trending_patterns.png`

**Habilidades demostradas**:
- Manejo de datos semiestructurados a gran escala
- Análisis de engagement y tendencias de contenido
- Visualizaciones de alto impacto para presentar resultados

---

## 🚀 Cómo Ejecutar (flujo Big Data)

### Requisitos avanzados

```bash
pip install scikit-learn statsmodels dash streamlit schedule openpyxl
```

### Flujo recomendado

1. **Carga y procesamiento en chunks**  
   - Usar scripts como `scripts/procesamiento_big_data.py` (ver ejemplo en `data/README.md`)  
   - Procesar y cargar a PostgreSQL en tablas particionadas
2. **Optimización extrema en PostgreSQL**  
   - Crear particiones por fecha / región / tienda  
   - Crear índices avanzados e índices `CONCURRENTLY`  
   - Definir vistas materializadas para agregados pesados
3. **Pipeline ML avanzado**  
   - `notebooks/pipeline_ml_extremo.ipynb`: feature engineering, validación cruzada, tuning  
   - Medir tiempos de entrenamiento y scoring
4. **Análisis y reporting**  
   - Construir notebooks de análisis (ventas, e-commerce, YouTube)  
   - Generar figuras para portfolio (`figures/`) y reportes ejecutivos

---

## ✅ Checklist de Habilidades EXTREMAS (Data Analyst Big Data)

- [x] ETL en chunks para datasets de millones de filas
- [x] Particionado e índices avanzados en PostgreSQL
- [x] Optimización de tiempos de ejecución y uso de memoria
- [x] Pipelines ML avanzados aplicados a problemas de negocio
- [x] Análisis de series temporales y forecasting a gran escala
- [x] Proyectos end-to-end con múltiples fuentes grandes
- [x] Comunicación clara de insights complejos

---

**Nivel**: EXTREMO – Data Analyst especializado en Big Data


