"""
Script Maestro - Ejecuta TODO en orden
Portfolio Data Analyst - Nivel Básico

Este script ejecuta todos los pasos del análisis en orden:
1. Cargar datos a PostgreSQL
2. Explorar datos
3. Generar visualizaciones
4. Exportar a Excel
"""

import sys
from pathlib import Path

# Agregar el directorio al path
sys.path.append(str(Path(__file__).parent))

def ejecutar_todo():
    """Ejecuta todos los pasos en orden"""
    
    print("=" * 70)
    print("EJECUTANDO PROYECTO COMPLETO - NIVEL BASICO")
    print("=" * 70)
    print("\nEste script ejecutará todos los pasos del análisis:")
    print("  1. Cargar datos a PostgreSQL")
    print("  2. Explorar datos con pandas/numpy")
    print("  3. Generar visualizaciones")
    print("  4. Exportar resultados a Excel")
    print("\n" + "=" * 70)
    
    # Paso 1: Cargar datos
    print("\n[PASO 1/4] Cargando datos a PostgreSQL...")
    print("-" * 70)
    try:
        from cargar_datos_postgresql import cargar_datos
        if cargar_datos():
            print("[OK] Paso 1 completado")
        else:
            print("[ERROR] Error en Paso 1")
            return False
    except Exception as e:
        print(f"[ERROR] Error en Paso 1: {e}")
        return False
    
    # Paso 2: Explorar datos
    print("\n[PASO 2/4] Explorando datos...")
    print("-" * 70)
    try:
        from exploracion_datos import explorar_datos
        explorar_datos()
        print("[OK] Paso 2 completado")
    except Exception as e:
        print(f"[ERROR] Error en Paso 2: {e}")
        return False
    
    # Paso 3: Visualizaciones
    print("\n[PASO 3/4] Generando visualizaciones...")
    print("-" * 70)
    try:
        from visualizaciones import crear_visualizaciones
        if crear_visualizaciones():
            print("[OK] Paso 3 completado")
        else:
            print("[ERROR] Error en Paso 3")
            return False
    except Exception as e:
        print(f"[ERROR] Error en Paso 3: {e}")
        return False
    
    # Paso 4: Exportar a Excel
    print("\n[PASO 4/4] Exportando a Excel...")
    print("-" * 70)
    try:
        from exportar_excel import exportar_a_excel
        if exportar_a_excel():
            print("[OK] Paso 4 completado")
        else:
            print("[ERROR] Error en Paso 4")
            return False
    except Exception as e:
        print(f"[ERROR] Error en Paso 4: {e}")
        return False
    
    # Resumen final
    print("\n" + "=" * 70)
    print("[EXITO] PROYECTO COMPLETO EJECUTADO")
    print("=" * 70)
    print("\nArchivos generados:")
    print("  - PostgreSQL: Datos cargados en BD")
    print("  - figures/: Visualizaciones guardadas")
    print("  - excel/: Reporte Excel creado")
    print("\nPróximos pasos:")
    print("  1. Revisar visualizaciones en figures/")
    print("  2. Abrir reporte Excel en excel/")
    print("  3. Abrir notebook: notebooks/analisis_completo_basico.ipynb")
    print("  4. Revisar consultas SQL: sql/consultas_ventas.sql")
    print("=" * 70)
    
    return True


if __name__ == "__main__":
    ejecutar_todo()

