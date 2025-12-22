# 🔧 Guía Completa: Configurar Kaggle API en Windows

Esta guía te ayudará a configurar correctamente Kaggle API para poder descargar los datasets del portfolio.

---

## ❌ Problema Detectado

Si ves este error:
```
Could not find kaggle.json. Make sure it's located in C:\Users\andre\.kaggle
```

Significa que falta el archivo de autenticación de Kaggle.

---

## ✅ Solución Paso a Paso

### Paso 1: Crear Cuenta en Kaggle (si no tienes)

1. Ir a https://www.kaggle.com/
2. Click en "Sign Up" o "Sign In"
3. Puedes usar Google, Facebook o crear cuenta con email

---

### Paso 2: Obtener Token de API

1. **Iniciar sesión** en Kaggle
2. Click en tu **avatar/foto de perfil** (esquina superior derecha)
3. Seleccionar **"Account"** del menú
4. Bajar hasta la sección **"API"**
5. Click en **"Create New API Token"**
6. Se descargará automáticamente el archivo `kaggle.json`

---

### Paso 3: Ubicar el Archivo Descargado

El archivo `kaggle.json` generalmente se descarga en:
- **Descargas**: `C:\Users\andre\Downloads\kaggle.json`
- O en la carpeta que tengas configurada para descargas

---

### Paso 4: Crear Carpeta .kaggle

**Opción A: Usando PowerShell (Recomendado)**

```powershell
# Crear la carpeta .kaggle
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.kaggle"

# Verificar que se creó
Test-Path "$env:USERPROFILE\.kaggle"
```

**Opción B: Usando Explorador de Archivos**

1. Abrir **Explorador de Archivos**
2. En la barra de direcciones, escribir: `%USERPROFILE%`
3. Presionar Enter
4. Crear nueva carpeta llamada `.kaggle` (con el punto al inicio)
   - Si no te deja crear carpeta con punto, usar PowerShell (Opción A)

---

### Paso 5: Mover kaggle.json a la Carpeta Correcta

**Ubicación correcta**: `C:\Users\andre\.kaggle\kaggle.json`

**Método 1: Arrastrar y Soltar**
1. Abrir carpeta de Descargas
2. Buscar `kaggle.json`
3. Arrastrar a la carpeta `.kaggle` que creaste

**Método 2: Usando PowerShell**

```powershell
# Mover archivo desde Descargas a .kaggle
Move-Item -Path "$env:USERPROFILE\Downloads\kaggle.json" -Destination "$env:USERPROFILE\.kaggle\kaggle.json" -Force

# Verificar que está en el lugar correcto
Test-Path "$env:USERPROFILE\.kaggle\kaggle.json"
```

**Método 3: Copiar y Pegar**
1. Ir a carpeta de Descargas
2. Copiar `kaggle.json`
3. Ir a `C:\Users\andre\.kaggle\`
4. Pegar el archivo

---

### Paso 6: Verificar el Contenido del Archivo

El archivo `kaggle.json` debe tener este formato:

```json
{
  "username": "tu-usuario-kaggle",
  "key": "tu-clave-api-muy-larga"
}
```

**Para verificar**:

```powershell
# Ver contenido del archivo
Get-Content "$env:USERPROFILE\.kaggle\kaggle.json"
```

Si el archivo está vacío o tiene formato incorrecto:
1. Volver a Kaggle
2. Generar nuevo token
3. Reemplazar el archivo

---

### Paso 7: Verificar Configuración

Ejecutar el script de verificación:

```powershell
python Portfolio/scripts/verificar_configuracion.py
```

Deberías ver:
```
✅ Python versión correcta
✅ Kaggle API instalada
✅ Archivo kaggle.json encontrado
✅ Formato del archivo correcto
✅ Autenticación exitosa
```

---

## 🔍 Verificación Manual Rápida

### Verificar que el archivo existe:

```powershell
Test-Path "$env:USERPROFILE\.kaggle\kaggle.json"
```

Debería devolver: `True`

### Verificar contenido:

```powershell
Get-Content "$env:USERPROFILE\.kaggle\kaggle.json"
```

Debería mostrar tu username y key.

### Probar autenticación:

```powershell
python -c "from kaggle.api.kaggle_api_extended import KaggleApi; api = KaggleApi(); api.authenticate(); print('✅ Autenticación exitosa')"
```

---

## 🐛 Solución de Problemas Comunes

### Problema 1: "No se puede crear carpeta con punto"

**Solución**: Usar PowerShell:
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.kaggle"
```

### Problema 2: "El archivo no se encuentra"

**Solución**: 
1. Verificar que descargaste el archivo desde Kaggle
2. Buscar en carpeta de Descargas
3. Verificar que lo moviste a `.kaggle`

### Problema 3: "Formato incorrecto del JSON"

**Solución**:
1. Abrir `kaggle.json` con Notepad
2. Verificar que tenga formato JSON válido
3. Si está corrupto, descargar nuevo token desde Kaggle

### Problema 4: "Permission denied" o "Acceso denegado"

**Solución**:
1. Ejecutar PowerShell como Administrador
2. O verificar permisos de la carpeta `.kaggle`

### Problema 5: "Invalid credentials"

**Solución**:
1. Regenerar token desde Kaggle
2. Reemplazar el archivo `kaggle.json` antiguo

---

## 📋 Checklist Final

Antes de ejecutar los scripts de descarga, verifica:

- [ ] ✅ Cuenta de Kaggle creada
- [ ] ✅ Token de API descargado desde Kaggle
- [ ] ✅ Carpeta `.kaggle` creada en `C:\Users\andre\.kaggle`
- [ ] ✅ Archivo `kaggle.json` movido a la carpeta `.kaggle`
- [ ] ✅ Archivo tiene formato JSON correcto
- [ ] ✅ Script de verificación ejecutado exitosamente
- [ ] ✅ Autenticación funciona correctamente

---

## 🚀 Una Vez Configurado

Cuando todo esté configurado, puedes ejecutar:

```powershell
# Verificar configuración
python Portfolio/scripts/verificar_configuracion.py

# Descargar todos los datasets
python Portfolio/scripts/descargar_todos_datasets.py

# O descargar por nivel
python Portfolio/scripts/descargar_basico.py
```

---

## 📚 Recursos Adicionales

- **Documentación oficial de Kaggle API**: https://github.com/Kaggle/kaggle-api
- **Guía de inicio rápido**: `Portfolio/INICIO_RAPIDO.md`
- **Resumen de descargas**: `Portfolio/RESUMEN_DESCARGAS.md`

---

## 💡 Notas Importantes

1. **Seguridad**: El archivo `kaggle.json` contiene credenciales. No lo compartas ni lo subas a Git.

2. **Ubicación exacta**: En Windows debe estar en:
   ```
   C:\Users\TU-USUARIO\.kaggle\kaggle.json
   ```

3. **Permisos**: Asegúrate de tener permisos de lectura/escritura en la carpeta.

4. **Actualización**: Si cambias tu contraseña de Kaggle, necesitarás generar un nuevo token.

---

**Última actualización**: Diciembre 2024

**Si sigues teniendo problemas**, ejecuta el script de verificación y revisa los mensajes de error específicos.

