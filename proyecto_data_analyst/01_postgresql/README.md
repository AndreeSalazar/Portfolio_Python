# 📊 PostgreSQL - Bases de Datos SQL

## 🎯 Objetivo
Dominar PostgreSQL, la herramienta más importante para un Data Analyst.

## 📁 Archivos en esta carpeta

- `crear_base_datos.sql` - Script para crear base de datos de ejemplo
- `ejercicios.sql` - Ejercicios prácticos
- `consultas_utiles.sql` - Consultas comunes para análisis

## 🚀 Inicio Rápido

### 1. Conectar a PostgreSQL
```bash
# Usando psql
& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres

# O usando pgAdmin 4 (interfaz gráfica)
# Busca "pgAdmin 4" en el menú de inicio
```

### 2. Crear base de datos de práctica
```sql
CREATE DATABASE practica_data_analyst;
\c practica_data_analyst
```

### 3. Ejecutar scripts
```bash
# Desde PowerShell
& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -d practica_data_analyst -f crear_base_datos.sql
```

## 📚 Conceptos Clave

- SELECT, WHERE, JOIN
- GROUP BY, ORDER BY
- Funciones de agregación
- Window Functions
- CTEs (Common Table Expressions)

## ✅ Próximos Pasos

1. Ejecuta `crear_base_datos.sql`
2. Completa los ejercicios en `ejercicios.sql`
3. Practica con `consultas_utiles.sql`

