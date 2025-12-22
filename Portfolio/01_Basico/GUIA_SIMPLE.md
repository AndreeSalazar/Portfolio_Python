# 📘 Guía Simple - Nivel Básico

## 🚀 Pasos Rápidos

### 1. Instalar dependencias
```bash
pip install pandas numpy matplotlib seaborn sqlalchemy openpyxl psycopg2-binary jupyter
```

### 2. Crear base de datos PostgreSQL
```sql
CREATE DATABASE retail_analysis_basico;
\c retail_analysis_basico
```
Luego ejecuta: `sql/schema_basico.sql`

### 3. Cargar datos
```bash
python scripts/cargar_datos_postgresql.py
```

### 4. Abrir notebook
```bash
jupyter notebook notebooks/analisis_completo_basico.ipynb
```

### 5. Ejecutar celdas en orden

---

## 📁 Estructura

- `data/` - Datos CSV
- `sql/` - Scripts SQL
- `scripts/` - Scripts Python
- `notebooks/` - Notebooks Jupyter
- `figures/` - Gráficos generados
- `excel/` - Reportes Excel

---

## ⚠️ Problema de Encoding

Si tienes errores de encoding, usa:
```bash
python scripts/cargar_datos_simple.py
```

Este script usa psycopg2 directamente y maneja el encoding correctamente.

---

## ✅ Checklist

- [ ] PostgreSQL instalado y ejecutándose
- [ ] Base de datos creada
- [ ] Datos cargados
- [ ] Notebook ejecutado
- [ ] Visualizaciones generadas

---

**¡Listo para empezar!** 🎉

