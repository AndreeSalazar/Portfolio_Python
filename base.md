# Guía de Tecnologías para Data Analyst Jr

## PostgreSQL ⭐

### Versión Actual
- **PostgreSQL 18.1** (lanzada en noviembre de 2024)
- Versión estable recomendada: **PostgreSQL 16.x** o superior

### Descarga e Instalación Completa

#### Paso 1: Acceder al Sitio Oficial
1. Visita la página oficial de descargas: **https://www.postgresql.org/download/**
2. Selecciona tu sistema operativo (Windows, macOS, Linux)

#### Paso 2: Descarga para Windows
1. **Opción Recomendada - Instalador de EnterpriseDB**:
   - Ve a: https://www.postgresql.org/download/windows/
   - Haz clic en "Download the installer"
   - Serás redirigido a: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
   - Selecciona la versión más reciente (PostgreSQL 18.x o 16.x)
   - Elige la arquitectura: **64-bit** (para la mayoría de sistemas modernos)
   - Descarga el instalador `.exe` (aproximadamente 200-300 MB)

2. **Componentes Incluidos en el Instalador**:
   - ✅ Servidor PostgreSQL
   - ✅ pgAdmin 4 (herramienta gráfica de administración)
   - ✅ Stack Builder (para instalar extensiones adicionales)
   - ✅ Command Line Tools (psql, pg_dump, etc.)
   - ✅ PostgreSQL JDBC Driver
   - ✅ Npgsql (driver .NET)

#### Paso 3: Instalación en Windows
1. **Ejecutar el Instalador**:
   - Haz doble clic en el archivo `.exe` descargado
   - Si aparece UAC (Control de Cuentas de Usuario), haz clic en "Sí"

2. **Asistente de Instalación**:
   - **Bienvenida**: Haz clic en "Next"
   - **Directorio de Instalación**: 
     - Por defecto: `C:\Program Files\PostgreSQL\18` (o versión correspondiente)
     - Puedes dejarlo por defecto o cambiar la ruta
   - **Componentes a Instalar**:
     - ✅ PostgreSQL Server (obligatorio)
     - ✅ pgAdmin 4 (recomendado)
     - ✅ Stack Builder (opcional, útil para extensiones)
     - ✅ Command Line Tools (recomendado)
     - ✅ Dev Drivers (opcional, para desarrollo)
   - **Directorio de Datos**: 
     - Por defecto: `C:\Program Files\PostgreSQL\18\data`
     - Recomendado: Cambiar a `C:\PostgreSQL\data` (más fácil de acceder)
   - **Contraseña del Superusuario (postgres)**:
     - ⚠️ **IMPORTANTE**: Guarda esta contraseña en un lugar seguro
     - Usa una contraseña segura (mínimo 8 caracteres)
     - Ejemplo: `Postgres2024!` (pero usa una propia)
   - **Puerto**:
     - Por defecto: `5432` (déjalo así a menos que tengas conflicto)
   - **Configuración Regional**:
     - Locale: `Spanish, Spain` o `English, United States`
   - **Preparación para Instalar**: Revisa la configuración y haz clic en "Next"
   - **Instalación**: Espera a que se complete (5-10 minutos)
   - **Stack Builder**: Opcional, puedes cerrarlo si no lo necesitas ahora

#### Paso 4: Verificar la Instalación

**Método 1: Usando psql (línea de comandos)**
```bash
# Abrir PowerShell o CMD
# Navegar a la carpeta bin de PostgreSQL
cd "C:\Program Files\PostgreSQL\18\bin"

# Conectar a PostgreSQL
psql -U postgres

# Ingresar la contraseña que configuraste
# Deberías ver: postgres=#
```

**Método 2: Usando pgAdmin 4 (interfaz gráfica)**
1. Busca "pgAdmin 4" en el menú de inicio de Windows
2. Abre pgAdmin 4
3. Ingresa la contraseña del superusuario cuando se solicite
4. Deberías ver el servidor PostgreSQL conectado

**Método 3: Verificar el Servicio**
```bash
# En PowerShell (como Administrador)
Get-Service -Name postgresql*

# Debería mostrar el servicio como "Running"
```

