# 🚀 Inicio Rápido - Descarga de Datasets

Guía rápida para descargar todos los datasets del portfolio.

---

## ⚡ Inicio Rápido (4 Pasos)

### Paso 0: Verificar Configuración (NUEVO) ⭐
```bash
# Ejecutar script de verificación primero
python Portfolio/scripts/verificar_configuracion.py
```

Este script te dirá exactamente qué falta configurar.

### Paso 1: Instalar Dependencias
```bash
pip install kaggle pandas requests
```

### Paso 2: Configurar Kaggle

**Si el script de verificación detecta problemas, sigue esta guía:**
- **Guía completa**: `Portfolio/CONFIGURAR_KAGGLE.md` ⭐
- **Resumen rápido**:
  1. Crear cuenta en https://www.kaggle.com/
  2. Ir a Account → API → Create New API Token
  3. Descargar `kaggle.json`
  4. Colocar en: `C:\Users\tu-usuario\.kaggle\kaggle.json` (Windows)

### Paso 3: Ejecutar Descarga
```bash
# Verificar nuevamente que todo esté OK
python Portfolio/scripts/verificar_configuracion.py

# Descargar TODOS los datasets (recomendado)
python Portfolio/scripts/descargar_todos_datasets.py

# O descargar por nivel:
python Portfolio/scripts/descargar_basico.py
python Portfolio/scripts/descargar_intermedio.py
python Portfolio/scripts/descargar_avanzado.py
python Portfolio/scripts/descargar_extremo.py
```

---

## 📋 Resumen de Datasets

| Nivel | Datasets | Tamaño | Tiempo |
|-------|----------|--------|--------|
| 📘 Básico | 3 | ~250 MB | 5-15 min |
| 📗 Intermedio | 3 | ~800 MB | 15-30 min |
| 📙 Avanzado | 3 | ~5 GB | 30-60 min |
| 📕 EXTREMO | 3 | ~20 GB | 1-3 horas |
| **TOTAL** | **12** | **~30 GB** | **2-4 horas** |

---

## 📁 Estructura Después de Descargar

```
Portfolio/
├── 01_Basico/data/
│   ├── retail_sales/
│   ├── superstore/
│   └── hr_analytics/
├── 02_Intermedio/data/
│   ├── ecommerce/
│   ├── online_retail/
│   └── marketing/
├── 03_Avanzado/data/
│   ├── brazilian_ecommerce/
│   ├── store_sales/
│   └── banking/
└── 04_EXTREMO/data/
    ├── store_sales_completo/
    ├── brazilian_ecommerce_completo/
    └── youtube_trending/
```

---

## ✅ Verificación

Después de descargar, verifica:

```bash
# Verificar estructura
ls -R Portfolio/*/data/

# Verificar tamaño
du -sh Portfolio/*/data/
```

---

## 📚 Documentación Completa

- **Resumen Completo**: `RESUMEN_DESCARGAS.md`
- **Fuentes de Datos**: `FUENTES_DATOS_Y_PROYECTOS.md`
- **Datasets Recomendados**: `DATASETS_RECOMENDADOS.md`
- **Resumen Ejecutivo**: `RESUMEN_EJECUTIVO.md`

---

## 🔧 Solución Rápida de Problemas

### ❌ Error: "Could not find kaggle.json"

**Solución**:
1. Ejecutar script de verificación:
   ```bash
   python Portfolio/scripts/verificar_configuracion.py
   ```

2. Seguir guía completa:
   - `Portfolio/CONFIGURAR_KAGGLE.md` ⭐

3. Verificar manualmente (Windows PowerShell):
   ```powershell
   # Verificar que existe
   Test-Path "$env:USERPROFILE\.kaggle\kaggle.json"
   
   # Ver contenido
   Get-Content "$env:USERPROFILE\.kaggle\kaggle.json"
   ```

**Error de espacio en disco**:
- Libera espacio o descarga solo niveles necesarios

**Error de conexión**:
- Verifica internet y vuelve a intentar

**Otros errores**:
- Ejecutar: `python Portfolio/scripts/verificar_configuracion.py`
- Revisar: `Portfolio/CONFIGURAR_KAGGLE.md`

---

## 💡 Próximos Pasos

1. ✅ Datasets descargados
2. 📖 Revisar README.md de cada nivel
3. 🗄️ Configurar PostgreSQL
4. 🐍 Cargar datos con Python
5. 📊 Empezar análisis en Jupyter

---

**¡Listo para empezar!** 🎉

