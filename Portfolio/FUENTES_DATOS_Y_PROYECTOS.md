# 🎯 Fuentes de Datos y Proyectos para Data Analyst Jr

Guía completa de fuentes de datos reales y proyectos detallados para demostrar el stack completo:
- **PostgreSQL** ⭐
- **Python** (pandas, numpy)
- **Jupyter**
- **Excel / Sheets**
- **Git**

---

## 📊 FUENTES DE DATOS RECOMENDADAS (GRATUITAS)

### ⭐ **1. KAGGLE** - La mejor opción para Data Analyst
**URL**: https://www.kaggle.com/datasets

**Por qué es la mejor**:
- ✅ Miles de datasets reales y actualizados
- ✅ Datasets de diferentes industrias (retail, finanzas, salud, e-commerce)
- ✅ Tamaños variados (pequeños para empezar, grandes para avanzar)
- ✅ Comunidad activa con notebooks de ejemplo
- ✅ Competencias para practicar

**Cómo descargar**:
1. Crear cuenta gratuita en Kaggle
2. Buscar dataset (ej: "retail sales", "e-commerce", "customer data")
3. Click en "Download" o usar API
4. Descargar como CSV, JSON, o SQL

**Datasets recomendados para Portfolio**:
- **Retail Sales**: `retail-sales-dataset`, `superstore-sales`
- **E-commerce**: `ecommerce-customer-data`, `online-retail`
- **HR Analytics**: `hr-analytics`, `employee-data`
- **Financial**: `stock-market-data`, `banking-dataset`

**Ejemplo de uso con Python**:
```python
# Instalar kaggle API
# pip install kaggle

# Configurar credenciales (desde tu cuenta Kaggle)
# Descargar dataset
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
api.dataset_download_files('dataset-name', path='./data', unzip=True)
```

---

### ⭐ **2. UCI MACHINE LEARNING REPOSITORY**
**URL**: https://archive.ics.uci.edu/ml/index.php

**Por qué es excelente**:
- ✅ Datasets clásicos y bien documentados
- ✅ Perfectos para análisis estadísticos
- ✅ Datos limpios y estructurados
- ✅ Ideal para proyectos de nivel básico e intermedio

**Datasets recomendados**:
- **Retail**: `Online Retail Dataset`
- **Customer**: `Customer Segmentation Dataset`
- **Sales**: `Sales Transactions Dataset`

**Cómo descargar**:
1. Buscar dataset en el repositorio
2. Click en "Data Folder"
3. Descargar archivos CSV directamente

---

### ⭐ **3. DATA.GOV** (Estados Unidos)
**URL**: https://data.gov/

**Por qué es útil**:
- ✅ Datos gubernamentales reales
- ✅ Datos de economía, comercio, demografía
- ✅ Excelente para análisis de tendencias
- ✅ Datos históricos extensos

**Categorías útiles**:
- Business & Economy
- Consumer & Finance
- Trade & International

---

### ⭐ **4. GOOGLE DATASET SEARCH**
**URL**: https://datasetsearch.research.google.com/

**Por qué es potente**:
- ✅ Busca datasets en múltiples fuentes
- ✅ Filtros por formato, licencia, fecha
- ✅ Enlaces directos a datasets

---

### ⭐ **5. GITHUB - AWESOME PUBLIC DATASETS**
**URL**: https://github.com/awesomedata/awesome-public-datasets

**Por qué es valioso**:
- ✅ Lista curada de datasets públicos
- ✅ Organizados por categoría
- ✅ Enlaces directos a fuentes

---

### ⭐ **6. DATA.WORLD**
**URL**: https://data.world/

**Por qué es recomendable**:
- ✅ Datasets de diferentes fuentes
- ✅ Interfaz amigable
- ✅ Descarga directa o API

---

### ⭐ **7. FIVETHIRTYEIGHT** (538)
**URL**: https://data.fivethirtyeight.com/

**Por qué es interesante**:
- ✅ Datos usados en artículos periodísticos
- ✅ Datos reales y actualizados
- ✅ Perfectos para análisis de tendencias

---

## 🚀 PROYECTOS DETALLADOS POR NIVEL

### 📘 NIVEL BÁSICO - Proyecto 1: Análisis de Ventas Retail

#### **Objetivo**: Demostrar habilidades básicas con datos reales de ventas

