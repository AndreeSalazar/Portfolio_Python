"""
Generar visualizaciones básicas
Portfolio Data Analyst - Nivel Básico

Este script crea visualizaciones profesionales de los datos
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from pathlib import Path

# Configuración
DATABASE_URL = 'postgresql://postgres:123456@localhost:5432/retail_analysis_basico'

def crear_visualizaciones():
    """Crea visualizaciones básicas de los datos"""
    
    print("=" * 70)
    print("GENERANDO VISUALIZACIONES")
    print("=" * 70)
    
    try:
        # Crear conexión con encoding UTF-8
        engine = create_engine(
            DATABASE_URL,
            connect_args={
                'client_encoding': 'utf8'
            },
            pool_pre_ping=True
        )
        
        # Cargar datos
        print("\n[1] Cargando datos...")
        df_ventas = pd.read_sql("SELECT * FROM ventas", engine)
        df_ventas['fecha'] = pd.to_datetime(df_ventas['fecha'])
        print(f"   [OK] {len(df_ventas)} ventas cargadas")
        
        # Crear carpeta figures si no existe
        figures_dir = Path(__file__).parent.parent / 'figures'
        figures_dir.mkdir(exist_ok=True)
        
        # Configurar estilo
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        # Crear figura con múltiples subplots
        print("\n[2] Generando gráficos...")
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('Análisis de Ventas Retail - Nivel Básico', fontsize=16, fontweight='bold', y=0.995)
        
        # Gráfico 1: Ventas por región (Barras)
        print("   [2.1] Gráfico de barras - Ventas por región...")
        ventas_region = df_ventas.groupby('region')['total'].sum().sort_values(ascending=False)
        colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']
        axes[0, 0].bar(ventas_region.index, ventas_region.values, color=colors[:len(ventas_region)])
        axes[0, 0].set_title('Ventas Totales por Región', fontsize=14, fontweight='bold', pad=15)
        axes[0, 0].set_xlabel('Región', fontsize=12)
        axes[0, 0].set_ylabel('Total Ventas (€)', fontsize=12)
        axes[0, 0].grid(axis='y', alpha=0.3, linestyle='--')
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # Agregar valores en las barras
        for i, v in enumerate(ventas_region.values):
            axes[0, 0].text(i, v, f'{v:,.0f}€', ha='center', va='bottom', fontweight='bold')
        
        # Gráfico 2: Ventas mensuales (Línea)
        print("   [2.2] Gráfico de líneas - Ventas mensuales...")
        df_ventas['mes'] = df_ventas['fecha'].dt.to_period('M')
        ventas_mensuales = df_ventas.groupby('mes')['total'].sum()
        axes[0, 1].plot(range(len(ventas_mensuales)), ventas_mensuales.values, 
                       marker='o', linewidth=2.5, markersize=8, color='#2ecc71')
        axes[0, 1].set_title('Evolución de Ventas Mensuales', fontsize=14, fontweight='bold', pad=15)
        axes[0, 1].set_xlabel('Mes', fontsize=12)
        axes[0, 1].set_ylabel('Total Ventas (€)', fontsize=12)
        axes[0, 1].grid(True, alpha=0.3, linestyle='--')
        axes[0, 1].set_xticks(range(len(ventas_mensuales)))
        axes[0, 1].set_xticklabels([str(m) for m in ventas_mensuales.index], rotation=45, ha='right')
        
        # Gráfico 3: Top productos (Barras horizontales)
        print("   [2.3] Gráfico de barras horizontales - Top productos...")
        top_productos = df_ventas.groupby('producto')['total'].sum().nlargest(5)
        axes[1, 0].barh(top_productos.index, top_productos.values, color='steelblue', alpha=0.8)
        axes[1, 0].set_title('Top 5 Productos por Ventas', fontsize=14, fontweight='bold', pad=15)
        axes[1, 0].set_xlabel('Total Ventas (€)', fontsize=12)
        axes[1, 0].grid(axis='x', alpha=0.3, linestyle='--')
        
        # Agregar valores
        for i, v in enumerate(top_productos.values):
            axes[1, 0].text(v, i, f'{v:,.0f}€', va='center', fontweight='bold')
        
        # Gráfico 4: Distribución de ventas (Histograma)
        print("   [2.4] Histograma - Distribución de montos...")
        axes[1, 1].hist(df_ventas['total'], bins=50, edgecolor='black', alpha=0.7, color='#9b59b6')
        media = df_ventas['total'].mean()
        mediana = df_ventas['total'].median()
        axes[1, 1].axvline(media, color='r', linestyle='--', linewidth=2, label=f'Media: {media:.2f}€')
        axes[1, 1].axvline(mediana, color='g', linestyle='--', linewidth=2, label=f'Mediana: {mediana:.2f}€')
        axes[1, 1].set_title('Distribución de Montos de Venta', fontsize=14, fontweight='bold', pad=15)
        axes[1, 1].set_xlabel('Monto de Venta (€)', fontsize=12)
        axes[1, 1].set_ylabel('Frecuencia', fontsize=12)
        axes[1, 1].legend(fontsize=10)
        axes[1, 1].grid(axis='y', alpha=0.3, linestyle='--')
        
        plt.tight_layout()
        
        # Guardar figura
        figura_path = figures_dir / 'analisis_ventas_basico.png'
        plt.savefig(figura_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"\n[OK] Gráfico guardado: {figura_path}")
        
        plt.close()
        
        # Crear segundo gráfico: Análisis por segmento
        print("\n[3] Generando gráfico adicional - Ventas por segmento...")
        df_clientes = pd.read_sql("SELECT * FROM clientes", engine)
        df_ventas_clientes = df_ventas.merge(df_clientes, on='cliente_id', how='left')
        
        fig2, axes2 = plt.subplots(1, 2, figsize=(14, 6))
        fig2.suptitle('Análisis por Segmento de Cliente', fontsize=16, fontweight='bold')
        
        # Ventas por segmento
        ventas_segmento = df_ventas_clientes.groupby('segmento')['total'].agg(['sum', 'mean', 'count'])
        ventas_segmento.columns = ['Total', 'Promedio', 'Cantidad']
        
        axes2[0].bar(ventas_segmento.index, ventas_segmento['Total'], color=['#3498db', '#e74c3c', '#2ecc71'])
        axes2[0].set_title('Ventas Totales por Segmento', fontsize=12, fontweight='bold')
        axes2[0].set_ylabel('Total Ventas (€)')
        axes2[0].grid(axis='y', alpha=0.3)
        
        # Ticket promedio por segmento
        axes2[1].bar(ventas_segmento.index, ventas_segmento['Promedio'], color=['#3498db', '#e74c3c', '#2ecc71'])
        axes2[1].set_title('Ticket Promedio por Segmento', fontsize=12, fontweight='bold')
        axes2[1].set_ylabel('Ticket Promedio (€)')
        axes2[1].grid(axis='y', alpha=0.3)
        
        plt.tight_layout()
        figura_path2 = figures_dir / 'analisis_segmento.png'
        plt.savefig(figura_path2, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"[OK] Gráfico guardado: {figura_path2}")
        
        plt.close()
        
        print("\n" + "=" * 70)
        print("[EXITO] Visualizaciones generadas correctamente")
        print("=" * 70)
        
        return True
        
    except Exception as e:
        print(f"\n[ERROR] Error al generar visualizaciones: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    crear_visualizaciones()

