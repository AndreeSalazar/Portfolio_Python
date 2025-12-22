# 📚 Guía Completa de Descargas - Portfolio Data Analyst

Esta guía explica TODO el sistema de descarga de datasets creado para el portfolio completo.

---

## 🎯 Objetivo

Descargar **TODOS** los datasets necesarios para demostrar el stack completo de Data Analyst Jr en los 4 niveles:
- 📘 Básico
- 📗 Intermedio  
- 📙 Avanzado
- 📕 EXTREMO

**Total: 12 datasets (~30 GB)**

---

## 📁 Archivos Creados

### Scripts de Descarga

1. **`scripts/descargar_todos_datasets.py`** ⭐ PRINCIPAL
   - Script maestro que descarga TODOS los datasets
   - Incluye función para crear estructura de carpetas
   - Manejo de errores y resumen final
   - Descarga de Kaggle y URLs directas

2. **`scripts/descargar_basico.py`**
   - Descarga solo datasets del nivel básico (3 datasets)

3. **`scripts/descargar_intermedio.py`**
   - Descarga solo datasets del nivel intermedio (3 datasets)

4. **`scripts/descargar_avanzado.py`**
   - Descarga solo datasets del nivel avanzado (3 datasets)
   - Incluye advertencia sobre tamaño

5. **`scripts/descargar_extremo.py`**
   - Descarga solo datasets del nivel EXTREMO (3 datasets)
   - Requiere confirmación explícita por tamaño

### Documentación

6. **`RESUMEN_DESCARGAS.md`** ⭐
   - Resumen completo de todos los datasets
   - Tabla resumen por nivel
   - Instrucciones detalladas
   - Solución de problemas

7. **`INICIO_RAPIDO.md`** ⭐
   - Guía rápida de 3 pasos
   - Comandos esenciales
   - Verificación rápida

8. **`01_Basico/data/README.md`**
   - Descripción de datasets básicos
   - Instrucciones de uso
   - Ejemplos de código

9. **`02_Intermedio/data/README.md`**
   - Descripción de datasets intermedios
   - Instrucciones de uso
   - Ejemplos avanzados

10. **`03_Avanzado/data/README.md`**
    - Descripción de datasets avanzados
    - Instrucciones de optimización
    - Ejemplos de Big Data

11. **`04_EXTREMO/data/README.md`**
    - Descripción de datasets EXTREMOS
    - Instrucciones de procesamiento en chunks
    - Optimización extrema

---

## 🚀 Cómo Usar

### Opción 1: Descargar Todo (Recomendado)

```bash
# 1. Instalar dependencias
pip install kaggle pandas requests

# 2. Configurar Kaggle (ver INICIO_RAPIDO.md)

# 3. Ejecutar descarga completa
python Portfolio/scripts/descargar_todos_datasets.py
```

**Tiempo estimado**: 2-4 horas (dependiendo de conexión)

### Opción 2: Descargar por Nivel

```bash
# Nivel Básico (5-15 min)
python Portfolio/scripts/descargar_basico.py

# Nivel Intermedio (15-30 min)
python Portfolio/scripts/descargar_intermedio.py

# Nivel Avanzado (30-60 min)
python Portfolio/scripts/descargar_avanzado.py

# Nivel EXTREMO (1-3 horas)
python Portfolio/scripts/descargar_extremo.py
```

### Opción 3: Descarga Manual

1. Revisar `RESUMEN_DESCARGAS.md` para lista completa
2. Ir a Kaggle/UCI y descargar manualmente
3. Colocar archivos en carpetas correspondientes

---

## 📊 Datasets por Nivel

### 📘 Nivel Básico (3 datasets, ~250 MB)

1. **Retail Sales Dataset**
   - ID: `rohitsahoo/sales-forecasting`
   - Ubicación: `01_Basico/data/retail_sales/`

2. **Superstore Sales Dataset**
   - ID: `vivek468/superstore-dataset-final`
   - Ubicación: `01_Basico/data/superstore/`

3. **HR Analytics Dataset**
   - ID: `arindam235/startup-investments-crunchbase`
   - Ubicación: `01_Basico/data/hr_analytics/`

### 📗 Nivel Intermedio (3 datasets, ~800 MB)

1. **E-commerce Customer Data**
   - ID: `carrie1/ecommerce-data`
   - Ubicación: `02_Intermedio/data/ecommerce/`

2. **Online Retail Dataset (UCI)**
   - URL: UCI Repository
   - Ubicación: `02_Intermedio/data/online_retail/`

3. **Marketing Analytics**
   - ID: `datasnaek/marketing-analytics`
   - Ubicación: `02_Intermedio/data/marketing/`

### 📙 Nivel Avanzado (3 datasets, ~5 GB)

1. **Brazilian E-commerce**
   - ID: `olistbr/brazilian-ecommerce`
   - Ubicación: `03_Avanzado/data/brazilian_ecommerce/`

2. **Store Sales Time Series**
   - ID: `competitions/store-sales-time-series-forecasting`
   - Ubicación: `03_Avanzado/data/store_sales/`

3. **Banking Dataset**
   - ID: `sriharipramod/bank-customer-data`
   - Ubicación: `03_Avanzado/data/banking/`

### 📕 Nivel EXTREMO (3 datasets, ~20 GB)

1. **Store Sales Time Series (COMPLETO)**
   - ID: `competitions/store-sales-time-series-forecasting`
   - Ubicación: `04_EXTREMO/data/store_sales_completo/`

2. **Brazilian E-commerce (COMPLETO)**
   - ID: `olistbr/brazilian-ecommerce`
   - Ubicación: `04_EXTREMO/data/brazilian_ecommerce_completo/`