#### **Dataset Recomendado**: 
- **Kaggle**: "Superstore Sales Dataset" o "Retail Sales Dataset"
- **Alternativa**: Crear dataset sintético basado en datos reales

#### **Stack a Demostrar**:
1. ✅ **PostgreSQL**: Crear base de datos y tablas
2. ✅ **Python (pandas)**: Cargar y explorar datos
3. ✅ **Jupyter**: Análisis documentado
4. ✅ **Excel**: Exportar resultados y crear dashboard básico
5. ✅ **Git**: Versionar el proyecto

#### **Paso a Paso Detallado**:

##### **PASO 1: Descargar Datos**
```bash
# Opción 1: Desde Kaggle
# 1. Ir a https://www.kaggle.com/datasets
# 2. Buscar "superstore sales" o "retail sales"
# 3. Descargar CSV

# Opción 2: Usar dataset de ejemplo
# Crear carpeta data/
mkdir Portfolio/01_Basico/data
# Descargar archivo a: Portfolio/01_Basico/data/sales_data.csv
```

##### **PASO 2: Configurar PostgreSQL**
```sql
-- Conectar a PostgreSQL
psql -U postgres

-- Crear base de datos
CREATE DATABASE retail_analysis;

-- Conectarse a la base de datos
\c retail_analysis

-- Crear tabla de ventas
CREATE TABLE ventas (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    region VARCHAR(50),
    producto VARCHAR(100),
    categoria VARCHAR(50),
    cantidad INTEGER,
    precio_unitario DECIMAL(10, 2),
    total DECIMAL(10, 2),
    vendedor VARCHAR(100),
    cliente_id INTEGER
);

-- Crear índices para optimizar consultas
CREATE INDEX idx_ventas_fecha ON ventas(fecha);
CREATE INDEX idx_ventas_region ON ventas(region);
CREATE INDEX idx_ventas_categoria ON ventas(categoria);
```

##### **PASO 3: Cargar Datos con Python**
```python
# scripts/cargar_datos_postgresql.py
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Leer datos CSV
df = pd.read_csv('data/sales_data.csv')

# Limpiar datos básicos
df = df.dropna(subset=['fecha', 'total'])
df['fecha'] = pd.to_datetime(df['fecha'])

# Conectar a PostgreSQL
engine = create_engine('postgresql://postgres:tu_password@localhost:5432/retail_analysis')

# Cargar datos a PostgreSQL
df.to_sql('ventas', engine, if_exists='replace', index=False)

print(f"✅ Datos cargados: {len(df)} registros")
```

##### **PASO 4: Análisis en Jupyter**
```python
# notebooks/analisis_ventas_basico.ipynb

# Celda 1: Importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Celda 2: Conectar a PostgreSQL
engine = create_engine('postgresql://postgres:password@localhost:5432/retail_analysis')

# Celda 3: Cargar datos
query = "SELECT * FROM ventas"
df = pd.read_sql(query, engine)

# Celda 4: Exploración básica
print("Shape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nPrimeras filas:")
df.head()

# Celda 5: Estadísticas descriptivas
df.describe()

# Celda 6: Visualizaciones básicas
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Ventas por región
df.groupby('region')['total'].sum().plot(kind='bar', ax=axes[0,0])
axes[0,0].set_title('Ventas por Región')

# Ventas por mes
df['mes'] = pd.to_datetime(df['fecha']).dt.to_period('M')
df.groupby('mes')['total'].sum().plot(kind='line', ax=axes[0,1])
axes[0,1].set_title('Ventas Mensuales')

# Top productos
df.groupby('producto')['total'].sum().nlargest(10).plot(kind='barh', ax=axes[1,0])
axes[1,0].set_title('Top 10 Productos')

# Distribución de ventas
df['total'].hist(bins=50, ax=axes[1,1])
axes[1,1].set_title('Distribución de Ventas')

plt.tight_layout()
plt.savefig('../figures/analisis_ventas_basico.png', dpi=300)
```

