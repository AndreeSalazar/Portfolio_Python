# 📙 Portfolio - Nivel Avanzado (Data Analyst Senior)

Este nivel está diseñado para mostrar **cómo trabajas como Data Analyst en un contexto casi de producción**: arquitectura de datos profesional, análisis de negocio end-to-end, modelos predictivos y automatización de reporting para dirección.

## 🎯 Rol y objetivos como Data Analyst (Nivel Avanzado)

- **Liderar el análisis de negocio completo** desde la definición de objetivos hasta conclusiones estratégicas
- **Diseñar arquitectura de datos** pensada para reporting, análisis avanzado y escalabilidad
- **Construir pipelines ETL robustos** para grandes volúmenes de datos (e-commerce, banca, series temporales)
- **Desarrollar modelos predictivos básicos–intermedios** orientados a negocio (no solo a precisión)
- **Automatizar dashboards y reportes ejecutivos** que consumen datos actualizados desde la base de datos

## 📁 Proyectos Incluidos (visión Data Analyst Senior)

Cada proyecto se describe pensando en lo que un recruiter / hiring manager quiere ver:
- **Contexto de negocio**
- **Preguntas que responde el análisis**
- **Responsabilidades como Data Analyst**
- **Entregables (SQL, scripts ETL, notebooks, dashboards, reportes)**

---

### 1. Sistema de Análisis de Negocio Completo

**Rol como Data Analyst**: Responsable del **diseño del modelo de datos**, optimización de consultas y creación de un flujo de análisis que conecte datos crudos con reportes ejecutivos.

**Contexto de negocio**  
- Negocio digital (e-commerce/banca) con múltiples fuentes y tablas (órdenes, clientes, productos, vendedores, geolocalización)  
- Necesidad de una **vista única y confiable** para dirección (ventas, margen, performance por segmento, geografía, canal)

**Preguntas clave de negocio**:
- ¿Cuáles son los principales drivers de revenue y margen?  
- ¿Qué segmentos (cliente, producto, región, canal) son más rentables?  
- ¿Cómo cambia el rendimiento a lo largo del tiempo y entre unidades de negocio?  
- ¿Qué métricas deben ver los directivos cada semana/mes?

**Tecnologías**:
- PostgreSQL: optimización avanzada, índices, vistas materializadas
- Python: arquitectura modular de scripts ETL robustos
- Jupyter: análisis de negocio documentado de punta a punta
- Excel / reporting: reportes ejecutivos automáticos para stakeholders
- Git: control de versiones del código analítico

**Archivos (esperados)**:
- `sql/optimizacion_queries.sql`
- `sql/schema_profesional.sql`
- `scripts/etl_robusto.py`
- `notebooks/analisis_completo.ipynb`
- `scripts/generar_reportes.py`

**Habilidades demostradas**:
- Diseño de **modelo analítico** sobre datasets grandes (`brazilian_ecommerce`, `store_sales`, `banking`)
- Optimización de queries (índices, vistas materializadas, particionado cuando aplique)
- ETL robusto en Python (procesamiento por chunks, control de errores)
- Generación de reportes ejecutivos recurrentes
- Documentación técnica y funcional del flujo de datos

---

### 2. Análisis Predictivo Aplicado al Negocio

**Rol como Data Analyst**: Construir modelos predictivos que aporten **valor accionable** (no solo métricas de ML), y explicar sus resultados a negocio.

**Contexto de negocio**  
- Series temporales de ventas (`store_sales`) o riesgo/segmentación de clientes (`banking`)  
- Necesidad de **anticipar resultados futuros** (ventas, demanda, probabilidad de churn, riesgo) para planificación

**Preguntas clave**:
- ¿Qué variables explican mejor el comportamiento (ventas, churn, riesgo)?  
- ¿Qué resultados esperamos en los próximos periodos bajo escenarios base?  
- ¿Qué segmentos presentan mayor riesgo / mayor potencial?

**Tecnologías**:
- PostgreSQL: almacenamiento y preparación de históricos optimizados
- Python: `scikit-learn`, `statsmodels` para modelos de regresión / clasificación básicos
- Jupyter: desarrollo, validación y explicación de modelos

**Archivos (esperados)**:
- `notebooks/modelo_predictivo.ipynb`
- `scripts/entrenar_modelo.py`
- `figures/predicciones.png`

**Habilidades demostradas**:
- Preparación de datos para ML (features, tratamientos de nulos, escalado si aplica)
- Modelos de regresión y/o clasificación con enfoque de negocio
- Validación de modelos (train/test split, métricas adecuadas)
- Interpretación y comunicación de resultados a stakeholders

---

### 3. Dashboard Ejecutivo Automatizado

**Rol como Data Analyst**: Diseñar un **dashboard ejecutivo** que se alimente automáticamente de la base de datos y exponga KPIs clave sin intervención manual.

