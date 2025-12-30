"""
Script Maestro para Descargar TODOS los Datasets del Portfolio
Portfolio Data Analyst - Descarga Completa por Niveles

Este script descarga automáticamente todos los datasets necesarios
para demostrar el stack completo en todos los niveles.

Niveles:
- 📘 Básico: Retail Sales, Superstore Sales, HR Analytics
- 📗 Intermedio: E-commerce Customer, Online Retail (UCI), Marketing Analytics
- 📙 Avanzado: Brazilian E-commerce, Store Sales Time Series, Banking
- 📕 EXTREMO: Store Sales Time Series completo, múltiples datasets integrados

Requisitos:
1. pip install kaggle pandas requests
2. Configurar kaggle.json en ~/.kaggle/kaggle.json
"""

import os
import sys
from pathlib import Path
import time

# Agregar el directorio raíz al path
sys.path.append(str(Path(__file__).parent.parent))

try:
    from kaggle.api.kaggle_api_extended import KaggleApi
    KAGGLE_AVAILABLE = True
except ImportError:
    KAGGLE_AVAILABLE = False
    print("⚠️  Kaggle API no disponible. Instala con: pip install kaggle")

import requests
from urllib.parse import urlparse


class DescargadorDatasets:
    """Clase para descargar datasets de diferentes fuentes"""
    
    def __init__(self, base_path="Portfolio"):
        self.base_path = Path(base_path)
        self.api = None
        
        if KAGGLE_AVAILABLE:
            try:
                self.api = KaggleApi()
                self.api.authenticate()
                print("✅ Kaggle API autenticada correctamente")
            except Exception as e:
                print(f"⚠️  Error al autenticar Kaggle: {e}")
                print("\n" + "="*70)
                print("❌ PROBLEMA DE CONFIGURACIÓN DETECTADO")
                print("="*70)
                print("\nEl archivo kaggle.json no está configurado correctamente.")
                print("\n📝 SOLUCIÓN RÁPIDA:")
                print("   1. Ejecuta: python Portfolio/scripts/verificar_configuracion.py")
                print("   2. Sigue las instrucciones en: Portfolio/CONFIGURAR_KAGGLE.md")
                print("   3. O revisa: Portfolio/INICIO_RAPIDO.md")
                print("\n" + "="*70)
    
    def crear_estructura_carpetas(self):
        """Crea la estructura de carpetas para todos los niveles"""
        niveles = ['01_Basico', '02_Intermedio', '03_Avanzado', '04_EXTREMO']
        
        for nivel in niveles:
            data_path = self.base_path / nivel / 'data'
            data_path.mkdir(parents=True, exist_ok=True)
            
            # Crear README en data/
            readme_path = data_path / 'README.md'
            if not readme_path.exists():
                readme_path.write_text(f"# Datos - {nivel}\n\nEsta carpeta contiene los datasets descargados para este nivel.\n")
            
            print(f"✅ Carpeta creada: {data_path}")
    
    def descargar_kaggle(self, dataset_id, destino, descripcion=""):
        """Descarga un dataset de Kaggle"""
        if not self.api:
            print(f"❌ No se puede descargar {dataset_id}: Kaggle API no disponible")
            return False
        
        try:
            destino_path = self.base_path / destino
            destino_path.mkdir(parents=True, exist_ok=True)
            
            print(f"\n📥 Descargando: {descripcion or dataset_id}")
            print(f"   Dataset: {dataset_id}")
            print(f"   Destino: {destino_path}")
            
            self.api.dataset_download_files(
                dataset_id,
                path=str(destino_path),
                unzip=True
            )
            
            # Listar archivos descargados
            archivos = list(destino_path.glob('*'))
            print(f"   ✅ Descargado: {len([f for f in archivos if f.is_file()])} archivo(s)")
            
            return True
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            return False
    
    def descargar_url(self, url, destino, nombre_archivo):
        """Descarga un archivo desde una URL"""
        try:
            destino_path = self.base_path / destino
            destino_path.mkdir(parents=True, exist_ok=True)
            
            archivo_path = destino_path / nombre_archivo
            
            print(f"\n📥 Descargando desde URL: {nombre_archivo}")
            print(f"   URL: {url}")
            
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            with open(archivo_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            tamaño_mb = archivo_path.stat().st_size / (1024 * 1024)
            print(f"   ✅ Descargado: {tamaño_mb:.2f} MB")
            
            return True
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            return False


def descargar_nivel_basico(descargador):
    """Descarga datasets para nivel Básico"""
    print("\n" + "=" * 70)
    print("📘 DESCARGANDO DATASETS - NIVEL BÁSICO")
    print("=" * 70)
    
    datasets = [
        {
            'tipo': 'kaggle',
            'id': 'rohitsahoo/sales-forecasting',
            'destino': '01_Basico/data/retail_sales',
            'descripcion': 'Retail Sales Dataset - Ventas retail reales'
        },
        {
            'tipo': 'kaggle',
            'id': 'vivek468/superstore-dataset-final',
            'destino': '01_Basico/data/superstore',
            'descripcion': 'Superstore Sales Dataset - Datos de supermercado'
        },
        {
            'tipo': 'kaggle',
            'id': 'arindam235/startup-investments-crunchbase',
            'destino': '01_Basico/data/hr_analytics',
            'descripcion': 'HR Analytics Dataset - Datos de recursos humanos'
        }
    ]
    
    resultados = []
    for dataset in datasets:
        if dataset['tipo'] == 'kaggle':
            resultado = descargador.descargar_kaggle(
                dataset['id'],
                dataset['destino'],
                dataset['descripcion']
            )
            resultados.append(resultado)
            time.sleep(2)  # Pausa entre descargas
    
    return resultados


def descargar_nivel_intermedio(descargador):
    """Descarga datasets para nivel Intermedio"""
    print("\n" + "=" * 70)
    print("📗 DESCARGANDO DATASETS - NIVEL INTERMEDIO")
    print("=" * 70)
    
    datasets = [
        {
            'tipo': 'kaggle',
            'id': 'carrie1/ecommerce-data',
            'destino': '02_Intermedio/data/ecommerce',
            'descripcion': 'E-commerce Customer Data - Datos de e-commerce'
        },
        {
            'tipo': 'url',
            'url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx',
            'destino': '02_Intermedio/data/online_retail',
            'nombre': 'OnlineRetail.xlsx',
            'descripcion': 'Online Retail Dataset (UCI) - Transacciones online'
        },
        {
            'tipo': 'kaggle',
            'id': 'datasnaek/marketing-analytics',
            'destino': '02_Intermedio/data/marketing',
            'descripcion': 'Marketing Analytics - Datos de marketing digital'
        }
    ]
    
    resultados = []
    for dataset in datasets:
        if dataset['tipo'] == 'kaggle':
            resultado = descargador.descargar_kaggle(
                dataset['id'],
                dataset['destino'],
                dataset['descripcion']
            )
            resultados.append(resultado)
        elif dataset['tipo'] == 'url':
            resultado = descargador.descargar_url(
                dataset['url'],
                dataset['destino'],
                dataset['nombre']
            )
            resultados.append(resultado)
        
        time.sleep(2)
    
    return resultados


def descargar_nivel_avanzado(descargador):
    """Descarga datasets para nivel Avanzado"""
    print("\n" + "=" * 70)
    print("📙 DESCARGANDO DATASETS - NIVEL AVANZADO")
    print("=" * 70)
    
    datasets = [
        {
            'tipo': 'kaggle',
            'id': 'olistbr/brazilian-ecommerce',
            'destino': '03_Avanzado/data/brazilian_ecommerce',
            'descripcion': 'Brazilian E-commerce - Dataset grande y completo'
        },
        {
            'tipo': 'kaggle',
            'id': 'competitions/store-sales-time-series-forecasting',
            'destino': '03_Avanzado/data/store_sales',
            'descripcion': 'Store Sales Time Series - Datos temporales extensos'
        },
        {
            'tipo': 'kaggle',
            'id': 'sriharipramod/bank-customer-data',
            'destino': '03_Avanzado/data/banking',
            'descripcion': 'Banking Dataset - Datos financieros y clientes'
        }
    ]
    
    resultados = []
    for dataset in datasets:
        if dataset['tipo'] == 'kaggle':
            resultado = descargador.descargar_kaggle(
                dataset['id'],
                dataset['destino'],
                dataset['descripcion']
            )
            resultados.append(resultado)
            time.sleep(3)  # Pausa más larga para datasets grandes
    
    return resultados


def descargar_nivel_extremo(descargador):
    """Descarga datasets para nivel EXTREMO"""
    print("\n" + "=" * 70)
    print("📕 DESCARGANDO DATASETS - NIVEL EXTREMO")
    print("=" * 70)
    
    datasets = [
        {
            'tipo': 'kaggle',
            'id': 'competitions/store-sales-time-series-forecasting',
            'destino': '04_EXTREMO/data/store_sales_completo',
            'descripcion': 'Store Sales Time Series COMPLETO - Big Data'
        },
        {
            'tipo': 'kaggle',
            'id': 'olistbr/brazilian-ecommerce',
            'destino': '04_EXTREMO/data/brazilian_ecommerce_completo',
            'descripcion': 'Brazilian E-commerce COMPLETO - Múltiples tablas'
        },
        {
            'tipo': 'kaggle',
            'id': 'datasnaek/youtube-new',
            'destino': '04_EXTREMO/data/youtube_trending',
            'descripcion': 'YouTube Trending - Dataset grande para análisis'
        }
    ]
    
    resultados = []
    for dataset in datasets:
        if dataset['tipo'] == 'kaggle':
            resultado = descargador.descargar_kaggle(
                dataset['id'],
                dataset['destino'],
                dataset['descripcion']
            )
            resultados.append(resultado)
            time.sleep(3)
    
    return resultados


def main():
    """Función principal - Descarga todos los datasets"""
    print("=" * 70)
    print("🚀 DESCARGADOR COMPLETO DE DATASETS - PORTFOLIO DATA ANALYST")
    print("=" * 70)
    print("\nEste script descargará TODOS los datasets necesarios para")
    print("demostrar el stack completo en todos los niveles del portfolio.")
    print("\nNiveles a procesar:")
    print("  📘 Básico: 3 datasets")
    print("  📗 Intermedio: 3 datasets")
    print("  📙 Avanzado: 3 datasets")
    print("  📕 EXTREMO: 3 datasets")
    print("\nTotal: 12 datasets")
    print("=" * 70)
    
    respuesta = input("\n¿Continuar con la descarga? (s/n): ").lower()
    if respuesta != 's':
        print("❌ Descarga cancelada")
        return
    
    # Inicializar descargador
    descargador = DescargadorDatasets()
    
    # Crear estructura de carpetas
    print("\n📁 Creando estructura de carpetas...")
    descargador.crear_estructura_carpetas()
    
    # Descargar por niveles
    resultados_totales = {
        'basico': [],
        'intermedio': [],
        'avanzado': [],
        'extremo': []
    }
    
    try:
        # Nivel Básico
        resultados_totales['basico'] = descargar_nivel_basico(descargador)
        
        # Nivel Intermedio
        resultados_totales['intermedio'] = descargar_nivel_intermedio(descargador)
        
        # Nivel Avanzado
        resultados_totales['avanzado'] = descargar_nivel_avanzado(descargador)
        
        # Nivel EXTREMO
        resultados_totales['extremo'] = descargar_nivel_extremo(descargador)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Descarga interrumpida por el usuario")
        return
    
    # Resumen final
    print("\n" + "=" * 70)
    print("📊 RESUMEN DE DESCARGAS")
    print("=" * 70)
    
    total_exitosos = 0
    total_fallidos = 0
    
    for nivel, resultados in resultados_totales.items():
        exitosos = sum(resultados)
        fallidos = len(resultados) - exitosos
        total_exitosos += exitosos
        total_fallidos += fallidos
        
        print(f"\n{nivel.upper()}:")
        print(f"  ✅ Exitosos: {exitosos}/{len(resultados)}")
        print(f"  ❌ Fallidos: {fallidos}/{len(resultados)}")
    
    print(f"\n{'='*70}")
    print(f"TOTAL GENERAL:")
    print(f"  ✅ Exitosos: {total_exitosos}/12")
    print(f"  ❌ Fallidos: {total_fallidos}/12")
    print(f"{'='*70}")
    
    if total_exitosos > 0:
        print("\n✅ ¡Descarga completada!")
        print("\n📝 Próximos pasos:")
        print("   1. Revisa los datasets descargados en cada carpeta data/")
        print("   2. Consulta los README.md de cada nivel")
        print("   3. Sigue las guías en FUENTES_DATOS_Y_PROYECTOS.md")
    else:
        print("\n⚠️  No se descargaron datasets. Verifica:")
        print("   1. Que tengas instalado: pip install kaggle")
        print("   2. Que tengas configurado kaggle.json")
        print("   3. Tu conexión a internet")


if __name__ == "__main__":
    main()