##### **PASO 5: Consultas SQL Básicas**
```sql
-- sql/consultas_ventas_basico.sql

-- Total de ventas
SELECT 
    COUNT(*) AS total_transacciones,
    SUM(total) AS ingresos_totales,
    AVG(total) AS ticket_promedio
FROM ventas;

-- Ventas por región
SELECT 
    region,
    COUNT(*) AS num_ventas,
    SUM(total) AS total_ventas,
    AVG(total) AS promedio
FROM ventas
GROUP BY region
ORDER BY total_ventas DESC;

-- Ventas por mes
SELECT 
    DATE_TRUNC('month', fecha) AS mes,
    COUNT(*) AS num_ventas,
    SUM(total) AS total_mes
FROM ventas
GROUP BY mes
ORDER BY mes;

-- Top 10 productos
SELECT 
    producto,
    SUM(cantidad) AS unidades_vendidas,
    SUM(total) AS ingresos
FROM ventas
GROUP BY producto
ORDER BY ingresos DESC
LIMIT 10;
```

##### **PASO 6: Exportar a Excel**
```python
# scripts/exportar_a_excel.py
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:password@localhost:5432/retail_analysis')

# Consultas para Excel
queries = {
    'Resumen': "SELECT COUNT(*) as total, SUM(total) as ingresos FROM ventas",
    'Por Region': "SELECT region, COUNT(*) as ventas, SUM(total) as total FROM ventas GROUP BY region",
    'Por Mes': "SELECT DATE_TRUNC('month', fecha) as mes, COUNT(*) as ventas, SUM(total) as total FROM ventas GROUP BY mes ORDER BY mes"
}

# Crear Excel con múltiples hojas
with pd.ExcelWriter('excel/reporte_ventas.xlsx', engine='openpyxl') as writer:
    for nombre, query in queries.items():
        df = pd.read_sql(query, engine)
        df.to_excel(writer, sheet_name=nombre, index=False)

print("✅ Reporte Excel creado: excel/reporte_ventas.xlsx")
```

##### **PASO 7: Control de Versiones con Git**
```bash
# Inicializar repositorio (si no existe)
git init

# Crear .gitignore
echo "*.csv" >> .gitignore
echo "*.xlsx" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".ipynb_checkpoints/" >> .gitignore

# Agregar archivos
git add .
git commit -m "feat: Análisis básico de ventas retail

- Configuración de PostgreSQL
- Scripts de carga de datos
- Notebook de análisis exploratorio
- Consultas SQL básicas
- Exportación a Excel
- Visualizaciones básicas"

# Subir a GitHub/GitLab
git remote add origin https://github.com/tu-usuario/portfolio-data-analyst.git
git push -u origin main
```

---

### 📗 NIVEL INTERMEDIO - Proyecto 2: Análisis de Performance E-commerce

#### **Objetivo**: Análisis completo con JOINs, Window Functions y dashboards

#### **Dataset Recomendado**:
- **Kaggle**: "E-commerce Customer Data" o "Online Retail Dataset"
- **UCI**: "Online Retail Dataset"

#### **Stack a Demostrar**:
1. ✅ **PostgreSQL**: JOINs complejos, Window Functions, CTEs
2. ✅ **Python (pandas avanzado)**: Transformaciones complejas, análisis estadístico
3. ✅ **Jupyter**: Dashboard interactivo con widgets
4. ✅ **Excel**: Dashboard con tablas dinámicas y gráficos
5. ✅ **Git**: Branches, commits descriptivos

#### **Estructura del Proyecto**:
```
02_Intermedio/
├── data/
│   ├── customers.csv
│   ├── orders.csv
│   ├── products.csv
│   └── order_items.csv
├── sql/
│   ├── schema_ecommerce.sql
│   ├── performance_analysis.sql
│   └── cohort_analysis.sql
├── notebooks/
│   ├── dashboard_ecommerce.ipynb
│   └── analisis_avanzado.ipynb
├── scripts/
│   ├── etl_ecommerce.py
│   └── generar_dashboard.py
├── excel/
│   └── dashboard_ecommerce.xlsx
└── figures/
    └── dashboard_ecommerce.png
```

#### **Paso a Paso**:

