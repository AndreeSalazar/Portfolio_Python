# 📊 Datasets - Basic Level

This folder contains datasets used for basic level projects.

## 📦 Included Datasets

### 1. Retail Sales Dataset
**Source**: Kaggle  
**ID**: `rohitsahoo/sales-forecasting`  
**Folder**: `retail_sales/`

**Description**:
- Real retail sales data.
- Multiple dimensions (time, product, region, customer).
- Size: ~50K-100K records.
- Perfect for basic and intermediate analysis.

**Expected Structure**:
- `ventas.csv`: date, product_id, quantity, total, region
- `productos.csv`: product_id, name, category, price
- `clientes.csv`: customer_id, name, city, segment

**Use in Projects**:
- Sales analysis by region/month.
- Product performance.
- Seasonal trend analysis.
- Customer segmentation.

---

### 2. Superstore Sales Dataset
**Source**: Kaggle  
**ID**: `vivek468/superstore-dataset-final`  
**Folder**: `superstore/`

**Description**:
- Very popular supermarket/retail dataset.
- Multiple dimensions.
- Perfect for dashboards.

**Expected Structure**:
- `Superstore.xlsx` or `Superstore.csv`
- Columns: Order ID, Order Date, Ship Date, Customer Name, Segment, Country, City, State, Region, Product ID, Category, Sub-Category, Product Name, Sales, Quantity, Discount, Profit

**Use in Projects**:
- Full sales dashboard.
- Profitability analysis.
- Product segmentation.
- Trend analysis.

---

### 3. HR Analytics Dataset
**Source**: Kaggle  
**ID**: `arindam235/startup-investments-crunchbase`  
**Folder**: `hr_analytics/`

**Description**:
- Human Resources data.
- Employee analysis and performance.
- Size: ~15K records.
- Perfect for business analysis.

**Expected Structure**:
- CSV files with employee information.
- Columns: Employee ID, Department, Position, Salary, Performance, etc.

**Use in Projects**:
- Employee turnover analysis.
- Performance by department.
- Satisfaction analysis.
- Resignation prediction.

---

## 🚀 How to Use These Datasets

### Step 1: Verify Download
```bash
# Verify that datasets are downloaded
ls -la Portfolio/01_Basico/data/
```

### Step 2: Explore Data
```python
import pandas as pd

# Load dataset
df = pd.read_csv('data/retail_sales/file.csv')
print(df.head())
print(df.info())
```

### Step 3: Load to PostgreSQL
```python
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:password@localhost:5432/retail_analysis')
df.to_sql('ventas', engine, if_exists='replace', index=False)
```
