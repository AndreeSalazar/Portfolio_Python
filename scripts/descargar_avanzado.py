"""
Script para descargar datasets del Nivel Avanzado
Portfolio Data Analyst - Nivel Avanzado

Datasets:
1. Brazilian E-commerce Dataset
2. Store Sales Time Series Forecasting
3. Banking Dataset
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from scripts.descargar_todos_datasets import DescargadorDatasets, descargar_nivel_avanzado


def main():
    print("=" * 70)
    print("📙 DESCARGADOR DE DATASETS - NIVEL AVANZADO")
    print("=" * 70)
    print("\n⚠️  ADVERTENCIA: Estos datasets son grandes y pueden tardar varios minutos")
    
    respuesta = input("\n¿Continuar? (s/n): ").lower()
    if respuesta != 's':
        print("❌ Descarga cancelada")
        return
    
    descargador = DescargadorDatasets()
    descargador.crear_estructura_carpetas()
    
    resultados = descargar_nivel_avanzado(descargador)
    
    print("\n" + "=" * 70)
    print("📊 RESUMEN")
    print("=" * 70)
    exitosos = sum(resultados)
    print(f"✅ Exitosos: {exitosos}/{len(resultados)}")
    print(f"❌ Fallidos: {len(resultados) - exitosos}/{len(resultados)}")
    
    if exitosos > 0:
        print("\n✅ Datasets descargados en: Portfolio/03_Avanzado/data/")
        print("📝 Revisa el README.md en cada subcarpeta para más información")


if __name__ == "__main__":
    main()

