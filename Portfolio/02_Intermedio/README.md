# 📗 Portfolio - Nivel Intermedio (Enfoque Data Analyst)

Este nivel del portfolio está diseñado para mostrar **cómo trabajo como Data Analyst** en proyectos más complejos: conectando datos de negocio con métricas claras, modelos analíticos y entregables accionables para stakeholders.

## 🎯 Rol y Objetivos como Data Analyst

- **Traducir preguntas de negocio** en métricas, hipótesis y consultas de datos
- **Diseñar modelos de datos** y consultas SQL complejas (JOINs, CTEs, Window Functions)
- **Construir análisis estadísticos** que expliquen el rendimiento del negocio
- **Crear dashboards y reportes ejecutivos** para equipos comerciales y dirección
- **Integrar y preparar datos** desde múltiples fuentes (ETL básico en Python + SQL)

## 📁 Proyectos Incluidos (visión tipo CV / Portfolio)

Cada proyecto está pensado para que un reclutador o hiring manager pueda ver:
- **Contexto de negocio**
- **Preguntas que responde el análisis**
- **Responsabilidades como Data Analyst**
- **Entregables finales (SQL, notebooks, dashboards, reportes)**

---

### 1. Análisis de Performance de Vendedores

**Rol como Data Analyst**: Responsable de definir métricas de rendimiento, construir el modelo de datos en SQL y preparar un dashboard para dirección comercial.

**Contexto de negocio**  
- Empresa con equipo de ventas distribuido por zonas/regiones  
- Necesidad de **medir performance por vendedor, región y producto**  
- Identificar outliers (top performers y vendedores con bajo rendimiento)

**Preguntas que responde el análisis**:
- ¿Qué vendedores generan mayor facturación y margen?  
- ¿Cómo evoluciona el rendimiento por periodo (mes/trimestre)?  
- ¿Qué regiones requieren acciones de mejora o acompañamiento?  
- ¿Qué productos impulsan el mejor rendimiento?

**Tecnologías (stack Data Analyst)**:
- PostgreSQL: JOINs complejos, Window Functions, CTEs
- Python: `pandas` avanzado, análisis estadístico descriptivo
- Jupyter: creación de reportes exploratorios y dashboard interactivo
- Excel: resumen ejecutivo para negocio

**Entregables (esperados)**:
- `sql/performance_vendedores.sql` – consultas principales
- `notebooks/dashboard_vendedores.ipynb` – análisis + visualizaciones
- `scripts/analisis_rendimiento.py` – lógica analítica reproducible
- `figures/dashboard_vendedores.png` – vista del dashboard

**Habilidades demostradas**:
- Definición de KPIs de ventas y performance
- JOINs múltiples y modelado relacional para reporting
- Window Functions para rankings y comparaciones
- Visualizaciones orientadas a negocio (segmentación por vendedor / región)

---

### 2. Análisis de Tendencias Temporales

**Rol como Data Analyst**: Responsable de analizar **tendencias y estacionalidad** en las ventas para apoyar decisiones de planificación y presupuestos.

**Contexto de negocio**  
- Ventas con alta componente estacional (por meses, campañas, festivos)  
- Necesidad de entender **qué periodos son pico/bajo** y cómo cambian año a año

**Preguntas que responde el análisis**:
- ¿Cómo evolucionan las ventas mes a mes y año a año?  
- ¿Existen patrones estacionales claros (por ejemplo, Q4 más fuerte)?  
- ¿Qué campañas o periodos generan mejores resultados?  
- ¿Qué escenario base se puede usar para pronósticos simples?

**Tecnologías**:
- PostgreSQL: funciones de fecha avanzadas, agregaciones temporales
- Python: `pandas` time series (re-sample, rolling windows, etc.)
- Jupyter: narración del análisis completo (EDA + insights)

**Entregables (esperados)**:
- `sql/tendencias_temporales.sql`
- `notebooks/analisis_temporal.ipynb`

**Habilidades demostradas**:
- Análisis de series temporales a nivel negocio (no técnico puro)
- Detección y comunicación de tendencias y estacionalidad
- Comparaciones año a año y por periodo
- Pronósticos básicos y escenarios simples para negocio

---

### 3. Dashboard Interactivo de Ventas

**Rol como Data Analyst**: Diseño y construcción de un **dashboard interactivo** para que managers puedan explorar ventas sin necesidad de código.

**Contexto de negocio**  
- Stakeholders necesitan una **vista única y clara de las ventas**  
- Requieren filtros por periodo, región, producto y canal

