"""
Script de Verificación de Configuración
Portfolio Data Analyst

Verifica que todo esté configurado correctamente antes de descargar datasets.
"""

import os
import sys
from pathlib import Path
import platform

# Configurar encoding UTF-8 para Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def verificar_python():
    """Verifica que Python esté instalado"""
    print("=" * 70)
    print("VERIFICACION DE CONFIGURACION - PORTFOLIO DATA ANALYST")
    print("=" * 70)
    
    print("\n[1] Verificando Python...")
    version = sys.version_info
    print(f"   Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 7:
        print("   [OK] Python version correcta")
        return True
    else:
        print("   [ERROR] Se requiere Python 3.7 o superior")
        return False


def verificar_kaggle_instalado():
    """Verifica que kaggle esté instalado"""
    print("\n[2] Verificando Kaggle API...")
    try:
        import kaggle
        print("   [OK] Kaggle API instalada")
        return True
    except ImportError:
        print("   [ERROR] Kaggle API NO instalada")
        print("   [INFO] Instala con: pip install kaggle")
        return False


def verificar_kaggle_json():
    """Verifica que kaggle.json exista y esté en la ubicación correcta"""
    print("\n[3] Verificando kaggle.json...")
    
    sistema = platform.system()
    
    if sistema == "Windows":
        usuario = os.environ.get('USERNAME', os.environ.get('USER', 'usuario'))
        ruta_kaggle = Path(f"C:/Users/{usuario}/.kaggle")
        archivo_json = ruta_kaggle / "kaggle.json"
    else:
        ruta_kaggle = Path.home() / ".kaggle"
        archivo_json = ruta_kaggle / "kaggle.json"
    
    print(f"   Buscando en: {archivo_json}")
    
    if archivo_json.exists():
        print("   [OK] Archivo kaggle.json encontrado")
        
        # Verificar contenido
        try:
            import json
            with open(archivo_json, 'r') as f:
                contenido = json.load(f)
            
            if 'username' in contenido and 'key' in contenido:
                print("   [OK] Formato del archivo correcto")
                print(f"   Usuario: {contenido.get('username', 'N/A')}")
                return True
            else:
                print("   [ERROR] Formato incorrecto. Debe contener 'username' y 'key'")
                return False
        except json.JSONDecodeError:
            print("   [ERROR] El archivo no es un JSON valido")
            return False
    else:
        print("   [ERROR] Archivo kaggle.json NO encontrado")
        print("\n   [INFO] COMO CONFIGURAR:")
        print("   1. Ir a https://www.kaggle.com/")
        print("   2. Iniciar sesion o crear cuenta")
        print("   3. Ir a Account -> API -> Create New API Token")
        print("   4. Se descargara kaggle.json")
        print(f"   5. Colocar en: {archivo_json}")
        
        # Crear directorio si no existe
        if not ruta_kaggle.exists():
            print(f"\n   [INFO] Creando directorio: {ruta_kaggle}")
            try:
                ruta_kaggle.mkdir(parents=True, exist_ok=True)
                print("   [OK] Directorio creado")
            except Exception as e:
                print(f"   [ERROR] Error al crear directorio: {e}")
        
        return False


def verificar_autenticacion():
    """Intenta autenticarse con Kaggle"""
    print("\n[4] Verificando autenticacion con Kaggle...")
    
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
        api = KaggleApi()
        api.authenticate()
        print("   [OK] Autenticacion exitosa")
        return True
    except Exception as e:
        print(f"   [ERROR] Error de autenticacion: {str(e)}")
        return False


def verificar_espacio_disco():
    """Verifica espacio en disco disponible"""
    print("\n[5] Verificando espacio en disco...")
    
    try:
        import shutil
        total, usado, libre = shutil.disk_usage(".")
        libre_gb = libre / (1024**3)
        
        print(f"   Espacio libre: {libre_gb:.2f} GB")
        
        if libre_gb >= 30:
            print("   [OK] Espacio suficiente (30+ GB recomendado)")
            return True
        elif libre_gb >= 10:
            print("   [ADVERTENCIA] Espacio limitado (se recomienda 30+ GB)")
            return True
        else:
            print("   [ERROR] Espacio insuficiente (minimo 10 GB)")
            return False
    except Exception as e:
        print(f"   [ADVERTENCIA] No se pudo verificar espacio: {e}")
        return True  # No crítico


def verificar_dependencias():
    """Verifica otras dependencias"""
    print("\n[6] Verificando dependencias adicionales...")
    
    dependencias = {
        'pandas': 'pandas',
        'requests': 'requests',
        'numpy': 'numpy'
    }
    
    todas_ok = True
    for nombre, modulo in dependencias.items():
        try:
            __import__(modulo)
            print(f"   [OK] {nombre} instalado")
        except ImportError:
            print(f"   [ERROR] {nombre} NO instalado")
            print(f"   [INFO] Instala con: pip install {nombre}")
            todas_ok = False
    
    return todas_ok


def main():
    """Función principal de verificación"""
    resultados = {
        'python': verificar_python(),
        'kaggle_instalado': verificar_kaggle_instalado(),
        'kaggle_json': verificar_kaggle_json(),
        'autenticacion': False,
        'espacio': verificar_espacio_disco(),
        'dependencias': verificar_dependencias()
    }
    
    # Solo intentar autenticación si kaggle está instalado y configurado
    if resultados['kaggle_instalado'] and resultados['kaggle_json']:
        resultados['autenticacion'] = verificar_autenticacion()
    
    # Resumen final
    print("\n" + "=" * 70)
    print("RESUMEN DE VERIFICACION")
    print("=" * 70)
    
    total = len(resultados)
    exitosos = sum(1 for v in resultados.values() if v)
    
    for nombre, resultado in resultados.items():
        estado = "[OK]" if resultado else "[ERROR]"
        print(f"{estado} {nombre.replace('_', ' ').title()}")
    
    print(f"\n{'='*70}")
    print(f"Total: {exitosos}/{total} verificaciones exitosas")
    
    if exitosos == total:
        print("\n[EXITO] Todo esta configurado correctamente!")
        print("   Puedes ejecutar los scripts de descarga:")
        print("   python Portfolio/scripts/descargar_todos_datasets.py")
    else:
        print("\n[ADVERTENCIA] Hay problemas de configuracion que resolver")
        print("\n[INFO] PROXIMOS PASOS:")
        
        if not resultados['kaggle_instalado']:
            print("   1. Instalar Kaggle: pip install kaggle")
        
        if not resultados['kaggle_json']:
            print("   2. Configurar kaggle.json (ver instrucciones arriba)")
        
        if not resultados['dependencias']:
            print("   3. Instalar dependencias faltantes")
        
        print("\n   Revisa las instrucciones detalladas en:")
        print("   - Portfolio/INICIO_RAPIDO.md")
        print("   - Portfolio/CONFIGURAR_KAGGLE.md")
    
    print("=" * 70)


if __name__ == "__main__":
    main()

