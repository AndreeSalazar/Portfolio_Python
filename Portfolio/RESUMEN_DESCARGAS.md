# 📥 Resumen Completo de Descargas - Portfolio Data Analyst

Este documento resume TODOS los datasets descargados para el portfolio completo, organizados por nivel.

---

## 📊 Resumen General

| Nivel | Datasets | Tamaño Aproximado | Complejidad |
|-------|----------|-------------------|-------------|
| 📘 **Básico** | 3 datasets | ~100-500 MB | Baja |
| 📗 **Intermedio** | 3 datasets | ~500 MB - 2 GB | Media |
| 📙 **Avanzado** | 3 datasets | ~2-5 GB | Alta |
| 📕 **EXTREMO** | 3 datasets | ~5-20 GB | Muy Alta |
| **TOTAL** | **12 datasets** | **~10-30 GB** | - |

---

## 📘 NIVEL BÁSICO

### Dataset 1: Retail Sales Dataset
- **Fuente**: Kaggle
- **ID**: `rohitsahoo/sales-forecasting`
- **Ubicación**: `01_Basico/data/retail_sales/`
- **Tamaño**: ~50-100 MB
- **Registros**: ~50K-100K
- **Uso**: Análisis básico de ventas, JOINs simples, visualizaciones básicas

### Dataset 2: Superstore Sales Dataset
- **Fuente**: Kaggle
- **ID**: `vivek468/superstore-dataset-final`
- **Ubicación**: `01_Basico/data/superstore/`
- **Tamaño**: ~50-100 MB
- **Registros**: ~10K-50K
- **Uso**: Dashboards, análisis de profitabilidad, tablas dinámicas

### Dataset 3: HR Analytics Dataset
- **Fuente**: Kaggle
- **ID**: `arindam235/startup-investments-crunchbase`
- **Ubicación**: `01_Basico/data/hr_analytics/`
- **Tamaño**: ~20-50 MB
- **Registros**: ~15K
- **Uso**: Análisis de empleados, performance, rotación

**Total Nivel Básico**: ~120-250 MB

---

## 📗 NIVEL INTERMEDIO

### Dataset 1: E-commerce Customer Data
- **Fuente**: Kaggle
- **ID**: `carrie1/ecommerce-data`
- **Ubicación**: `02_Intermedio/data/ecommerce/`
- **Tamaño**: ~200-500 MB
- **Registros**: ~500K
- **Uso**: Análisis de cohortes, CLV, JOINs complejos, Window Functions

### Dataset 2: Online Retail Dataset (UCI)
- **Fuente**: UCI Machine Learning Repository
- **URL**: https://archive.ics.uci.edu/ml/datasets/Online+Retail
- **Ubicación**: `02_Intermedio/data/online_retail/`
- **Tamaño**: ~50-100 MB
- **Registros**: ~540K
- **Uso**: RFM Analysis, análisis temporal, detección de anomalías

### Dataset 3: Marketing Analytics Dataset
- **Fuente**: Kaggle
- **ID**: `datasnaek/marketing-analytics`
- **Ubicación**: `02_Intermedio/data/marketing/`
- **Tamaño**: ~100-200 MB
- **Registros**: ~100K-200K
- **Uso**: Análisis de campañas, ROI, segmentación, optimización

**Total Nivel Intermedio**: ~350-800 MB

---

## 📙 NIVEL AVANZADO

### Dataset 1: Brazilian E-commerce Dataset
- **Fuente**: Kaggle
- **ID**: `olistbr/brazilian-ecommerce`
- **Ubicación**: `03_Avanzado/data/brazilian_ecommerce/`
- **Tamaño**: ~500 MB - 2 GB
- **Registros**: ~100K órdenes, 1M+ items
- **Uso**: Análisis completo, optimización avanzada, ETL robusto, análisis predictivo

