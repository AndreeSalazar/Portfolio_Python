# 📓 Jupyter Notebooks

Esta carpeta es para tus Jupyter Notebooks de análisis.

## 🎯 Propósito

Los notebooks son perfectos para:
- Análisis exploratorios de datos
- Presentar análisis de forma clara
- Combinar código, visualizaciones y explicaciones
- Compartir resultados con otros

## 🚀 Inicio Rápido

### 1. Instalar Jupyter
```bash
pip install jupyter notebook
```

### 2. Iniciar Jupyter
```bash
# Desde la raíz del proyecto
jupyter notebook

# O desde esta carpeta
cd notebooks
jupyter notebook
```

### 3. Crear tu primer notebook
1. Haz clic en "New" → "Python 3"
2. Importa las librerías necesarias
3. Carga datos desde `../data/` o PostgreSQL
4. Realiza tu análisis
5. Guarda en esta carpeta

## 📁 Estructura Recomendada

Crea notebooks con nombres descriptivos:
- `01_exploracion_datos.ipynb` - Exploración inicial
- `02_limpieza_datos.ipynb` - Limpieza y transformación
- `03_analisis_ventas.ipynb` - Análisis específico
- `04_visualizaciones.ipynb` - Gráficos y dashboards

## 💡 Tips

### Magic Commands Útiles
```python
%matplotlib inline          # Gráficos inline
%time                       # Tiempo de ejecución
%%timeit                    # Tiempo promedio
%load_ext autoreload        # Recargar módulos
%autoreload 2
```

### Cargar Datos
```python
# Desde CSV
import pandas as pd
df = pd.read_csv('../data/ventas.csv')

# Desde PostgreSQL
from sqlalchemy import create_engine
engine = create_engine('postgresql://user:pass@localhost/db')
df = pd.read_sql('SELECT * FROM ventas', engine)
```

### Guardar Gráficos
```python
import matplotlib.pyplot as plt

# Crear gráfico
plt.figure(figsize=(10, 6))
# ... tu código de gráfico ...

# Guardar
plt.savefig('../figures/mi_grafico.png', dpi=300, bbox_inches='tight')
plt.show()
```

## 📚 Mejores Prácticas

1. **Organiza tu notebook**:
   - Markdown para explicaciones
   - Código bien comentado
   - Resultados claros

2. **Limpia outputs** antes de commit:
   - Cell → All Output → Clear

3. **Usa nombres descriptivos** para variables

4. **Exporta a diferentes formatos**:
   - HTML: `jupyter nbconvert notebook.ipynb --to html`
   - PDF: `jupyter nbconvert notebook.ipynb --to pdf`

## ✅ Checklist

- [ ] Jupyter instalado
- [ ] Primer notebook creado
- [ ] Datos cargados correctamente
- [ ] Gráficos guardados en `../figures/`
- [ ] Notebook documentado con Markdown

---

**¡Crea análisis increíbles con Jupyter!** 📊

