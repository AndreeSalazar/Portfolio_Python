# ✅ Datos Sintéticos Generados - Portfolio Data Analyst

## 🎉 ¡Datos Listos para Usar!

Se han generado **datos sintéticos realistas** para demostrar el stack completo del portfolio.

---

## 📊 Resumen de Datos Generados

### 📘 Nivel Básico (3 datasets)

1. **Retail Sales Dataset**
   - `01_Basico/data/retail_sales/ventas.csv` - 5,000 registros
   - `01_Basico/data/retail_sales/productos.csv` - 5 productos
   - `01_Basico/data/retail_sales/clientes.csv` - 500 clientes
   - **Total**: ~5,500 registros

2. **Superstore Dataset**
   - `01_Basico/data/superstore/superstore.csv` - 3,000 registros
   - Columnas: Order ID, Order Date, Ship Date, Customer Name, Segment, Region, Product, Sales, Quantity, Discount, Profit

3. **HR Analytics Dataset**
   - `01_Basico/data/hr_analytics/hr_data.csv` - 1,500 registros
   - Columnas: employee_id, nombre, departamento, posicion, edad, salario, experiencia, performance_score

**Total Nivel Básico**: ~10,000 registros

---

### 📗 Nivel Intermedio (3 datasets)

1. **E-commerce Dataset**
   - `02_Intermedio/data/ecommerce/customers.csv` - 1,000 clientes
   - `02_Intermedio/data/ecommerce/products.csv` - 200 productos
   - `02_Intermedio/data/ecommerce/orders.csv` - 5,000 órdenes
   - `02_Intermedio/data/ecommerce/order_items.csv` - 12,394 items
   - **Total**: ~18,594 registros

2. **Online Retail Dataset**
   - `02_Intermedio/data/online_retail/online_retail.csv` - 10,000 registros
   - Columnas: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country

3. **Marketing Analytics Dataset**
   - `02_Intermedio/data/marketing/marketing_analytics.csv` - 2,000 registros
   - Columnas: campaign_id, fecha, canal, impresiones, clicks, conversiones, costo, revenue, roi

**Total Nivel Intermedio**: ~30,594 registros

---

### 📙 Nivel Avanzado (3 datasets)

1. **Brazilian E-commerce Dataset**
   - `03_Avanzado/data/brazilian_ecommerce/customers.csv` - 5,000 clientes
   - `03_Avanzado/data/brazilian_ecommerce/orders.csv` - 10,000 órdenes
   - `03_Avanzado/data/brazilian_ecommerce/order_items.csv` - 9,991 items
   - **Total**: ~24,991 registros

2. **Store Sales Time Series**
   - `03_Avanzado/data/store_sales/stores.csv` - 50 tiendas
   - `03_Avanzado/data/store_sales/train.csv` - 127,858 registros de ventas
   - **Total**: ~127,908 registros

3. **Banking Dataset**
   - `03_Avanzado/data/banking/banking_data.csv` - 5,000 registros
   - Columnas: customer_id, age, job, marital, education, balance, loan, etc.

**Total Nivel Avanzado**: ~157,899 registros

---

## 📈 Estadísticas Totales

- **Total de archivos CSV**: 20+ archivos
- **Total de registros**: ~200,000+ registros
- **Niveles completados**: 3 (Básico, Intermedio, Avanzado)
- **Tamaño aproximado**: ~50-100 MB

---

## 🚀 Cómo Usar Estos Datos

### 1. Cargar a PostgreSQL

```python
import pandas as pd
from sqlalchemy import create_engine

# Conectar a PostgreSQL
engine = create_engine('postgresql://postgres:password@localhost:5432/retail_analysis')

# Cargar datos
df = pd.read_csv('Portfolio/01_Basico/data/retail_sales/ventas.csv')
df.to_sql('ventas', engine, if_exists='replace', index=False)
```

### 2. Analizar con Python/Pandas

```python
import pandas as pd

# Cargar datos
df = pd.read_csv('Portfolio/01_Basico/data/retail_sales/ventas.csv')

# Explorar
print(df.head())
print(df.info())
print(df.describe())
```

### 3. Crear Notebooks en Jupyter

Los datos están listos para usar en Jupyter Notebooks. Crea notebooks en:
- `01_Basico/notebooks/`
- `02_Intermedio/notebooks/`
- `03_Avanzado/notebooks/`

### 4. Exportar a Excel

```python
df.to_excel('excel/reporte.xlsx', index=False)
```

---

## ✅ Ventajas de Estos Datos

1. **Listos para usar inmediatamente** - No necesitas configurar Kaggle
2. **Estructura realista** - Simulan datos reales de diferentes industrias
3. **Múltiples relaciones** - Perfectos para JOINs y análisis complejos
4. **Datos temporales** - Incluyen fechas para análisis de tendencias
5. **Tamaños variados** - Desde pequeños (básico) hasta grandes (avanzado)

---

## 📝 Notas Importantes

- Estos son datos **sintéticos** generados para demostración
- Son perfectos para practicar y demostrar habilidades
- Cuando tengas `kaggle.json` configurado, puedes descargar datos reales
- Los scripts funcionarán igual con datos reales de Kaggle

---

## 🔄 Próximos Pasos

1. ✅ **Datos generados** - Listo
2. 📖 **Revisar estructura** - Explora las carpetas `data/`
3. 🗄️ **Configurar PostgreSQL** - Cargar datos a base de datos
4. 📊 **Crear análisis** - Empezar con notebooks en Jupyter
5. 📈 **Generar visualizaciones** - Crear gráficos y dashboards
6. 📝 **Documentar proyectos** - Crear READMEs y documentación

---

## 🎯 Stack Completo Demostrable

Con estos datos puedes demostrar:

- ✅ **PostgreSQL**: Crear tablas, JOINs, Window Functions, CTEs
- ✅ **Python (pandas, numpy)**: ETL, análisis, transformaciones
- ✅ **Jupyter**: Notebooks documentados, dashboards interactivos
- ✅ **Excel**: Exportar resultados, tablas dinámicas, gráficos
- ✅ **Git**: Versionar código y notebooks

---

**¡Todo está listo para empezar a trabajar!** 🚀

**Última actualización**: Diciembre 2024