##### **PASO 1: Schema PostgreSQL Completo**
```sql
-- sql/schema_ecommerce.sql

CREATE DATABASE ecommerce_analysis;

\c ecommerce_analysis

-- Tabla de clientes
CREATE TABLE clientes (
    customer_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    ciudad VARCHAR(50),
    pais VARCHAR(50),
    fecha_registro DATE,
    segmento VARCHAR(50)
);

-- Tabla de productos
CREATE TABLE productos (
    product_id SERIAL PRIMARY KEY,
    nombre VARCHAR(200),
    categoria VARCHAR(50),
    subcategoria VARCHAR(50),
    precio DECIMAL(10, 2),
    costo DECIMAL(10, 2)
);

-- Tabla de órdenes
CREATE TABLE ordenes (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES clientes(customer_id),
    fecha_orden DATE,
    fecha_envio DATE,
    estado VARCHAR(20),
    region VARCHAR(50),
    total DECIMAL(10, 2)
);

-- Tabla de items de orden
CREATE TABLE order_items (
    item_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES ordenes(order_id),
    product_id INTEGER REFERENCES productos(product_id),
    cantidad INTEGER,
    precio_unitario DECIMAL(10, 2),
    descuento DECIMAL(5, 2),
    subtotal DECIMAL(10, 2)
);

-- Índices para optimización
CREATE INDEX idx_ordenes_customer ON ordenes(customer_id);
CREATE INDEX idx_ordenes_fecha ON ordenes(fecha_orden);
CREATE INDEX idx_items_order ON order_items(order_id);
CREATE INDEX idx_items_product ON order_items(product_id);
```

##### **PASO 2: ETL con Python**
```python
# scripts/etl_ecommerce.py
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from datetime import datetime, timedelta

print("=" * 60)
print("ETL E-COMMERCE - Nivel Intermedio")
print("=" * 60)

# Conectar a PostgreSQL
engine = create_engine('postgresql://postgres:password@localhost:5432/ecommerce_analysis')

# 1. Cargar datos CSV
print("\n1. Cargando datos...")
clientes_df = pd.read_csv('data/customers.csv')
productos_df = pd.read_csv('data/products.csv')
ordenes_df = pd.read_csv('data/orders.csv')
items_df = pd.read_csv('data/order_items.csv')

# 2. Limpieza y transformación
print("\n2. Limpiando datos...")

# Limpiar clientes
clientes_df['fecha_registro'] = pd.to_datetime(clientes_df['fecha_registro'])
clientes_df = clientes_df.dropna(subset=['email'])

# Limpiar productos
productos_df['precio'] = pd.to_numeric(productos_df['precio'], errors='coerce')
productos_df['costo'] = pd.to_numeric(productos_df['costo'], errors='coerce')
productos_df = productos_df.dropna(subset=['precio'])

# Limpiar órdenes
ordenes_df['fecha_orden'] = pd.to_datetime(ordenes_df['fecha_orden'])
ordenes_df['fecha_envio'] = pd.to_datetime(ordenes_df['fecha_envio'])
ordenes_df['total'] = ordenes_df['total'].fillna(0)

# Limpiar items
items_df['precio_unitario'] = pd.to_numeric(items_df['precio_unitario'], errors='coerce')
items_df['cantidad'] = pd.to_numeric(items_df['cantidad'], errors='coerce')
items_df['subtotal'] = items_df['cantidad'] * items_df['precio_unitario'] * (1 - items_df['descuento'].fillna(0))

# 3. Cargar a PostgreSQL
print("\n3. Cargando a PostgreSQL...")
clientes_df.to_sql('clientes', engine, if_exists='replace', index=False)
productos_df.to_sql('productos', engine, if_exists='replace', index=False)
ordenes_df.to_sql('ordenes', engine, if_exists='replace', index=False)
items_df.to_sql('order_items', engine, if_exists='replace', index=False)

print("\n✅ ETL completado exitosamente!")
print(f"   - Clientes: {len(clientes_df)}")
print(f"   - Productos: {len(productos_df)}")
print(f"   - Órdenes: {len(ordenes_df)}")
print(f"   - Items: {len(items_df)}")
```

