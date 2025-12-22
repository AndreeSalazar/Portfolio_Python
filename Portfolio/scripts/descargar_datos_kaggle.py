"""
Script para descargar datasets de Kaggle
Portfolio Data Analyst

Requisitos:
1. Instalar: pip install kaggle
2. Configurar credenciales de Kaggle:
   - Ir a https://www.kaggle.com/account
   - Click en "Create New API Token"
   - Descargar kaggle.json
   - Colocar en: C:\Users\tu-usuario\.kaggle\kaggle.json (Windows)
                 ~/.kaggle/kaggle.json (Linux/Mac)
"""

import os
import zipfile
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

def descargar_dataset_kaggle(dataset_name, destino='data', descomprimir=True):
    """
    Descarga un dataset de Kaggle
    
    Args:
        dataset_name: Nombre del dataset (formato: usuario/dataset)
                     Ejemplo: 'imtkaggleteam/retail-sales-dataset'
        destino: Carpeta donde guardar los datos
        descomprimir: Si True, descomprime automáticamente
    """
    try:
        # Autenticar
        api = KaggleApi()
        api.authenticate()
        
        print(f"📥 Descargando dataset: {dataset_name}")
        print(f"📁 Destino: {destino}")
        
        # Crear carpeta si no existe
        Path(destino).mkdir(parents=True, exist_ok=True)
        
        # Descargar dataset
        api.dataset_download_files(
            dataset_name, 
            path=destino, 
            unzip=descomprimir
        )
        
        print(f"✅ Dataset descargado exitosamente en: {destino}")
        
        # Listar archivos descargados
        archivos = list(Path(destino).glob('*'))
        print(f"\n📄 Archivos descargados:")
        for archivo in archivos:
            if archivo.is_file():
                tamaño = archivo.stat().st_size / (1024 * 1024)  # MB
                print(f"   - {archivo.name} ({tamaño:.2f} MB)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al descargar: {str(e)}")
        print("\n💡 Verifica:")
        print("   1. Que tengas instalado: pip install kaggle")
        print("   2. Que tengas configurado kaggle.json")
        print("   3. Que el nombre del dataset sea correcto")
        return False


def listar_datasets_populares(categoria='retail'):
    """
    Lista datasets populares de una categoría
    """
    print(f"🔍 Buscando datasets de: {categoria}")
    print("\n💡 Para descargar, usa:")
    print("   descargar_dataset_kaggle('usuario/dataset-name')")
    print("\n📊 Algunos datasets recomendados:")
    
    datasets_recomendados = {
        'retail': [
            ('imtkaggleteam/retail-sales-dataset', 'Retail Sales Dataset'),
            ('rohitsahoo/sales-forecasting', 'Sales Forecasting'),
            ('datasnaek/youtube-new', 'YouTube Trending Videos'),
        ],
        'ecommerce': [
            ('carrie1/ecommerce-data', 'E-commerce Data'),
            ('olistbr/brazilian-ecommerce', 'Brazilian E-commerce'),
        ],
        'customer': [
            ('datasnaek/marketing-analytics', 'Marketing Analytics'),
            ('arindam235/startup-investments-crunchbase', 'Startup Investments'),
        ]
    }
    
    if categoria in datasets_recomendados:
        for dataset_id, nombre in datasets_recomendados[categoria]:
            print(f"\n   📦 {nombre}")
            print(f"      ID: {dataset_id}")
            print(f"      Comando: descargar_dataset_kaggle('{dataset_id}')")


if __name__ == "__main__":
    print("=" * 60)
    print("DESCARGADOR DE DATASETS KAGGLE")
    print("=" * 60)
    
    # Ejemplo 1: Listar datasets recomendados
    listar_datasets_populares('retail')
    
    # Ejemplo 2: Descargar un dataset específico
    # Descomenta y ajusta según necesites:
    
    # dataset_ejemplo = 'imtkaggleteam/retail-sales-dataset'
    # descargar_dataset_kaggle(dataset_ejemplo, destino='data/retail')
    
    print("\n" + "=" * 60)
    print("💡 Para usar este script:")
    print("   1. Configura tus credenciales de Kaggle")
    print("   2. Descomenta la línea de descarga")
    print("   3. Ejecuta: python scripts/descargar_datos_kaggle.py")
    print("=" * 60)