#### Paso 5: Configuración Inicial

**Crear tu primera base de datos**:
```sql
-- Conectarse a PostgreSQL
psql -U postgres

-- Crear base de datos de prueba
CREATE DATABASE mi_base_datos;

-- Conectarse a la nueva base de datos
\c mi_base_datos

-- Crear una tabla de prueba
CREATE TABLE prueba (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos de prueba
INSERT INTO prueba (nombre) VALUES ('Test 1'), ('Test 2');

-- Consultar datos
SELECT * FROM prueba;
```

#### Enlaces Directos de Descarga

**Windows 64-bit (Versión más reciente)**:
- PostgreSQL 18.x: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
- PostgreSQL 16.x (LTS): https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

**Alternativas**:
- **PostgreSQL Portable**: Para uso sin instalación
- **Docker**: `docker pull postgres:18` (si usas Docker)
- **Chocolatey**: `choco install postgresql` (si usas Chocolatey)

#### Solución de Problemas Comunes

**Error: "Puerto 5432 ya está en uso"**
```bash
# Verificar qué proceso usa el puerto
netstat -ano | findstr :5432

# Detener el servicio si es necesario
net stop postgresql-x64-18
```

**Error: "No se puede conectar al servidor"**
- Verifica que el servicio esté ejecutándose: `services.msc` → Buscar "postgresql"
- Verifica el firewall de Windows
- Revisa que el puerto 5432 esté abierto

**Olvidaste la contraseña del superusuario**:
1. Edita el archivo `pg_hba.conf` (en la carpeta `data`)
2. Cambia `md5` a `trust` temporalmente
3. Reinicia el servicio
4. Conéctate sin contraseña y cambia la contraseña
5. Restaura `md5` en `pg_hba.conf`

#### Recursos Adicionales
- **Documentación de Instalación**: https://www.postgresql.org/docs/current/installation.html
- **Guía de Inicio Rápido**: https://www.postgresql.org/docs/current/tutorial.html
- **Foro de Soporte**: https://www.postgresql.org/support/

### Conceptos Fundamentales
- **Instalación y configuración básica**
- **Comandos SQL esenciales**: SELECT, WHERE, JOIN, GROUP BY, ORDER BY
- **Funciones de agregación**: COUNT, SUM, AVG, MAX, MIN
- **Subconsultas y CTEs (Common Table Expressions)**
- **Window Functions**: ROW_NUMBER(), RANK(), DENSE_RANK(), LAG(), LEAD()
- **Índices**: Creación y optimización de consultas
- **Vistas y funciones**
- **Importación/Exportación de datos**: COPY, pg_dump, pg_restore

### Comandos Útiles para Data Analyst
```sql
-- Conectar a base de datos
\c nombre_base_datos

-- Listar tablas
\dt

-- Describir estructura de tabla
\d nombre_tabla

-- Ver esquemas
\dn

-- Exportar resultado a CSV
\copy (SELECT * FROM tabla) TO 'archivo.csv' CSV HEADER;
```

### Recursos de Aprendizaje
- Documentación oficial: https://www.postgresql.org/docs/
- PostgreSQL Tutorial: https://www.postgresqltutorial.com/

---

## Python (pandas, numpy)

### pandas
**Biblioteca principal para análisis de datos estructurados**

#### Conceptos Clave
- **DataFrames y Series**: Estructuras de datos fundamentales
- **Lectura de datos**: `read_csv()`, `read_excel()`, `read_sql()`
- **Exploración de datos**: `head()`, `tail()`, `info()`, `describe()`, `shape`
- **Filtrado y selección**: `loc[]`, `iloc[]`, condiciones booleanas
- **Manipulación de datos**:
  - `groupby()`: Agrupaciones y agregaciones
  - `merge()` / `join()`: Combinación de DataFrames
  - `pivot_table()`: Tablas dinámicas
  - `melt()`: Transformación de datos
- **Limpieza de datos**:
  - `dropna()`, `fillna()`: Manejo de valores faltantes
  - `drop_duplicates()`: Eliminar duplicados
  - `astype()`: Conversión de tipos