##### **PASO 3: Consultas SQL Avanzadas**
```sql
-- sql/performance_analysis.sql

-- Análisis completo de performance con JOINs múltiples
WITH ventas_completas AS (
    SELECT 
        o.order_id,
        o.fecha_orden,
        c.customer_id,
        c.nombre AS cliente,
        c.segmento,
        c.pais,
        p.product_id,
        p.nombre AS producto,
        p.categoria,
        oi.cantidad,
        oi.precio_unitario,
        oi.descuento,
        oi.subtotal,
        o.total AS total_orden,
        o.region
    FROM ordenes o
    JOIN clientes c ON o.customer_id = c.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN productos p ON oi.product_id = p.product_id
),
metricas_clientes AS (
    SELECT 
        customer_id,
        cliente,
        segmento,
        pais,
        COUNT(DISTINCT order_id) AS num_ordenes,
        SUM(subtotal) AS total_gastado,
        AVG(total_orden) AS ticket_promedio,
        MAX(fecha_orden) AS ultima_compra
    FROM ventas_completas
    GROUP BY customer_id, cliente, segmento, pais
)
SELECT 
    *,
    RANK() OVER (ORDER BY total_gastado DESC) AS ranking_cliente,
    RANK() OVER (PARTITION BY segmento ORDER BY total_gastado DESC) AS ranking_segmento,
    CASE 
        WHEN total_gastado >= PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY total_gastado) OVER ()
        THEN 'VIP'
        WHEN total_gastado >= PERCENTILE_CONT(0.7) WITHIN GROUP (ORDER BY total_gastado) OVER ()
        THEN 'Premium'
        ELSE 'Regular'
    END AS categoria_cliente
FROM metricas_clientes
ORDER BY total_gastado DESC;
```

##### **PASO 4: Dashboard en Jupyter**
```python
# notebooks/dashboard_ecommerce.ipynb

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import ipywidgets as widgets
from IPython.display import display

# Configuración
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (15, 8)

# Conectar a PostgreSQL
engine = create_engine('postgresql://postgres:password@localhost:5432/ecommerce_analysis')

# Widgets interactivos
segmento_widget = widgets.Dropdown(
    options=['Todos', 'Consumer', 'Corporate', 'Home Office'],
    value='Todos',
    description='Segmento:'
)

def actualizar_dashboard(segmento):
    # Consulta dinámica
    if segmento == 'Todos':
        query = """
        SELECT 
            DATE_TRUNC('month', fecha_orden) AS mes,
            COUNT(DISTINCT order_id) AS num_ordenes,
            SUM(total) AS ingresos,
            AVG(total) AS ticket_promedio
        FROM ordenes
        GROUP BY mes
        ORDER BY mes
        """
    else:
        query = f"""
        SELECT 
            DATE_TRUNC('month', o.fecha_orden) AS mes,
            COUNT(DISTINCT o.order_id) AS num_ordenes,
            SUM(o.total) AS ingresos,
            AVG(o.total) AS ticket_promedio
        FROM ordenes o
        JOIN clientes c ON o.customer_id = c.customer_id
        WHERE c.segmento = '{segmento}'
        GROUP BY mes
        ORDER BY mes
        """
    
    df = pd.read_sql(query, engine)
    df['mes'] = pd.to_datetime(df['mes'])
    
    # Crear visualizaciones
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # Gráfico 1: Ingresos mensuales
    axes[0, 0].plot(df['mes'], df['ingresos'], marker='o', linewidth=2)
    axes[0, 0].set_title('Ingresos Mensuales', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('Mes')
    axes[0, 0].set_ylabel('Ingresos ($)')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Gráfico 2: Número de órdenes
    axes[0, 1].bar(df['mes'], df['num_ordenes'], color='steelblue', alpha=0.7)
    axes[0, 1].set_title('Número de Órdenes Mensuales', fontsize=14, fontweight='bold')
    axes[0, 1].set_xlabel('Mes')
    axes[0, 1].set_ylabel('Número de Órdenes')
    axes[0, 1].grid(True, alpha=0.3, axis='y')
    
    # Gráfico 3: Ticket promedio
    axes[1, 0].plot(df['mes'], df['ticket_promedio'], marker='s', color='green', linewidth=2)
    axes[1, 0].set_title('Ticket Promedio Mensual', fontsize=14, fontweight='bold')
    axes[1, 0].set_xlabel('Mes')
    axes[1, 0].set_ylabel('Ticket Promedio ($)')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Gráfico 4: Resumen
    resumen = df[['ingresos', 'num_ordenes', 'ticket_promedio']].sum()
    axes[1, 1].barh(['Ingresos', 'Órdenes', 'Ticket'], 
                    [resumen['ingresos'], resumen['num_ordenes'], resumen['ticket_promedio']],
                    color=['#2ecc71', '#3498db', '#e74c3c'])
    axes[1, 1].set_title('Resumen Total', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f'../figures/dashboard_{segmento.lower()}.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return df

# Conectar widget a función
widgets.interactive(actualizar_dashboard, segmento=segmento_widget)
```

