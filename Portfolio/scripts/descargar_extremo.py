"""
Script para descargar datasets del Nivel EXTREMO
Portfolio Data Analyst - Nivel EXTREMO

Datasets:
1. Store Sales Time Series Forecasting (COMPLETO)
2. Brazilian E-commerce (COMPLETO)
3. YouTube Trending Dataset

⚠️ ADVERTENCIA: Estos datasets son MUY grandes (varios GB)
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from scripts.descargar_todos_datasets import DescargadorDatasets, descargar_nivel_extremo


def main():
    print("=" * 70)
    print("📕 DESCARGADOR DE DATASETS - NIVEL EXTREMO")
    print("=" * 70)
    print("\n⚠️  ADVERTENCIA CRÍTICA:")
    print("   - Estos datasets son MUY grandes (varios GB)")
    print("   - La descarga puede tardar HORAS")
    print("   - Requieren mucho espacio en disco")
    print("   - Requieren procesamiento optimizado")
    
    respuesta = input("\n¿Estás seguro de continuar? (escribe 'SI' para confirmar): ")
    if respuesta != 'SI':
        print("❌ Descarga cancelada")
        return
    
    descargador = DescargadorDatasets()
    descargador.crear_estructura_carpetas()
    
    resultados = descargar_nivel_extremo(descargador)
    
    print("\n" + "=" * 70)
    print("📊 RESUMEN")
    print("=" * 70)
    exitosos = sum(resultados)
    print(f"✅ Exitosos: {exitosos}/{len(resultados)}")
    print(f"❌ Fallidos: {len(resultados) - exitosos}/{len(resultados)}")
    
    if exitosos > 0:
        print("\n✅ Datasets descargados en: Portfolio/04_EXTREMO/data/")
        print("📝 Revisa el README.md en cada subcarpeta para más información")
        print("\n💡 Próximos pasos:")
        print("   1. Verifica el espacio en disco disponible")
        print("   2. Revisa los scripts de procesamiento en chunks")
        print("   3. Configura PostgreSQL con particionado")


if __name__ == "__main__":
    main()

