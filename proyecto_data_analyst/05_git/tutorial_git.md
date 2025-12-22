# Tutorial de Git para Data Analyst

## 🎯 Objetivo
Aprender Git para versionar tus proyectos y crear un portfolio en GitHub.

## 📋 Configuración Inicial

### 1. Verificar instalación
```bash
git --version
```

### 2. Configurar identidad
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### 3. Ver configuración
```bash
git config --list
```

## 🚀 Flujo Básico de Trabajo

### 1. Inicializar repositorio
```bash
git init
```

### 2. Ver estado
```bash
git status
```

### 3. Agregar archivos
```bash
# Agregar archivo específico
git add archivo.py

# Agregar todos los archivos
git add .

# Agregar todos los archivos de un tipo
git add *.py
```

### 4. Hacer commit
```bash
git commit -m "Descripción clara de los cambios"
```

### 5. Ver historial
```bash
git log
git log --oneline  # Versión compacta
```

## 🌿 Trabajar con Branches

### Crear y cambiar de branch
```bash
# Crear nuevo branch
git branch nombre-branch

# Cambiar de branch
git checkout nombre-branch

# Crear y cambiar en un comando
git checkout -b nombre-branch
```

### Ver branches
```bash
git branch
git branch -a  # Ver todos incluyendo remotos
```

### Fusionar branches
```bash
# Cambiar a la branch principal
git checkout main

# Fusionar branch
git merge nombre-branch
```

## 🔄 Trabajar con GitHub

### 1. Crear repositorio en GitHub
- Ve a https://github.com
- Crea un nuevo repositorio
- Copia la URL

### 2. Conectar repositorio local con GitHub
```bash
# Agregar remote
git remote add origin https://github.com/tu-usuario/tu-repo.git

# Verificar
git remote -v
```

### 3. Subir cambios
```bash
# Primera vez
git branch -M main
git push -u origin main

# Siguientes veces
git push
```

### 4. Descargar cambios
```bash
git pull
```

## 📝 Comandos Útiles

### Ver diferencias
```bash
git diff
git diff archivo.py
```

### Deshacer cambios
```bash
# Deshacer cambios en archivo (antes de add)
git checkout -- archivo.py

# Deshacer add (mantener cambios)
git reset HEAD archivo.py

# Deshacer último commit (mantener cambios)
git reset --soft HEAD~1
```

### Clonar repositorio
```bash
git clone https://github.com/usuario/repo.git
```

## 🎨 Mejores Prácticas

### 1. Mensajes de commit claros
```bash
# ❌ Malo
git commit -m "cambios"

# ✅ Bueno
git commit -m "Agregar análisis de ventas mensuales"
git commit -m "Corregir cálculo de promedio en reporte"
```

### 2. Commits frecuentes y pequeños
- Mejor muchos commits pequeños que uno grande
- Facilita revisar cambios y deshacer si es necesario

### 3. Usar .gitignore
```bash
# Crear .gitignore
touch .gitignore

# Agregar archivos a ignorar
echo "*.csv" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".ipynb_checkpoints/" >> .gitignore
```

### 4. Branching strategy
- `main`: Código estable
- `develop`: Desarrollo activo
- `feature/nombre`: Nueva funcionalidad
- `fix/nombre`: Corrección de bugs

## 📚 Crear Portfolio en GitHub

### 1. Estructura recomendada
```
tu-usuario/
├── README.md (perfil profesional)
├── proyecto-1/
├── proyecto-2/
└── proyecto-3/
```

### 2. README profesional
- Descripción breve
- Tecnologías usadas
- Enlaces a proyectos
- Contacto

### 3. Proyectos destacados
- Código limpio y comentado
- README con explicación
- Datos de ejemplo
- Visualizaciones

## ✅ Checklist para Data Analyst

- [ ] Git configurado
- [ ] Cuenta en GitHub creada
- [ ] Primer repositorio creado
- [ ] README profesional
- [ ] Proyectos subidos
- [ ] Portfolio organizado

---

**¡Empieza a versionar tus proyectos ahora!** 🚀

