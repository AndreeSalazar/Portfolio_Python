"""
Completa los archivos faltantes del nivel EXTREMO con progreso en tiempo real
"""

import sys
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import timedelta
import random
import time
import warnings
warnings.filterwarnings('ignore')

# Configurar encoding
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def mostrar_progreso(actual, total, mensaje="", bar_length=50):
    """Muestra barra de progreso"""
    porcentaje = (actual / total) * 100
    filled = int(bar_length * actual // total)
    bar = '█' * filled + '░' * (bar_length - filled)
    print(f'\r{mensaje} [{bar}] {porcentaje:.1f}% ({actual}/{total})', end='', flush=True)
    if actual == total:
        print()

def completar_brazilian_faltantes():
    """Completa los 3 archivos faltantes de Brazilian E-commerce"""
    print("=" * 70)
    print("COMPLETANDO ARCHIVOS FALTANTES - BRAZILIAN E-COMMERCE")
    print("=" * 70)
    
    base_path = Path("Portfolio/04_EXTREMO/data/brazilian_ecommerce_completo")
    base_path.mkdir(parents=True, exist_ok=True)
    
    # Cargar orders para usar en reviews y payments
    print("\n[INFO] Cargando orders.csv...")
    df_orders = pd.read_csv(base_path / 'orders.csv')
    print(f"[OK] {len(df_orders):,} ordenes cargadas")
    
    np.random.seed(42)
    random.seed(42)
    
    estados_br = ['SP', 'RJ', 'MG', 'RS', 'PR', 'SC', 'BA', 'GO', 'PE', 'CE', 'DF', 'ES', 'MT', 'MS', 'PA', 'PB', 'AM', 'RN', 'AL', 'PI']
    ciudades = [f'City_{i}' for i in range(1, 1001)]
    
    # 1. Order Reviews
    print("\n[1/3] Generando Order Reviews (300K)...")
    reviews_data = []
    scores = [1, 2, 3, 4, 5]
    orders_delivered = df_orders[df_orders['order_status'] == 'delivered'].head(300000)
    total_orders = len(orders_delivered)
    
    inicio = time.time()
    for i, (idx, order) in enumerate(orders_delivered.iterrows()):
        if np.random.random() > 0.3:  # 70% deja review
            fecha_delivered = pd.to_datetime(order['order_delivered_customer_date']) if pd.notna(order['order_delivered_customer_date']) else pd.to_datetime(order['order_purchase_timestamp']) + timedelta(days=10)
            fecha_review = fecha_delivered + timedelta(days=np.random.randint(1, 30))
            
            reviews_data.append({
                'review_id': f'REV-{len(reviews_data)+1:06d}',
                'order_id': order['order_id'],
                'review_score': random.choice(scores),
                'review_comment_title': f'Review Title {len(reviews_data)+1}' if np.random.random() > 0.2 else None,
                'review_comment_message': f'Review message for order {order["order_id"]}' if np.random.random() > 0.3 else None,
                'review_creation_date': fecha_review.strftime('%Y-%m-%d %H:%M:%S'),
                'review_answer_timestamp': (fecha_review + timedelta(days=np.random.randint(1, 7))).strftime('%Y-%m-%d %H:%M:%S') if np.random.random() > 0.2 else None
            })
        
        if (i + 1) % 30000 == 0:
            mostrar_progreso(i + 1, total_orders, "  Reviews")
    
    df_reviews = pd.DataFrame(reviews_data)
    df_reviews.to_csv(base_path / 'order_reviews.csv', index=False)
    tiempo = time.time() - inicio
    print(f"\n[OK] {len(df_reviews):,} reviews guardadas en {tiempo:.1f} segundos")
    
    # 2. Order Payments
    print("\n[2/3] Generando Order Payments (600K+)...")
    payments_data = []
    tipos_pago = ['credit_card', 'boleto', 'voucher', 'debit_card']
    total_orders = len(df_orders)
    
    inicio = time.time()
    for i, (idx, order) in enumerate(df_orders.iterrows()):
        num_pagos = np.random.randint(1, 4)
        total_pagado = round(np.random.uniform(20, 5000), 2)
        
        for j in range(num_pagos):
            payments_data.append({
                'order_id': order['order_id'],
                'payment_sequential': j + 1,
                'payment_type': random.choice(tipos_pago),
                'payment_installments': np.random.randint(1, 12),
                'payment_value': round(total_pagado / num_pagos, 2) if j < num_pagos - 1 else total_pagado - sum([round(total_pagado / num_pagos, 2) for _ in range(num_pagos - 1)])
            })
        
        if (i + 1) % 20000 == 0:
            mostrar_progreso(i + 1, total_orders, "  Pagos")
    
    df_payments = pd.DataFrame(payments_data)
    df_payments.to_csv(base_path / 'order_payments.csv', index=False)
    tiempo = time.time() - inicio
    print(f"\n[OK] {len(payments_data):,} pagos guardados en {tiempo:.1f} segundos")
    
    # 3. Geolocation
    print("\n[3/3] Generando Geolocation (10K)...")
    geolocation_data = []
    total = 10000
    
    inicio = time.time()
    for i in range(total):
        geolocation_data.append({
            'geolocation_zip_code_prefix': np.random.randint(1000, 99999),
            'geolocation_lat': round(np.random.uniform(-35, 5), 6),
            'geolocation_lng': round(np.random.uniform(-75, -30), 6),
            'geolocation_city': random.choice(ciudades),
            'geolocation_state': random.choice(estados_br)
        })
        
        if (i + 1) % 1000 == 0:
            mostrar_progreso(i + 1, total, "  Geolocalizaciones")
    
    df_geolocation = pd.DataFrame(geolocation_data)
    df_geolocation.to_csv(base_path / 'geolocation.csv', index=False)
    tiempo = time.time() - inicio
    print(f"\n[OK] {len(df_geolocation):,} ubicaciones guardadas en {tiempo:.1f} segundos")
    
    print("\n" + "=" * 70)
    print("[EXITO] Archivos faltantes completados")
    print("=" * 70)

def main():
    """Función principal"""
    inicio_total = time.time()
    
    completar_brazilian_faltantes()
    
    # Verificar resultado final
    base_path = Path("Portfolio/04_EXTREMO/data")
    total_archivos = len(list(base_path.rglob('*.csv')))
    
    tiempo_total = time.time() - inicio_total
    print(f"\nTotal archivos CSV: {total_archivos}/27")
    print(f"Tiempo total: {tiempo_total:.1f} segundos ({tiempo_total/60:.1f} minutos)")
    
    if total_archivos == 27:
        print("\n[EXITO] ¡TODOS LOS ARCHIVOS COMPLETADOS!")
    else:
        print(f"\n[INFO] Faltan {27 - total_archivos} archivos")

if __name__ == "__main__":
    main()

