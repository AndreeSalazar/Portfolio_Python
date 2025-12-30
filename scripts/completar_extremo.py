"""
Script para completar la generación de datos EXTREMOS
Genera solo lo que falta
"""

import sys
from pathlib import Path

# Agregar encoding para Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Importar funciones del script principal
sys.path.append(str(Path(__file__).parent))
from generar_datos_extremo import (
    generar_big_data_time_series,
    generar_brazilian_ecommerce_completo,
    generar_youtube_trending
)

def completar_transactions():
    """Completa solo transactions.csv que falta"""
    print("=" * 70)
    print("COMPLETANDO TRANSACTIONS.CSV")
    print("=" * 70)
    
    import pandas as pd
    import numpy as np
    from datetime import timedelta
    import random
    
    base_path = Path("Portfolio/04_EXTREMO/data/store_sales_completo")
    base_path.mkdir(parents=True, exist_ok=True)
    
    np.random.seed(42)
    random.seed(42)
    
    # Transactions - Transacciones diarias por tienda
    print("\nGenerando Transactions Dataset...")
    transactions_data = []
    fechas_trans = pd.date_range(start='2013-01-01', end='2017-08-31', freq='D')
    
    for fecha in fechas_trans[::7]:  # Una vez por semana para optimizar
        for store_nbr in range(1, 201):
            transactions_data.append({
                'date': fecha.strftime('%Y-%m-%d'),
                'store_nbr': store_nbr,
                'transactions': np.random.randint(100, 10000)
            })
    
    df_transactions = pd.DataFrame(transactions_data)
    df_transactions.to_csv(base_path / 'transactions.csv', index=False)
    print(f"[OK] {len(df_transactions):,} registros de transacciones guardados")


def main():
    """Completa todo lo que falta"""
    print("=" * 70)
    print("COMPLETANDO GENERACION DE DATOS EXTREMOS")
    print("=" * 70)
    
    # Verificar qué falta
    base_path = Path("Portfolio/04_EXTREMO/data")
    
    # 1. Completar transactions.csv
    transactions_path = base_path / 'store_sales_completo' / 'transactions.csv'
    if not transactions_path.exists():
        print("\n[1] Completando transactions.csv...")
        completar_transactions()
    else:
        print("\n[1] transactions.csv ya existe")
    
    # 2. Generar Brazilian E-commerce si no existe
    brazilian_path = base_path / 'brazilian_ecommerce_completo'
    if not brazilian_path.exists() or len(list(brazilian_path.glob('*.csv'))) == 0:
        print("\n[2] Generando Brazilian E-commerce Completo...")
        generar_brazilian_ecommerce_completo()
    else:
        print("\n[2] Brazilian E-commerce ya existe")
    
    # 3. Generar YouTube Trending si no existe
    youtube_path = base_path / 'youtube_trending'
    if not youtube_path.exists() or len(list(youtube_path.glob('*.csv'))) == 0:
        print("\n[3] Generando YouTube Trending...")
        generar_youtube_trending()
    else:
        print("\n[3] YouTube Trending ya existe")
    
    print("\n" + "=" * 70)
    print("[EXITO] Generacion completada")
    print("=" * 70)


if __name__ == "__main__":
    main()