##### **PASO 5: Dashboard en Excel**
```python
# scripts/generar_dashboard_excel.py
import pandas as pd
from sqlalchemy import create_engine
from openpyxl import load_workbook
from openpyxl.chart import BarChart, LineChart, Reference

engine = create_engine('postgresql://postgres:password@localhost:5432/ecommerce_analysis')

# Consultas para diferentes hojas
queries = {
    'Resumen': """
        SELECT 
            COUNT(DISTINCT customer_id) AS total_clientes,
            COUNT(DISTINCT order_id) AS total_ordenes,
            SUM(total) AS ingresos_totales,
            AVG(total) AS ticket_promedio
        FROM ordenes
    """,
    'Ventas Mensuales': """
        SELECT 
            DATE_TRUNC('month', fecha_orden) AS mes,
            COUNT(*) AS num_ordenes,
            SUM(total) AS ingresos,
            AVG(total) AS ticket_promedio
        FROM ordenes
        GROUP BY mes
        ORDER BY mes
    """,
    'Por Segmento': """
        SELECT 
            c.segmento,
            COUNT(DISTINCT o.order_id) AS num_ordenes,
            SUM(o.total) AS ingresos,
            AVG(o.total) AS ticket_promedio
        FROM ordenes o
        JOIN clientes c ON o.customer_id = c.customer_id
        GROUP BY c.segmento
        ORDER BY ingresos DESC
    """,
    'Top Productos': """
        SELECT 
            p.nombre AS producto,
            p.categoria,
            SUM(oi.cantidad) AS unidades_vendidas,
            SUM(oi.subtotal) AS ingresos
        FROM order_items oi
        JOIN productos p ON oi.product_id = p.product_id
        GROUP BY p.product_id, p.nombre, p.categoria
        ORDER BY ingresos DESC
        LIMIT 20
    """
}

# Crear Excel
with pd.ExcelWriter('excel/dashboard_ecommerce.xlsx', engine='openpyxl') as writer:
    for nombre, query in queries.items():
        df = pd.read_sql(query, engine)
        df.to_excel(writer, sheet_name=nombre, index=False)

print("✅ Dashboard Excel creado: excel/dashboard_ecommerce.xlsx")
```

---

### 📙 NIVEL AVANZADO - Proyecto 3: Análisis Predictivo de Ventas

#### **Objetivo**: Demostrar análisis predictivo, ETL robusto y automatización

#### **Dataset Recomendado**:
- **Kaggle**: "Store Sales Time Series Forecasting"
- **UCI**: "Sales Transactions Dataset"

#### **Stack Completo**:
1. ✅ **PostgreSQL**: Optimización, vistas materializadas, particionado
2. ✅ **Python**: scikit-learn, feature engineering, pipelines
3. ✅ **Jupyter**: Análisis completo documentado
4. ✅ **Excel**: Reportes ejecutivos automatizados
5. ✅ **Git**: Workflow profesional con branches

---

### 📕 NIVEL EXTREMO - Proyecto 4: Sistema Completo End-to-End

#### **Objetivo**: Integrar todas las tecnologías en un proyecto completo

#### **Dataset Recomendado**:
- **Kaggle**: Dataset grande (1M+ registros)
- **Múltiples fuentes**: Integrar datos de diferentes orígenes

---

## 📋 CHECKLIST DE HABILIDADES POR TECNOLOGÍA

### ✅ PostgreSQL ⭐
- [ ] Instalación y configuración
- [ ] Crear bases de datos y tablas
- [ ] Consultas SELECT básicas y avanzadas
- [ ] JOINs (INNER, LEFT, RIGHT, FULL)
- [ ] Funciones de agregación (COUNT, SUM, AVG, MAX, MIN)
- [ ] GROUP BY y HAVING
- [ ] Window Functions (RANK, ROW_NUMBER, LAG, LEAD)
- [ ] CTEs (Common Table Expressions)
- [ ] Subconsultas
- [ ] Índices para optimización
- [ ] Vistas y vistas materializadas
- [ ] Importar/Exportar datos (COPY, pg_dump)
- [ ] Funciones de fecha y texto
- [ ] Particionado de tablas (nivel avanzado)

