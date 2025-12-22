# 📊 SQL - PostgreSQL Scripts

Esta carpeta contiene todos los scripts SQL para trabajar con PostgreSQL.

## 📁 Archivos

- **`crear_base_datos.sql`** - Script completo para crear la base de datos de práctica
  - Crea tablas: ventas, productos, clientes, vendedores
  - Inserta datos de ejemplo
  - Incluye consultas de verificación

- **`ejercicios.sql`** - Ejercicios prácticos para aprender SQL
  - Consultas básicas
  - JOINs
  - Agregaciones
  - Window Functions
  - CTEs
  - Incluye soluciones comentadas

- **`consultas_utiles.sql`** - Consultas comunes para análisis
  - Exploración de datos
  - Estadísticas descriptivas
  - Análisis temporal
  - Análisis por categorías
  - Análisis geográfico
  - Análisis de clientes y vendedores
  - Exportación de datos

## 🚀 Uso

### 1. Crear la base de datos
```bash
# Conectar a PostgreSQL
& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres

# Crear base de datos
CREATE DATABASE practica_data_analyst;
\c practica_data_analyst
```

### 2. Ejecutar script de creación
```bash
# Desde PowerShell (en la raíz del proyecto)
& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -d practica_data_analyst -f sql/crear_base_datos.sql
```

### 3. Practicar con ejercicios
```bash
# Abrir psql
& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -d practica_data_analyst

# Copiar y pegar ejercicios desde ejercicios.sql
# O ejecutar desde archivo:
\i sql/ejercicios.sql
```

### 4. Usar consultas útiles
- Abre `consultas_utiles.sql` en tu editor
- Copia las consultas que necesites
- Modifica según tus necesidades

## 📚 Conceptos Cubiertos

- ✅ SELECT, WHERE, ORDER BY
- ✅ JOINs (INNER, LEFT, RIGHT, FULL)
- ✅ GROUP BY, HAVING
- ✅ Funciones de agregación (SUM, AVG, COUNT, etc.)
- ✅ Window Functions (RANK, ROW_NUMBER, LAG, LEAD)
- ✅ CTEs (Common Table Expressions)
- ✅ Funciones de fecha y tiempo
- ✅ Exportación de datos

## 💡 Tips

- Usa `\dt` para listar tablas
- Usa `\d nombre_tabla` para ver estructura de tabla
- Usa `\copy` para exportar a CSV
- Guarda tus consultas personalizadas aquí

---

**¡Practica mucho SQL!** Es la herramienta más importante para un Data Analyst. ⭐