- **Funciones de agregación**: `sum()`, `mean()`, `count()`, `agg()`
- **Aplicación de funciones**: `apply()`, `map()`, `applymap()`
- **Manejo de fechas**: `pd.to_datetime()`, `dt` accessor

#### Ejemplo Básico
```python
import pandas as pd

# Leer datos
df = pd.read_csv('datos.csv')

# Explorar
print(df.head())
print(df.info())
print(df.describe())

# Filtrar y agrupar
resultado = df[df['columna'] > 100].groupby('categoria')['valor'].sum()
```

### numpy
**Biblioteca para operaciones numéricas y arrays multidimensionales**

#### Conceptos Clave
- **Arrays**: Creación y manipulación de arrays
- **Operaciones matemáticas**: Suma, resta, multiplicación, división
- **Funciones estadísticas**: `mean()`, `std()`, `median()`, `percentile()`
- **Operaciones de array**: `reshape()`, `transpose()`, `flatten()`
- **Indexación y slicing**: Acceso a elementos
- **Operaciones vectorizadas**: Más eficientes que loops
- **Generación de datos**: `np.random`, `np.arange()`, `np.linspace()`

#### Ejemplo Básico
```python
import numpy as np

# Crear array
arr = np.array([1, 2, 3, 4, 5])

# Operaciones estadísticas
print(np.mean(arr))
print(np.std(arr))
print(np.median(arr))
```

### Instalación
```bash
pip install pandas numpy
```

---

## Jupyter

### Conceptos Fundamentales
- **Jupyter Notebooks**: Archivos `.ipynb` para análisis interactivos
- **Celdas**: Código, Markdown, Raw
- **Kernels**: Entornos de ejecución (Python, R, etc.)
- **Magic Commands**: Comandos especiales (`%time`, `%%timeit`, `%matplotlib inline`)

### Comandos Útiles
- **Ejecutar celda**: `Shift + Enter`
- **Insertar celda**: `A` (arriba), `B` (abajo)
- **Eliminar celda**: `DD` (doble D)
- **Modo comando**: `Esc`
- **Modo edición**: `Enter`

### Magic Commands Importantes
```python
%matplotlib inline          # Gráficos inline
%time                       # Tiempo de ejecución
%%timeit                    # Tiempo promedio múltiples ejecuciones
%load_ext autoreload        # Recargar módulos automáticamente
%autoreload 2
!                           # Ejecutar comandos shell
```

### Instalación
```bash
pip install jupyter
jupyter notebook
# o
pip install jupyterlab
jupyter lab
```

### Extensiones Útiles
- **JupyterLab**: Interfaz moderna
- **nbconvert**: Convertir notebooks a otros formatos
- **ipywidgets**: Widgets interactivos

---

## Excel / Google Sheets

### Excel
**Herramienta esencial para análisis y visualización**

#### Funciones Clave para Data Analyst
- **Funciones de búsqueda**: VLOOKUP, HLOOKUP, XLOOKUP, INDEX/MATCH
- **Funciones lógicas**: IF, AND, OR, IFERROR
- **Funciones de texto**: LEFT, RIGHT, MID, CONCATENATE, TEXT
- **Funciones de fecha**: TODAY, NOW, YEAR, MONTH, DAY, DATEDIF
- **Funciones estadísticas**: AVERAGE, MEDIAN, MODE, STDEV, COUNTIF, SUMIF
- **Tablas dinámicas (Pivot Tables)**: Análisis de datos multidimensional
- **Gráficos**: Creación y personalización
- **Power Query**: Importación y transformación de datos
- **Power Pivot**: Modelado de datos avanzado

#### Atajos Útiles
- `Ctrl + Shift + L`: Filtros automáticos
- `Alt + =`: AutoSum
- `Ctrl + T`: Crear tabla
- `F2`: Editar celda
- `Ctrl + ;`: Fecha actual

### Google Sheets
**Alternativa colaborativa en la nube**

#### Funciones Específicas
- **QUERY()**: Consultas tipo SQL
- **IMPORTRANGE()**: Importar datos de otras hojas
- **GOOGLEFINANCE()**: Datos financieros
- **ARRAYFORMULA()**: Fórmulas de array
- **VLOOKUP()**, **INDEX/MATCH()**: Búsquedas
- **Pivot Tables**: Similar a Excel