### Dataset 2: Store Sales Time Series Forecasting
- **Fuente**: Kaggle
- **ID**: `competitions/store-sales-time-series-forecasting`
- **Ubicación**: `03_Avanzado/data/store_sales/`
- **Tamaño**: ~1-3 GB
- **Registros**: ~1M+
- **Uso**: Forecasting, análisis de estacionalidad, modelos predictivos, optimización de inventario

### Dataset 3: Banking Dataset
- **Fuente**: Kaggle
- **ID**: `sriharipramod/bank-customer-data`
- **Ubicación**: `03_Avanzado/data/banking/`
- **Tamaño**: ~200-500 MB
- **Registros**: ~100K-500K
- **Uso**: Análisis de riesgo, detección de fraude, segmentación, churn analysis

**Total Nivel Avanzado**: ~1.7-5.5 GB

---

## 📕 NIVEL EXTREMO

### Dataset 1: Store Sales Time Series Forecasting (COMPLETO)
- **Fuente**: Kaggle
- **ID**: `competitions/store-sales-time-series-forecasting`
- **Ubicación**: `04_EXTREMO/data/store_sales_completo/`
- **Tamaño**: ~5-10 GB
- **Registros**: Múltiples millones
- **Uso**: Big Data analysis, forecasting avanzado, optimización extrema, particionado

### Dataset 2: Brazilian E-commerce (COMPLETO)
- **Fuente**: Kaggle
- **ID**: `olistbr/brazilian-ecommerce`
- **Ubicación**: `04_EXTREMO/data/brazilian_ecommerce_completo/`
- **Tamaño**: ~2-5 GB
- **Registros**: Múltiples millones
- **Uso**: Proyectos end-to-end, análisis a gran escala, optimización avanzada

### Dataset 3: YouTube Trending Dataset
- **Fuente**: Kaggle
- **ID**: `datasnaek/youtube-new`
- **Ubicación**: `04_EXTREMO/data/youtube_trending/`
- **Tamaño**: ~3-5 GB
- **Registros**: Múltiples millones
- **Uso**: Análisis de Big Data, predicción de viralidad, análisis de comportamiento

**Total Nivel EXTREMO**: ~10-20 GB

---

## 🚀 Cómo Descargar

### Opción 1: Descargar Todos (Recomendado)
```bash
python Portfolio/scripts/descargar_todos_datasets.py
```

### Opción 2: Descargar por Nivel
```bash
# Nivel Básico
python Portfolio/scripts/descargar_basico.py

# Nivel Intermedio
python Portfolio/scripts/descargar_intermedio.py

# Nivel Avanzado
python Portfolio/scripts/descargar_avanzado.py

# Nivel EXTREMO
python Portfolio/scripts/descargar_extremo.py
```

### Opción 3: Descarga Manual
1. Revisa los README.md en cada carpeta `data/`
2. Descarga manualmente desde Kaggle/UCI
3. Coloca los archivos en las carpetas correspondientes

---

## 📋 Requisitos Previos

### Software Necesario
- ✅ Python 3.7+
- ✅ pip install kaggle pandas requests
- ✅ Cuenta de Kaggle (gratuita)
- ✅ Archivo `kaggle.json` configurado

### Configuración de Kaggle
1. Crear cuenta en https://www.kaggle.com/
2. Ir a Account → API → Create New API Token
3. Descargar `kaggle.json`
4. Colocar en:
   - Windows: `C:\Users\tu-usuario\.kaggle\kaggle.json`
   - Linux/Mac: `~/.kaggle/kaggle.json`
5. Permisos (Linux/Mac): `chmod 600 ~/.kaggle/kaggle.json`

### Espacio en Disco
- **Mínimo recomendado**: 30 GB libres
- **Ideal**: 50+ GB libres
- Los datasets EXTREMOS requieren más espacio

---

## 📁 Estructura de Carpetas