### ✅ Python (pandas, numpy)
- [ ] Leer datos (CSV, Excel, SQL, JSON)
- [ ] Exploración básica (head, tail, info, describe)
- [ ] Filtrado y selección (loc, iloc)
- [ ] Operaciones con DataFrames
- [ ] Groupby y agregaciones
- [ ] Merge y join de DataFrames
- [ ] Pivot tables
- [ ] Limpieza de datos (dropna, fillna, drop_duplicates)
- [ ] Transformación de datos (apply, map)
- [ ] Manejo de fechas (pd.to_datetime, dt accessor)
- [ ] Operaciones con numpy arrays
- [ ] Estadísticas descriptivas
- [ ] Visualización básica (matplotlib, seaborn)

### ✅ Jupyter
- [ ] Crear y organizar notebooks
- [ ] Usar Markdown para documentación
- [ ] Magic commands (%time, %%timeit, %matplotlib inline)
- [ ] Widgets interactivos
- [ ] Exportar a diferentes formatos (HTML, PDF)
- [ ] Organizar código en funciones y clases
- [ ] Documentar análisis paso a paso

### ✅ Excel / Sheets
- [ ] Fórmulas básicas y avanzadas
- [ ] Funciones de búsqueda (VLOOKUP, INDEX/MATCH, XLOOKUP)
- [ ] Funciones lógicas (IF, AND, OR, IFERROR)
- [ ] Funciones de texto y fecha
- [ ] Tablas dinámicas (Pivot Tables)
- [ ] Gráficos profesionales
- [ ] Power Query (Excel) - Importar y transformar
- [ ] Dashboards interactivos
- [ ] Exportar desde Python a Excel

### ✅ Git
- [ ] Inicializar repositorio
- [ ] Commits descriptivos
- [ ] Branches (crear, cambiar, fusionar)
- [ ] Trabajar con remotos (GitHub, GitLab)
- [ ] Pull y push
- [ ] Resolver conflictos
- [ ] .gitignore para Data Science
- [ ] README profesional

---

## 🎯 RECOMENDACIONES FINALES

### **Para Empezar**:
1. **Empieza con Kaggle** - Es la fuente más completa y fácil de usar
2. **Elige datasets pequeños primero** (10K-100K registros)
3. **Completa un proyecto end-to-end** antes de pasar al siguiente nivel
4. **Documenta TODO** - README, comentarios, notebooks explicativos

### **Para Impresionar**:
1. **Usa datos reales** - No solo datasets de ejemplo
2. **Muestra el proceso completo** - Desde descarga hasta visualización
3. **Optimiza tus queries** - Demuestra que entiendes performance
4. **Crea dashboards profesionales** - Tanto en Jupyter como Excel
5. **Versiona con Git** - Muestra que trabajas profesionalmente

### **Estructura de Proyecto Ideal**:
```
proyecto/
├── README.md              # Descripción completa
├── data/                  # Datos (en .gitignore)
├── sql/                   # Scripts SQL
├── notebooks/             # Análisis en Jupyter
├── scripts/               # Scripts Python
├── excel/                 # Reportes Excel
├── figures/               # Visualizaciones
└── .gitignore            # Excluir datos grandes
```

---

## 🔗 ENLACES ÚTILES

### **Fuentes de Datos**:
- Kaggle: https://www.kaggle.com/datasets
- UCI ML Repository: https://archive.ics.uci.edu/ml/index.php
- Data.gov: https://data.gov/
- Google Dataset Search: https://datasetsearch.research.google.com/
- Awesome Public Datasets: https://github.com/awesomedata/awesome-public-datasets

### **Documentación**:
- PostgreSQL: https://www.postgresql.org/docs/
- pandas: https://pandas.pydata.org/docs/
- numpy: https://numpy.org/doc/
- Jupyter: https://jupyter.org/documentation

### **Tutoriales**:
- PostgreSQL Tutorial: https://www.postgresqltutorial.com/
- pandas Tutorial: https://pandas.pydata.org/docs/getting_started/intro_tutorials/
- Real Python: https://realpython.com/

---

**Última actualización**: Diciembre 2024

**Nota**: Este documento se actualiza constantemente con nuevas fuentes de datos y proyectos.

