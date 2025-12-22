# 🐍 Python Scripts

Esta carpeta contiene scripts Python para análisis de datos usando pandas y numpy.

## 📁 Archivos

- **`ejemplo_pandas.py`** - Ejemplos completos de pandas
  - Creación de DataFrames
  - Lectura de datos
  - Exploración y filtrado
  - Agrupaciones y agregaciones
  - Manejo de valores faltantes
  - Combinación de DataFrames

- **`ejemplo_numpy.py`** - Ejemplos completos de numpy
  - Creación de arrays
  - Operaciones matemáticas
  - Funciones estadísticas
  - Indexación y slicing
  - Operaciones vectorizadas

- **`conectar_postgresql.py`** - Conectar Python con PostgreSQL
  - Dos métodos: psycopg2 y SQLAlchemy
  - Leer datos desde PostgreSQL
  - Escribir DataFrames a PostgreSQL
  - Funciones útiles para análisis

## 🚀 Uso

### 1. Instalar dependencias
```bash
pip install pandas numpy psycopg2-binary sqlalchemy
```

### 2. Ejecutar ejemplos
```bash
# Ejemplos básicos
python scripts/ejemplo_pandas.py
python scripts/ejemplo_numpy.py

# Conectar con PostgreSQL (actualiza credenciales primero)
python scripts/conectar_postgresql.py
```

### 3. Usar en tus propios scripts
```python
# Importar funciones útiles
import sys
sys.path.append('scripts')
from conectar_postgresql import conectar_sqlalchemy, leer_tabla_completa

# Usar en tu código
df, engine = conectar_sqlalchemy()
productos = leer_tabla_completa('productos', engine)
```

## 📚 Conceptos Cubiertos

### pandas
- ✅ DataFrames y Series
- ✅ Lectura de CSV, Excel, SQL
- ✅ Filtrado y selección
- ✅ Agrupaciones (groupby)
- ✅ Agregaciones
- ✅ Merge/Join
- ✅ Limpieza de datos

### numpy
- ✅ Arrays y operaciones
- ✅ Funciones estadísticas
- ✅ Operaciones vectorizadas
- ✅ Indexación avanzada

### PostgreSQL
- ✅ Conexión desde Python
- ✅ Lectura de datos
- ✅ Escritura de datos
- ✅ Ejecución de consultas

## 💡 Tips

- Usa `pd.read_sql()` para leer desde PostgreSQL
- Usa `df.to_sql()` para escribir a PostgreSQL
- Combina SQL y pandas para análisis potentes
- Guarda tus scripts personalizados aquí

---

**¡Combina SQL y Python para análisis poderosos!** 🚀