3. **YouTube Trending**
   - ID: `datasnaek/youtube-new`
   - Ubicación: `04_EXTREMO/data/youtube_trending/`

---

## 🔧 Configuración Requerida

### 1. Python y Dependencias
```bash
pip install kaggle pandas requests
```

### 2. Cuenta de Kaggle
1. Crear cuenta en https://www.kaggle.com/
2. Ir a Account → API → Create New API Token
3. Descargar `kaggle.json`

### 3. Configurar kaggle.json
- **Windows**: `C:\Users\tu-usuario\.kaggle\kaggle.json`
- **Linux/Mac**: `~/.kaggle/kaggle.json`
- **Permisos (Linux/Mac)**: `chmod 600 ~/.kaggle/kaggle.json`

### 4. Espacio en Disco
- **Mínimo**: 30 GB libres
- **Recomendado**: 50+ GB libres

---

## 📋 Estructura de Carpetas Creada

```
Portfolio/
├── scripts/
│   ├── descargar_todos_datasets.py ⭐
│   ├── descargar_basico.py
│   ├── descargar_intermedio.py
│   ├── descargar_avanzado.py
│   ├── descargar_extremo.py
│   └── descargar_datos_kaggle.py
├── 01_Basico/
│   └── data/
│       ├── README.md
│       ├── retail_sales/ (se crea al descargar)
│       ├── superstore/ (se crea al descargar)
│       └── hr_analytics/ (se crea al descargar)
├── 02_Intermedio/
│   └── data/
│       ├── README.md
│       ├── ecommerce/ (se crea al descargar)
│       ├── online_retail/ (se crea al descargar)
│       └── marketing/ (se crea al descargar)
├── 03_Avanzado/
│   └── data/
│       ├── README.md
│       ├── brazilian_ecommerce/ (se crea al descargar)
│       ├── store_sales/ (se crea al descargar)
│       └── banking/ (se crea al descargar)
└── 04_EXTREMO/
    └── data/
        ├── README.md
        ├── store_sales_completo/ (se crea al descargar)
        ├── brazilian_ecommerce_completo/ (se crea al descargar)
        └── youtube_trending/ (se crea al descargar)
```

---

## ✅ Checklist de Verificación

### Antes de Ejecutar
- [ ] Python 3.7+ instalado
- [ ] Dependencias instaladas (`pip install kaggle pandas requests`)
- [ ] Cuenta de Kaggle creada
- [ ] `kaggle.json` configurado correctamente
- [ ] Espacio en disco suficiente (30+ GB)
- [ ] Conexión a internet estable

### Después de Ejecutar
- [ ] Verificar que las carpetas se crearon
- [ ] Verificar que los archivos están en las carpetas correctas
- [ ] Revisar los README.md de cada nivel
- [ ] Probar cargar un dataset pequeño en Python
- [ ] Verificar que no hay errores en los archivos

---

## 🔍 Solución de Problemas

### Error: "Kaggle API no disponible"
```bash
pip install kaggle
```

### Error: "Authentication failed"
- Verificar ubicación de `kaggle.json`
- Regenerar token desde Kaggle
- Verificar formato del archivo JSON

### Error: "Out of disk space"
- Liberar espacio en disco
- Descargar solo niveles necesarios
- Usar almacenamiento externo

### Error: "Connection timeout"
- Verificar conexión a internet
- Intentar de nuevo
- Descargar manualmente desde Kaggle

### Datasets muy grandes
- Usar procesamiento en chunks (ver READMEs de cada nivel)
- Considerar muestreo para análisis exploratorio
- Optimizar PostgreSQL con índices

---

## 📚 Documentación Relacionada

- **Inicio Rápido**: `INICIO_RAPIDO.md`
- **Resumen Completo**: `RESUMEN_DESCARGAS.md`
- **Fuentes de Datos**: `FUENTES_DATOS_Y_PROYECTOS.md`
- **Datasets Recomendados**: `DATASETS_RECOMENDADOS.md`
- **Resumen Ejecutivo**: `RESUMEN_EJECUTIVO.md`
- **README Principal**: `README.md`

---

## 💡 Próximos Pasos Después de Descargar

1. ✅ **Verificar descargas**: Revisar que todos los archivos estén presentes
2. 📖 **Leer READMEs**: Revisar documentación de cada nivel
3. 🗄️ **Configurar PostgreSQL**: Seguir guía en `base.md`
4. 🐍 **Cargar datos**: Usar scripts de ejemplo en `FUENTES_DATOS_Y_PROYECTOS.md`
5. 📊 **Empezar análisis**: Crear notebooks en Jupyter
6. 📈 **Crear visualizaciones**: Generar gráficos y dashboards
7. 📝 **Documentar**: Incluir READMEs y comentarios

---

## 🎯 Resumen Ejecutivo

**Sistema completo creado para**:
- ✅ Descargar 12 datasets organizados por nivel
- ✅ Scripts automatizados para descarga
- ✅ Documentación completa de cada dataset
- ✅ Guías paso a paso para uso
- ✅ Solución de problemas común

**Total de archivos creados**: 11 archivos
- 5 scripts de descarga
- 6 documentos de guía y resumen

**Total de datasets**: 12 datasets
- 3 básicos (~250 MB)
- 3 intermedios (~800 MB)
- 3 avanzados (~5 GB)
- 3 extremos (~20 GB)

**Tiempo total de descarga**: 2-4 horas (dependiendo de conexión)

---

**¡Sistema completo y listo para usar!** 🎉

**Última actualización**: Diciembre 2024