**Preguntas que responde el análisis**:
- ¿Cuál es la evolución de ventas por periodo y segmento?  
- ¿Qué productos y canales aportan más al revenue?  
- ¿Qué combinaciones región–producto–canal son más rentables?

**Tecnologías**:
- Python: `plotly`, `dash` para visualizaciones y apps analíticas
- Jupyter: prototipado rápido de gráficos y lógica
- Excel: versión resumida del dashboard para compartirse fácilmente

**Entregables (esperados)**:
- `notebooks/dashboard_interactivo.ipynb`
- `scripts/crear_dashboard.py`

**Habilidades demostradas**:
- Diseño de dashboards profesionales para negocio
- Visualizaciones interactivas y filtros
- Integración de múltiples tablas/fuentes en una sola vista
- Exportación y comunicación de resultados a diferentes audiencias

---

### 4. ETL Básico: Integración de Datos

**Rol como Data Analyst**: Diseñar y ejecutar un **pipeline ETL sencillo** para unificar información de distintas fuentes en una base de datos analítica.

**Contexto de negocio**  
- Datos dispersos en varios archivos (e-commerce, marketing, etc.)  
- Necesidad de una **fuente única de verdad (single source of truth)** para análisis

**Preguntas que responde el análisis**:
- ¿Cómo integrar datos de distintas fuentes de forma consistente?  
- ¿Qué transformaciones son necesarias para análisis de ventas y marketing?  
- ¿Cómo asegurar calidad mínima de datos (tipos, nulos, claves, etc.)?

**Tecnologías**:
- Python: `pandas`, `SQLAlchemy` para ETL simple
- PostgreSQL: carga masiva y modelado de tablas analíticas
- Scripts automatizados: tareas repetibles

**Entregables (esperados)**:
- `scripts/etl_pipeline.py`
- `sql/schema_integracion.sql`

**Habilidades demostradas**:
- Extracción de datos desde múltiples fuentes
- Limpieza y transformación orientadas a análisis
- Carga en base de datos y modelado básico
- Automatización mínima para procesos recurrentes

---

## 🚀 Cómo Ejecutar (flujo de trabajo típico de Data Analyst)

### Requisitos adicionales

```bash
pip install plotly dash openpyxl
```

### Preparar TODOS los datos en PostgreSQL (una sola vez)

1. Asegúrate de tener PostgreSQL ejecutándose en tu máquina  
   - Usuario: `postgres`  
   - Contraseña: `123456`  
   - Base de datos creada: `portfolio_intermedio`
2. Desde la carpeta `02_Intermedio`, ejecuta:

```bash
python scripts/cargar_datos_postgresql.py
```

Esto creará/actualizará las tablas:
- `ecom_customers`, `ecom_orders`, `ecom_order_items`, `ecom_products`
- `marketing_analytics`
- `online_retail`

Y dejará todo listo para ejecutar SQL y notebooks.

### Flujo recomendado por proyecto

1. **Preparar datos**  
   - Cargar CSVs de `data/`  
   - Crear o actualizar tablas en PostgreSQL (con el script de arriba)
2. **Ejecutar consultas SQL**  
   - Probar y validar consultas en los archivos `.sql`  
   - Guardar vistas/tablas intermedias si es necesario
3. **Analizar en Jupyter**  
   - Abrir notebooks y reproducir el análisis paso a paso  
   - Ajustar filtros, periodos y parámetros de negocio
4. **Generar entregables para negocio**  
   - Exportar gráficos, tablas y resúmenes a Excel / imágenes  
   - Documentar conclusiones y recomendaciones

---

## ✅ Checklist de Habilidades Intermedias (Data Analyst)

- [x] Traducción de preguntas de negocio en KPIs y métricas
- [x] JOINs múltiples y complejos
- [x] Window Functions (RANK, ROW_NUMBER, LAG, LEAD)
- [x] CTEs y subconsultas complejas
- [x] Análisis estadísticos descriptivos y comparativos
- [x] Visualizaciones interactivas orientadas a negocio
- [x] Integración de múltiples fuentes de datos (ETL básico)
- [x] Documentación y comunicación de resultados

---

## 📊 Resultados Esperados por Proyecto

Cada proyecto del nivel intermedio debe incluir:
- ✅ Consultas SQL optimizadas y bien documentadas
- ✅ Análisis estadísticos y de negocio claros
- ✅ Visualizaciones o dashboards listos para stakeholders
- ✅ Documentación técnica y funcional (qué se hizo y por qué)
- ✅ Conclusiones accionables y recomendaciones concretas

---

**Nivel**: Intermedio – Data Analyst Profesional
