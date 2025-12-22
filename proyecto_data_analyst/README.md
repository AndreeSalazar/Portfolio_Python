# 🚀 Data Analyst Project - Stack Profesional

Proyecto completo para dominar el stack de un Data Analyst Jr. con ejercicios prácticos y ejemplos listos para usar.

## 📁 Estructura del Proyecto

```
proyecto_data_analyst/
│── data/              # Datos de ejemplo y datasets
│── notebooks/         # Jupyter Notebooks para análisis
│── sql/               # Scripts SQL (PostgreSQL)
│── scripts/           # Scripts Python (pandas, numpy)
│── figures/           # Gráficos y visualizaciones
│── README.md          # Este archivo
│── falta.md           # Guía de instalación
```

## 🎯 Stack Tecnológico

1. **PostgreSQL** ⭐ - Bases de datos SQL (lo más importante)
2. **Python** - Especialmente pandas y numpy
3. **Jupyter Notebooks** - Presentar análisis claro
4. **Excel / Sheets** - Avanzado
5. **Git** - Versionado de código + GitHub como portfolio

## 🚀 Inicio Rápido

### 1. Instalar dependencias
```bash
# Ver falta.md para instrucciones completas
pip install pandas numpy jupyter psycopg2-binary sqlalchemy
```

### 2. PostgreSQL (SQL)
```bash
# Conectar a PostgreSQL
& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres

# Crear base de datos
CREATE DATABASE practica_data_analyst;

# Ejecutar scripts SQL
& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -d practica_data_analyst -f sql/crear_base_datos.sql
```

### 3. Python Scripts
```bash
# Ejecutar ejemplos
python scripts/ejemplo_pandas.py
python scripts/ejemplo_numpy.py
python scripts/conectar_postgresql.py
```

### 4. Jupyter Notebooks
```bash
# Iniciar Jupyter
jupyter notebook

# Abrir notebooks desde la carpeta notebooks/
```

### 5. Datos
- Los datos de ejemplo están en `data/`
- Exporta datos desde PostgreSQL a CSV para análisis
- Usa `data/` para tus propios datasets

### 6. Visualizaciones
- Guarda tus gráficos en `figures/`
- Formatos recomendados: PNG, PDF, SVG

## 📚 Contenido por Carpeta

### 📊 `sql/`
- `crear_base_datos.sql` - Script para crear BD de práctica
- `ejercicios.sql` - Ejercicios prácticos de SQL
- `consultas_utiles.sql` - Consultas comunes para análisis

### 🐍 `scripts/`
- `ejemplo_pandas.py` - Ejemplos de pandas
- `ejemplo_numpy.py` - Ejemplos de numpy
- `conectar_postgresql.py` - Conectar Python con PostgreSQL

### 📓 `notebooks/`
- Crea tus Jupyter Notebooks aquí
- Usa para análisis exploratorios y presentaciones

### 📁 `data/`
- Datos de ejemplo
- Datasets para práctica
- Exportaciones desde PostgreSQL

### 📈 `figures/`
- Gráficos y visualizaciones
- Imágenes de análisis
- Exportaciones de gráficos

## 🛠️ Configuración

### PostgreSQL
- **Versión**: 18.1
- **Puerto**: 5432 (por defecto)
- **Usuario**: postgres
- **Ruta psql**: `C:\Program Files\PostgreSQL\18\bin\psql.exe`

### Python
- **Versión**: 3.12.0
- **Paquetes requeridos**: Ver `falta.md`

## 📝 Flujo de Trabajo Recomendado

1. **Extracción**: Obtener datos desde PostgreSQL o archivos
2. **Transformación**: Usar SQL o Python (pandas) para limpiar datos
3. **Análisis**: Crear análisis en Jupyter Notebooks
4. **Visualización**: Generar gráficos y guardarlos en `figures/`
5. **Presentación**: Compartir resultados en Excel/Sheets o notebooks

## ✅ Checklist de Instalación

- [x] PostgreSQL 18.1 ✅ Instalado
- [x] Python 3.12.0 ✅ Instalado
- [x] numpy 2.3.5 ✅ Instalado
- [x] Git 2.52.0 ✅ Instalado
- [x] pandas ✅ Instalado
- [x] Jupyter ✅ Instalado
- [x] psycopg2-binary ✅ Instalado
- [x] sqlalchemy ✅ Instalado

## 📖 Recursos

- **PostgreSQL**: https://www.postgresql.org/docs/
- **pandas**: https://pandas.pydata.org/docs/
- **numpy**: https://numpy.org/doc/
- **Jupyter**: https://jupyter.org/documentation

## 🎯 Próximos Pasos

1. ✅ Revisa `falta.md` e instala lo que falta
2. ✅ Ejecuta `sql/crear_base_datos.sql` para crear datos de práctica
3. ✅ Prueba los scripts Python en `scripts/`
4. ✅ Crea tu primer notebook en `notebooks/`
5. ✅ Practica con los ejercicios en `sql/ejercicios.sql`

---

**¡Empieza ahora mismo!** 🎉

*Última actualización: Diciembre 2024*