```
Portfolio/
├── 01_Basico/
│   └── data/
│       ├── README.md
│       ├── retail_sales/
│       ├── superstore/
│       └── hr_analytics/
├── 02_Intermedio/
│   └── data/
│       ├── README.md
│       ├── ecommerce/
│       ├── online_retail/
│       └── marketing/
├── 03_Avanzado/
│   └── data/
│       ├── README.md
│       ├── brazilian_ecommerce/
│       ├── store_sales/
│       └── banking/
└── 04_EXTREMO/
    └── data/
        ├── README.md
        ├── store_sales_completo/
        ├── brazilian_ecommerce_completo/
        └── youtube_trending/
```

---

## ✅ Checklist de Descarga

### Antes de Descargar
- [ ] Python instalado y funcionando
- [ ] Kaggle API instalada (`pip install kaggle`)
- [ ] Cuenta de Kaggle creada
- [ ] `kaggle.json` configurado correctamente
- [ ] Espacio en disco suficiente (30+ GB)
- [ ] Conexión a internet estable

### Durante la Descarga
- [ ] Ejecutar script de descarga
- [ ] Verificar que las carpetas se crean correctamente
- [ ] Monitorear el progreso de descarga
- [ ] Verificar que no hay errores

### Después de Descargar
- [ ] Verificar que los archivos están en las carpetas correctas
- [ ] Revisar los README.md de cada nivel
- [ ] Probar cargar un dataset pequeño en Python
- [ ] Verificar que los archivos no están corruptos

---

## 🔧 Solución de Problemas

### Error: "Kaggle API no disponible"
```bash
pip install kaggle
```

### Error: "Authentication failed"
- Verifica que `kaggle.json` esté en la ubicación correcta
- Verifica que el archivo tenga el formato correcto
- Regenera el token desde Kaggle si es necesario

### Error: "Out of disk space"
- Libera espacio en disco
- Descarga solo los niveles necesarios
- Considera usar almacenamiento externo

### Error: "Connection timeout"
- Verifica tu conexión a internet
- Intenta descargar de nuevo
- Considera descargar manualmente desde Kaggle

### Datasets muy grandes
- Usa los scripts de procesamiento en chunks
- Considera usar muestreo para análisis exploratorio
- Optimiza PostgreSQL con índices y particionado

---

## 📝 Notas Importantes

1. **Tiempo de Descarga**: 
   - Básico: 5-15 minutos
   - Intermedio: 15-30 minutos
   - Avanzado: 30-60 minutos
   - EXTREMO: 1-3 horas (dependiendo de conexión)

2. **Procesamiento**:
   - Los datasets grandes requieren procesamiento en chunks
   - Usa índices en PostgreSQL para optimizar
   - Considera muestreo para análisis exploratorio

3. **Almacenamiento**:
   - Los datasets están en `.gitignore` por defecto
   - No subas datasets grandes a Git
   - Usa Git LFS si necesitas versionar datos

4. **Documentación**:
   - Cada nivel tiene su README.md con detalles
   - Consulta `FUENTES_DATOS_Y_PROYECTOS.md` para guías completas
   - Revisa `DATASETS_RECOMENDADOS.md` para más información

---

## 🔗 Enlaces Útiles

- **Kaggle**: https://www.kaggle.com/datasets
- **UCI Repository**: https://archive.ics.uci.edu/ml/index.php
- **Documentación Portfolio**: `FUENTES_DATOS_Y_PROYECTOS.md`
- **Guía de Datasets**: `DATASETS_RECOMENDADOS.md`
- **Resumen Ejecutivo**: `RESUMEN_EJECUTIVO.md`

---

## 📊 Estadísticas Finales

- **Total de Datasets**: 12
- **Total de Niveles**: 4
- **Tamaño Total Estimado**: 10-30 GB
- **Tiempo Total de Descarga**: 1-4 horas (dependiendo de conexión)
- **Stack Tecnológico Cubierto**: PostgreSQL, Python, Jupyter, Excel, Git

---

**Última actualización**: Diciembre 2024

**Nota**: Este documento se actualiza cuando se agregan nuevos datasets o se modifican los existentes.

