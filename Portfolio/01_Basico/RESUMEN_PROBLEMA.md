# 🔍 Resumen del Problema de Encoding

## ❌ El Problema

El error `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xab` ocurre **durante la conexión** a PostgreSQL, antes de poder leer datos.

**Causa raíz**: PostgreSQL está enviando mensajes del servidor (información de versión, configuración, etc.) que contienen caracteres especiales que psycopg2 intenta leer como UTF-8 y falla.

## ✅ Solución Recomendada

### Recrear la Base de Datos con UTF-8

```sql
-- Conectar a PostgreSQL
psql -U postgres

-- Eliminar BD existente
DROP DATABASE retail_analysis_basico;

-- Crear nueva BD con UTF-8
CREATE DATABASE retail_analysis_basico 
WITH ENCODING 'UTF8' 
LC_COLLATE='en_US.UTF-8' 
LC_CTYPE='en_US.UTF-8' 
TEMPLATE=template0;

-- Conectarse a la nueva BD
\c retail_analysis_basico
```

Luego ejecuta el schema y carga los datos:
```bash
psql -U postgres -d retail_analysis_basico -f sql/schema_basico.sql
python scripts/cargar_datos_postgresql.py
```

## 🔄 Alternativa: Trabajar Directamente con CSV

Si el problema persiste, puedes trabajar directamente con los CSV sin PostgreSQL:

```python
import pandas as pd

# Cargar directamente desde CSV
df_ventas = pd.read_csv('data/retail_sales/ventas.csv')
df_productos = pd.read_csv('data/retail_sales/productos.csv')
df_clientes = pd.read_csv('data/retail_sales/clientes.csv')

# Continuar con el análisis normalmente
```

---

**Recomendación**: Recrea la BD con UTF-8 para evitar problemas futuros.

