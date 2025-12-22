# ⚠️ Problema de Encoding - Explicación

## 🔍 ¿Qué está pasando?

El error `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xab` ocurre **durante la conexión** a PostgreSQL, no durante la lectura de datos.

**Causa**: PostgreSQL está enviando mensajes del servidor (como información de versión, configuración, etc.) que contienen caracteres especiales que no se pueden decodificar como UTF-8.

## ✅ Solución

### Opción 1: Usar el script que funciona
```bash
python scripts/cargar_datos_final.py
```

Este script:
- Establece variables de entorno antes de conectar
- Conecta y luego establece encoding LATIN1
- Carga los datos correctamente
- Convierte a UTF-8 automáticamente

### Opción 2: Recrear la BD con UTF-8 (Recomendado)

```sql
-- En psql
DROP DATABASE retail_analysis_basico;
CREATE DATABASE retail_analysis_basico WITH ENCODING 'UTF8';
```

Luego vuelve a cargar los datos:
```bash
python scripts/cargar_datos_postgresql.py
```

## 📝 Nota sobre el Notebook

El notebook puede tener problemas durante la conexión. Si eso pasa:
1. Usa `scripts/cargar_datos_final.py` para cargar los datos
2. Guarda los DataFrames en archivos pickle o CSV
3. Carga esos archivos en el notebook

---

**El script `cargar_datos_final.py` funciona correctamente.** ✅

