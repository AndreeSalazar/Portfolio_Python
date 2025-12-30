"""
Script para descargar datasets del Nivel Básico
Portfolio Data Analyst - Nivel Básico

Datasets:
1. Retail Sales Dataset
2. Superstore Sales Dataset
3. HR Analytics Dataset
"""

import sys
from pathlib import Path

# Agregar el directorio raíz al path
sys.path.append(str(Path(__file__).parent.parent))

from scripts.descargar_todos_datasets import DescargadorDatasets, descargar_nivel_basico


def main():
    print("=" * 70)
    print("📘 DESCARGADOR DE DATASETS - NIVEL BÁSICO")
    print("=" * 70)
    
    descargador = DescargadorDatasets()
    descargador.crear_estructura_carpetas()
    
    resultados = descargar_nivel_basico(descargador)
    
    print("\n" + "=" * 70)
    print("📊 RESUMEN")
    print("=" * 70)
    exitosos = sum(resultados)
    print(f"✅ Exitosos: {exitosos}/{len(resultados)}")
    print(f"❌ Fallidos: {len(resultados) - exitosos}/{len(resultados)}")
    
    if exitosos > 0:
        print("\n✅ Datasets descargados en: Portfolio/01_Basico/data/")
        print("📝 Revisa el README.md en cada subcarpeta para más información")


if __name__ == "__main__":
    main()