#### Ventajas
- Colaboración en tiempo real
- Acceso desde cualquier dispositivo
- Integración con Google Workspace
- Historial de versiones

---

## Git

### Conceptos Fundamentales
- **Repositorio**: Directorio con control de versiones
- **Commit**: Snapshot del código en un momento específico
- **Branch**: Línea de desarrollo independiente
- **Merge**: Combinar cambios de diferentes branches
- **Remote**: Repositorio remoto (GitHub, GitLab, etc.)

### Comandos Esenciales

#### Configuración Inicial
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

#### Comandos Básicos
```bash
# Inicializar repositorio
git init

# Clonar repositorio existente
git clone <url>

# Ver estado
git status

# Agregar archivos al staging
git add <archivo>
git add .                    # Todos los archivos

# Hacer commit
git commit -m "Mensaje descriptivo"

# Ver historial
git log

# Crear y cambiar de branch
git branch <nombre_branch>
git checkout <nombre_branch>
# o
git checkout -b <nombre_branch>    # Crear y cambiar

# Fusionar branch
git merge <nombre_branch>

# Trabajar con remoto
git remote add origin <url>
git push origin <branch>
git pull origin <branch>
```

### Flujo de Trabajo Típico
1. `git pull` - Obtener cambios más recientes
2. Trabajar en el código
3. `git add .` - Agregar cambios
4. `git commit -m "descripción"` - Guardar cambios
5. `git push` - Subir cambios al remoto

### Buenas Prácticas
- **Commits descriptivos**: Mensajes claros sobre qué cambió
- **Commits frecuentes**: Pequeños y frecuentes mejor que grandes
- **Branching**: Usar branches para features nuevas
- **.gitignore**: Excluir archivos innecesarios (datos, notebooks con outputs grandes)

### Archivo .gitignore para Data Science
```
# Datos
*.csv
*.xlsx
*.json
!sample_data/*

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

---

## Stack Completo para Data Analyst Jr

### Flujo de Trabajo Típico
1. **Extracción**: PostgreSQL, APIs, archivos CSV/Excel
2. **Transformación**: Python (pandas, numpy) en Jupyter
3. **Análisis**: Exploración, visualización, modelado
4. **Presentación**: Excel/Sheets, Jupyter notebooks
5. **Control de Versiones**: Git para código y notebooks

### Recursos Adicionales
- **SQL**: Practicar en plataformas como LeetCode, HackerRank
- **Python**: Real Python, Python.org documentation
- **Visualización**: matplotlib, seaborn, plotly
- **Comunidades**: Stack Overflow, Reddit (r/datascience), Kaggle

---

## Checklist de Habilidades

### PostgreSQL
- [ ] Instalar y configurar PostgreSQL
- [ ] Escribir consultas SELECT complejas
- [ ] Usar JOINs (INNER, LEFT, RIGHT, FULL)
- [ ] Aplicar funciones de agregación
- [ ] Trabajar con Window Functions
- [ ] Crear y usar CTEs
- [ ] Importar/exportar datos

### Python (pandas/numpy)
- [ ] Leer datos de diferentes fuentes
- [ ] Explorar y limpiar datos
- [ ] Filtrar y transformar DataFrames
- [ ] Agrupar y agregar datos
- [ ] Combinar múltiples DataFrames
- [ ] Manejar valores faltantes
- [ ] Aplicar funciones personalizadas

### Jupyter
- [ ] Crear y organizar notebooks
- [ ] Usar Markdown para documentación
- [ ] Aplicar magic commands
- [ ] Visualizar datos inline
- [ ] Exportar notebooks a diferentes formatos

### Excel/Sheets
- [ ] Crear fórmulas complejas
- [ ] Usar funciones de búsqueda
- [ ] Crear tablas dinámicas
- [ ] Generar gráficos profesionales
- [ ] Usar Power Query (Excel)

### Git
- [ ] Inicializar repositorios
- [ ] Hacer commits descriptivos
- [ ] Trabajar con branches
- [ ] Colaborar con repositorios remotos
- [ ] Resolver conflictos básicos

---

*Última actualización: Diciembre 2024*

