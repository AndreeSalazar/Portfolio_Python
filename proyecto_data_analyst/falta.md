# 📦 Instalación de Componentes Faltantes

Este archivo lista todo lo que necesitas instalar para completar el stack de Data Analyst.

## ✅ Estado Actual

- [x] **PostgreSQL 18.1** - ✅ Instalado y funcionando
- [x] **Python 3.12.0** - ✅ Instalado
- [x] **numpy 2.3.5** - ✅ Instalado
- [x] **Git 2.52.0** - ✅ Instalado
- [ ] **pandas** - ❌ Falta instalar
- [ ] **Jupyter** - ❌ Falta instalar
- [ ] **psycopg2-binary** - ❌ Falta instalar (para conectar Python con PostgreSQL)
- [ ] **sqlalchemy** - ❌ Falta instalar (para conectar Python con PostgreSQL)

## 🚀 Instalación Rápida

### Opción 1: Instalar todo de una vez
```bash
pip install pandas jupyter psycopg2-binary sqlalchemy
```

### Opción 2: Instalar uno por uno

#### 1. pandas
```bash
pip install pandas
```
**Verificar instalación:**
```bash
python -c "import pandas; print(pandas.__version__)"
```

#### 2. Jupyter
```bash
pip install jupyter notebook
```
**Verificar instalación:**
```bash
jupyter --version
```
**Iniciar Jupyter:**
```bash
jupyter notebook
```

#### 3. psycopg2-binary (conexión PostgreSQL)
```bash
pip install psycopg2-binary
```
**Verificar instalación:**
```bash
python -c "import psycopg2; print('psycopg2 instalado correctamente')"
```

#### 4. sqlalchemy (conexión PostgreSQL más fácil)
```bash
pip install sqlalchemy
```
**Verificar instalación:**
```bash
python -c "import sqlalchemy; print(sqlalchemy.__version__)"
```

## 📋 Comandos de Verificación

Ejecuta estos comandos para verificar que todo está instalado:

```bash
# Verificar Python
python --version

# Verificar pip
pip --version

# Verificar PostgreSQL
& "C:\Program Files\PostgreSQL\18\bin\psql.exe" --version

# Verificar Git
git --version

# Verificar paquetes Python instalados
pip list | Select-String -Pattern "pandas|numpy|jupyter|psycopg2|sqlalchemy"
```

## 🎯 Instalación Completa Recomendada

Para un entorno completo de Data Analyst, instala todo esto:

```bash
# Paquetes esenciales
pip install pandas numpy

# Jupyter y extensiones
pip install jupyter notebook jupyterlab

# Conexión con PostgreSQL
pip install psycopg2-binary sqlalchemy

# Visualización (opcional pero recomendado)
pip install matplotlib seaborn plotly

# Análisis estadístico (opcional)
pip install scipy scikit-learn

# Exportar a Excel (opcional)
pip install openpyxl xlsxwriter
```

## 📝 Notas Importantes

### PostgreSQL
- ✅ Ya está instalado (PostgreSQL 18.1)
- ⚠️ Recuerda tu contraseña del superusuario (postgres)
- 📍 Ruta: `C:\Program Files\PostgreSQL\18\`

### Python
- ✅ Ya está instalado (Python 3.12.0)
- ⚠️ Asegúrate de que `pip` esté actualizado:
  ```bash
  python -m pip install --upgrade pip
  ```

### Git
- ✅ Ya está instalado (Git 2.52.0)
- 📝 Configura tu identidad si no lo has hecho:
  ```bash
  git config --global user.name "Tu Nombre"
  git config --global user.email "tu@email.com"
  ```

## 🔧 Solución de Problemas

### Error: "pip no se reconoce"
```bash
python -m pip install nombre_paquete
```

### Error al instalar psycopg2
Si tienes problemas, usa la versión binary:
```bash
pip install psycopg2-binary
```

### Error al iniciar Jupyter
```bash
# Instalar con pip de usuario
pip install --user jupyter notebook

# O usar python -m
python -m pip install jupyter notebook
python -m jupyter notebook
```

### PostgreSQL no está en PATH
Agregar al PATH (PowerShell):
```powershell
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files\PostgreSQL\18\bin", "User")
```

## ✅ Checklist Final

Después de instalar todo, verifica:

- [ ] `python --version` funciona
- [ ] `pip list` muestra pandas, numpy, jupyter
- [ ] `jupyter notebook` inicia correctamente
- [ ] `python -c "import pandas; import numpy"` no da error
- [ ] `python -c "import psycopg2"` no da error
- [ ] `git --version` funciona
- [ ] PostgreSQL está corriendo (servicio activo)

## 🎉 ¡Listo para Empezar!

Una vez completada la instalación:

1. Ve a `proyecto_data_analyst/`
2. Lee el `README.md` principal
3. Empieza con `01_postgresql/`
4. Sigue el orden: PostgreSQL → Python → Jupyter → Excel → Git

---

**Última actualización:** Diciembre 2024

