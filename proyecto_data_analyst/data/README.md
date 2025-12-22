# 📁 Data - Datos y Datasets

Esta carpeta contiene todos los datos para tus análisis.

## 📊 Tipos de Datos

- **CSV**: Datos tabulares
- **JSON**: Datos estructurados
- **Excel**: Archivos .xlsx, .xls
- **SQL dumps**: Backups de bases de datos

## 🚀 Obtener Datos

### Desde PostgreSQL
```sql
-- Exportar tabla a CSV
\copy (SELECT * FROM ventas) TO '../data/ventas.csv' CSV HEADER;
\copy (SELECT * FROM productos) TO '../data/productos.csv' CSV HEADER;
```

### Desde Python
```python
import pandas as pd
from sqlalchemy import create_engine

# Conectar y exportar
engine = create_engine('postgresql://user:pass@localhost/db')
df = pd.read_sql('SELECT * FROM ventas', engine)
df.to_csv('data/ventas.csv', index=False)
```

### Descargar Datasets
- Kaggle: https://www.kaggle.com/datasets
- UCI ML Repository: https://archive.ics.uci.edu/
- Data.gov: https://data.gov/

## 📝 Organización

Organiza tus datos por proyecto o tipo:
```
data/
├── raw/              # Datos sin procesar
├── processed/        # Datos limpios
├── external/         # Datos externos
└── sample/           # Datos de ejemplo
```

## ⚠️ Importante

### Seguridad
- **NO subas datos sensibles** a Git
- Usa `.gitignore` para excluir archivos grandes
- Considera usar Git LFS para archivos grandes

### Tamaño
- Archivos pequeños (< 10MB): OK para Git
- Archivos grandes: Usa Git LFS o almacenamiento externo
- Datos de ejemplo: Mantén versiones pequeñas

## 🔒 .gitignore

Los siguientes tipos de archivos están ignorados por defecto:
- `*.csv` (excepto en `sample/`)
- `*.xlsx`, `*.xls`
- `*.json` (excepto en `sample/`)
- Archivos de backup

## 💡 Tips

1. **Mantén datos de ejemplo pequeños** para versionar
2. **Documenta la fuente** de tus datos
3. **Crea scripts** para generar datos de prueba
4. **Usa nombres descriptivos**: `ventas_2024.csv` mejor que `data.csv`

## ✅ Checklist

- [ ] Datos organizados por tipo/proyecto
- [ ] Datos de ejemplo documentados
- [ ] .gitignore configurado
- [ ] Scripts de exportación funcionando

---

**¡Mantén tus datos organizados!** 📊
