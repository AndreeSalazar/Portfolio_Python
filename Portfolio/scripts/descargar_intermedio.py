"""
Script para descargar datasets del Nivel Intermedio
Portfolio Data Analyst - Nivel Intermedio

Datasets:
1. E-commerce Customer Data
2. Online Retail Dataset (UCI)
3. Marketing Analytics Dataset
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from scripts.descargar_todos_datasets import DescargadorDatasets, descargar_nivel_intermedio


def main():
    print("=" * 70)
    print("📗 DESCARGADOR DE DATASETS - NIVEL INTERMEDIO")
    print("=" * 70)
    
    descargador = DescargadorDatasets()
    descargador.crear_estructura_carpetas()
    
    resultados = descargar_nivel_intermedio(descargador)
    
    print("\n" + "=" * 70)
    print("📊 RESUMEN")
    print("=" * 70)
    exitosos = sum(resultados)
    print(f"✅ Exitosos: {exitosos}/{len(resultados)}")
    print(f"❌ Fallidos: {len(resultados) - exitosos}/{len(resultados)}")
    
    if exitosos > 0:
        print("\n✅ Datasets descargados en: Portfolio/02_Intermedio/data/")
        print("📝 Revisa el README.md en cada subcarpeta para más información")


if __name__ == "__main__":
    main()