**Contexto de negocio**  
- Dirección necesita una vista **siempre actualizada** de ventas, margen, churn, riesgo o KPIs principales  
- Se busca reducir trabajo manual de reporting y asegurar consistencia en cifras

**Preguntas clave**:
- ¿Qué indicadores debe ver la dirección cada mañana?  
- ¿Cómo automatizar la actualización de datos y reportes?  
- ¿Qué cortes (tiempo, región, canal, producto, segmento cliente) son imprescindibles?

**Tecnologías**:
- Python: `Dash` o `Streamlit` para el dashboard, `schedule`/task scheduler para automatización
- PostgreSQL: vistas materializadas y consultas pre-optimiazadas
- Excel / PDF: exportación de reportes ejecutivos

**Archivos (esperados)**:
- `scripts/dashboard_ejecutivo.py`
- `scripts/actualizar_automatico.py`
- `excel/reporte_ejecutivo.xlsx`

**Habilidades demostradas**:
- Diseño de dashboards a nivel dirección (no solo gráficos sueltos)
- Automatización de procesos de actualización
- Definición y seguimiento de KPIs de negocio
- Exportación y distribución profesional de reportes

---

### 4. Análisis de Cohortes, Retención y Lifetime Value

**Rol como Data Analyst**: Liderar el análisis de **retención de clientes y LTV**, clave para decisiones de inversión en marketing y producto.

**Contexto de negocio**  
- Negocio con base de clientes recurrentes (e-commerce/banca)  
- Interés en entender **cuánto tiempo se quedan los clientes** y **cuánto valor generan** a lo largo de su ciclo de vida

**Preguntas clave**:
- ¿Cómo evolucionan las cohortes de clientes en el tiempo?  
- ¿Qué segmentos retienen mejor y por qué?  
- ¿Cuál es el Lifetime Value estimado por segmento/canal?  
- ¿Dónde conviene invertir para retener y dónde dejar de invertir?

**Tecnologías**:
- PostgreSQL: queries complejas de cohortes, retención y LTV
- Python: análisis y visualización de cohortes y métricas de retención
- Jupyter: narración analítica y visualización

**Archivos (esperados)**:
- `sql/analisis_cohortes.sql`
- `notebooks/retencion_clientes.ipynb`

**Habilidades demostradas**:
- Diseño de cohortes y métricas de retención/LTV
- Interpretación de patrones de retención
- Visualizaciones avanzadas para explicar comportamiento de clientes
- Conexión de métricas de retención con decisiones de negocio

---

## 🚀 Cómo Ejecutar (flujo típico en nivel avanzado)

### Requisitos avanzados (Python)

```bash
pip install scikit-learn statsmodels dash streamlit schedule openpyxl
```

### Flujo recomendado

1. **ETL y carga de datos**  
   - Usar scripts ETL (`scripts/etl_robusto.py`, etc.) para cargar datasets grandes de `data/` a PostgreSQL  
   - Ver `data/README.md` para detalles de cada dataset (`brazilian_ecommerce`, `store_sales`, `banking`)
2. **Optimización de base de datos**  
   - Ejecutar `sql/schema_profesional.sql` y `sql/optimizacion_queries.sql`  
   - Crear índices y vistas materializadas clave
3. **Análisis en notebooks**  
   - `notebooks/analisis_completo.ipynb`, `modelo_predictivo.ipynb`, `retencion_clientes.ipynb`  
   - Documentar hipótesis, pasos y resultados
4. **Dashboards y automatización**  
   - Ejecutar el dashboard (`scripts/dashboard_ejecutivo.py`)  
   - Configurar tareas automáticas (`scripts/actualizar_automatico.py`)
5. **Reportes y comunicación**  
   - Generar `excel/reporte_ejecutivo.xlsx` y otros artefactos  
   - Redactar conclusiones estratégicas y recomendaciones

---

## ✅ Checklist de Habilidades Avanzadas (Data Analyst Senior)

- [x] Diseño de arquitectura de datos profesional
- [x] Optimización de queries complejas en PostgreSQL
- [x] ETL robusto y escalable con Python
- [x] Modelado predictivo básico–intermedio aplicado a negocio
- [x] Automatización de procesos y reporting
- [x] Dashboards ejecutivos para dirección
- [x] Análisis de cohortes, retención y LTV
- [x] Documentación técnica y de negocio de nivel profesional

---

## 📊 Resultados Esperados

Cada proyecto avanzado debe incluir:
- ✅ Arquitectura clara y escalable (modelo de datos + ETL + optimización)
- ✅ Código optimizado, modular y mantenible
- ✅ Análisis profundos de negocio con foco en decisiones
- ✅ Automatización de dashboards y reportes clave
- ✅ Documentación técnica y funcional bien escrita
- ✅ Conclusiones estratégicas y recomendaciones accionables

---

**Nivel**: Avanzado – Data Analyst en entorno de Producción
