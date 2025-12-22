"""
Generador de Datos EXTREMOS con Progreso en Tiempo Real
Muestra el progreso mientras genera los datos
"""

import sys
import os
from pathlib import Path
import time
from datetime import datetime

# Configurar encoding para Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Importar pandas y numpy
import pandas as pd
import numpy as np
from datetime import timedelta
import random
import warnings
warnings.filterwarnings('ignore')


def mostrar_progreso(actual, total, mensaje="", bar_length=50):
    """Muestra una barra de progreso"""
    porcentaje = (actual / total) * 100
    filled = int(bar_length * actual // total)
    bar = '█' * filled + '░' * (bar_length - filled)
    print(f'\r{mensaje} [{bar}] {porcentaje:.1f}% ({actual}/{total})', end='', flush=True)
    if actual == total:
        print()  # Nueva línea al completar


def generar_transactions_tiempo_real():
    """Genera transactions.csv con progreso en tiempo real"""
    print("\n" + "=" * 70)
    print("GENERANDO TRANSACTIONS.CSV")
    print("=" * 70)
    
    base_path = Path("Portfolio/04_EXTREMO/data/store_sales_completo")
    base_path.mkdir(parents=True, exist_ok=True)
    
    np.random.seed(42)
    random.seed(42)
    
    print("\n[INFO] Generando transacciones diarias por tienda...")
    transactions_data = []
    fechas_trans = pd.date_range(start='2013-01-01', end='2017-08-31', freq='D')
    fechas_sample = fechas_trans[::7]  # Una vez por semana
    total_fechas = len(fechas_sample)
    total_stores = 200
    total_iteraciones = total_fechas * total_stores
    
    contador = 0
    inicio = time.time()
    
    for idx_fecha, fecha in enumerate(fechas_sample):
        for store_nbr in range(1, 201):
            transactions_data.append({
                'date': fecha.strftime('%Y-%m-%d'),
                'store_nbr': store_nbr,
                'transactions': np.random.randint(100, 10000)
            })
            
            contador += 1
            if contador % 1000 == 0 or contador == total_iteraciones:
                mostrar_progreso(contador, total_iteraciones, "Procesando transacciones")
    
    print("\n[INFO] Guardando archivo...")
    df_transactions = pd.DataFrame(transactions_data)
    df_transactions.to_csv(base_path / 'transactions.csv', index=False)
    
    tiempo_total = time.time() - inicio
    print(f"[OK] {len(df_transactions):,} registros guardados en {tiempo_total:.1f} segundos")
    return True


def generar_brazilian_ecommerce_tiempo_real():
    """Genera Brazilian E-commerce con progreso en tiempo real"""
    print("\n" + "=" * 70)
    print("GENERANDO BRAZILIAN E-COMMERCE COMPLETO")
    print("=" * 70)
    
    base_path = Path("Portfolio/04_EXTREMO/data/brazilian_ecommerce_completo")
    base_path.mkdir(parents=True, exist_ok=True)
    
    np.random.seed(42)
    random.seed(42)
    
    estados_br = ['SP', 'RJ', 'MG', 'RS', 'PR', 'SC', 'BA', 'GO', 'PE', 'CE', 'DF', 'ES', 'MT', 'MS', 'PA', 'PB', 'AM', 'RN', 'AL', 'PI']
    ciudades = [f'City_{i}' for i in range(1, 1001)]
    
    # 1. Customers
    print("\n[1/8] Generando Customers (100K)...")
    customers_data = []
    inicio = time.time()
    for i in range(100000):
        customers_data.append({
            'customer_id': f'CUST-{i+1:06d}',
            'customer_unique_id': f'UNIQ-{np.random.randint(1, 50000):06d}',
            'customer_zip_code_prefix': np.random.randint(1000, 99999),
            'customer_city': random.choice(ciudades),
            'customer_state': random.choice(estados_br)
        })
        if (i + 1) % 10000 == 0:
            mostrar_progreso(i + 1, 100000, "  Clientes")
    
    df_customers = pd.DataFrame(customers_data)
    df_customers.to_csv(base_path / 'customers.csv', index=False)
    print(f"  [OK] {len(df_customers):,} clientes guardados")
    
    # 2. Sellers
    print("\n[2/8] Generando Sellers (10K)...")
    sellers_data = []
    for i in range(10000):
        sellers_data.append({
            'seller_id': f'SELL-{i+1:06d}',
            'seller_zip_code_prefix': np.random.randint(1000, 99999),
            'seller_city': random.choice(ciudades),
            'seller_state': random.choice(estados_br)
        })
        if (i + 1) % 1000 == 0:
            mostrar_progreso(i + 1, 10000, "  Vendedores")
    
    df_sellers = pd.DataFrame(sellers_data)
    df_sellers.to_csv(base_path / 'sellers.csv', index=False)
    print(f"  [OK] {len(df_sellers):,} vendedores guardados")
    
    # 3. Products
    print("\n[3/8] Generando Products (50K)...")
    products_data = []
    categorias = [f'Category_{i}' for i in range(1, 101)]
    
    for i in range(50000):
        products_data.append({
            'product_id': f'PROD-{i+1:06d}',
            'product_category_name': random.choice(categorias),
            'product_name_lenght': np.random.randint(10, 100),
            'product_description_lenght': np.random.randint(50, 500),
            'product_photos_qty': np.random.randint(1, 10),
            'product_weight_g': np.random.randint(100, 50000),
            'product_length_cm': np.random.randint(10, 200),
            'product_height_cm': np.random.randint(5, 100),
            'product_width_cm': np.random.randint(10, 150)
        })
        if (i + 1) % 5000 == 0:
            mostrar_progreso(i + 1, 50000, "  Productos")
    
    df_products = pd.DataFrame(products_data)
    df_products.to_csv(base_path / 'products.csv', index=False)
    print(f"  [OK] {len(df_products):,} productos guardados")
    
    # 4. Orders
    print("\n[4/8] Generando Orders (200K)...")
    fechas = pd.date_range(start='2016-01-01', end='2018-12-31', freq='D')
    orders_data = []
    estados_orden = ['delivered', 'shipped', 'processing', 'approved', 'cancelled', 'unavailable']
    
    for i in range(200000):
        fecha_orden = random.choice(fechas)
        customer_id = f'CUST-{np.random.randint(1, 100001):06d}'
        estado = random.choice(estados_orden)
        
        orders_data.append({
            'order_id': f'ORD-{i+1:06d}',
            'customer_id': customer_id,
            'order_status': estado,
            'order_purchase_timestamp': fecha_orden.strftime('%Y-%m-%d %H:%M:%S'),
            'order_approved_at': (fecha_orden + timedelta(hours=np.random.randint(0, 24))).strftime('%Y-%m-%d %H:%M:%S') if estado != 'cancelled' else None,
            'order_delivered_carrier_date': (fecha_orden + timedelta(days=np.random.randint(1, 5))).strftime('%Y-%m-%d %H:%M:%S') if estado in ['delivered', 'shipped'] else None,
            'order_delivered_customer_date': (fecha_orden + timedelta(days=np.random.randint(5, 15))).strftime('%Y-%m-%d %H:%M:%S') if estado == 'delivered' else None,
            'order_estimated_delivery_date': (fecha_orden + timedelta(days=np.random.randint(7, 20))).strftime('%Y-%m-%d %H:%M:%S')
        })
        if (i + 1) % 20000 == 0:
            mostrar_progreso(i + 1, 200000, "  Ordenes")
    
    df_orders = pd.DataFrame(orders_data)
    df_orders.to_csv(base_path / 'orders.csv', index=False)
    print(f"  [OK] {len(df_orders):,} ordenes guardadas")
    
    # 5. Order Items (en chunks)
    print("\n[5/8] Generando Order Items (500K+)...")
    order_items_data = []
    chunk_size = 50000
    total_items_esperados = 0
    
    # Estimar total de items
    for order in orders_data:
        total_items_esperados += np.random.randint(1, 6)
    
    contador_items = 0
    for i, order in enumerate(orders_data):
        num_items = np.random.randint(1, 6)
        for j in range(num_items):
            order_items_data.append({
                'order_id': order['order_id'],
                'order_item_id': j + 1,
                'product_id': f'PROD-{np.random.randint(1, 50001):06d}',
                'seller_id': f'SELL-{np.random.randint(1, 10001):06d}',
                'shipping_limit_date': (pd.to_datetime(order['order_purchase_timestamp']) + timedelta(days=np.random.randint(5, 15))).strftime('%Y-%m-%d %H:%M:%S'),
                'price': round(np.random.uniform(10, 2000), 2),
                'freight_value': round(np.random.uniform(5, 100), 2)
            })
            contador_items += 1
        
        # Guardar en chunks
        if len(order_items_data) >= chunk_size:
            df_chunk = pd.DataFrame(order_items_data)
            if i == chunk_size:
                df_chunk.to_csv(base_path / 'order_items.csv', index=False, mode='w', header=True)
            else:
                df_chunk.to_csv(base_path / 'order_items.csv', index=False, mode='a', header=False)
            mostrar_progreso(contador_items, 500000, "  Items")
            order_items_data = []
        
        if (i + 1) % 20000 == 0:
            mostrar_progreso(i + 1, 200000, "  Procesando ordenes")
    
    # Guardar último chunk
    if order_items_data:
        df_chunk = pd.DataFrame(order_items_data)
        df_chunk.to_csv(base_path / 'order_items.csv', index=False, mode='a', header=False)
    
    total_items = sum(1 for _ in open(base_path / 'order_items.csv')) - 1
    print(f"  [OK] {total_items:,} items guardados")
    
    # 6. Order Reviews
    print("\n[6/8] Generando Order Reviews (300K)...")
    reviews_data = []
    scores = [1, 2, 3, 4, 5]
    contador_reviews = 0
    
    for i, order in enumerate(orders_data[:300000]):
        if order['order_status'] == 'delivered' and np.random.random() > 0.3:
            fecha_review = pd.to_datetime(order['order_delivered_customer_date']) + timedelta(days=np.random.randint(1, 30))
            reviews_data.append({
                'review_id': f'REV-{i+1:06d}',
                'order_id': order['order_id'],
                'review_score': random.choice(scores),
                'review_comment_title': f'Review Title {i+1}' if np.random.random() > 0.2 else None,
                'review_comment_message': f'Review message for order {order["order_id"]}' if np.random.random() > 0.3 else None,
                'review_creation_date': fecha_review.strftime('%Y-%m-%d %H:%M:%S'),
                'review_answer_timestamp': (fecha_review + timedelta(days=np.random.randint(1, 7))).strftime('%Y-%m-%d %H:%M:%S') if np.random.random() > 0.2 else None
            })
            contador_reviews += 1
        
        if (i + 1) % 30000 == 0:
            mostrar_progreso(i + 1, 300000, "  Reviews")
    
    df_reviews = pd.DataFrame(reviews_data)
    df_reviews.to_csv(base_path / 'order_reviews.csv', index=False)
    print(f"  [OK] {len(df_reviews):,} reviews guardadas")
    
    # 7. Order Payments
    print("\n[7/8] Generando Order Payments (600K+)...")
    payments_data = []
    tipos_pago = ['credit_card', 'boleto', 'voucher', 'debit_card']
    contador_pagos = 0
    
    for i, order in enumerate(orders_data):
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
            contador_pagos += 1
        
        if (i + 1) % 20000 == 0:
            mostrar_progreso(i + 1, 200000, "  Pagos")
    
    df_payments = pd.DataFrame(payments_data)
    df_payments.to_csv(base_path / 'order_payments.csv', index=False)
    print(f"  [OK] {len(payments_data):,} pagos guardados")
    
    # 8. Geolocation
    print("\n[8/8] Generando Geolocation (10K)...")
    geolocation_data = []
    for i in range(10000):
        geolocation_data.append({
            'geolocation_zip_code_prefix': np.random.randint(1000, 99999),
            'geolocation_lat': round(np.random.uniform(-35, 5), 6),
            'geolocation_lng': round(np.random.uniform(-75, -30), 6),
            'geolocation_city': random.choice(ciudades),
            'geolocation_state': random.choice(estados_br)
        })
        if (i + 1) % 1000 == 0:
            mostrar_progreso(i + 1, 10000, "  Geolocalizaciones")
    
    df_geolocation = pd.DataFrame(geolocation_data)
    df_geolocation.to_csv(base_path / 'geolocation.csv', index=False)
    print(f"  [OK] {len(df_geolocation):,} ubicaciones guardadas")
    
    print("\n" + "=" * 70)
    print("[EXITO] Brazilian E-commerce COMPLETO generado")
    print("=" * 70)
    return True


def generar_youtube_trending_tiempo_real():
    """Genera YouTube Trending con progreso en tiempo real"""
    print("\n" + "=" * 70)
    print("GENERANDO YOUTUBE TRENDING DATASET")
    print("=" * 70)
    
    base_path = Path("Portfolio/04_EXTREMO/data/youtube_trending")
    base_path.mkdir(parents=True, exist_ok=True)
    
    np.random.seed(42)
    random.seed(42)
    
    categorias = {
        1: 'Film & Animation',
        2: 'Autos & Vehicles',
        10: 'Music',
        15: 'Pets & Animals',
        17: 'Sports',
        19: 'Travel & Events',
        20: 'Gaming',
        22: 'People & Blogs',
        23: 'Comedy',
        24: 'Entertainment',
        25: 'News & Politics',
        26: 'Howto & Style',
        27: 'Education',
        28: 'Science & Technology'
    }
    
    paises = ['US', 'GB', 'CA', 'AU', 'DE', 'FR', 'ES', 'IT', 'BR', 'MX', 'IN', 'JP', 'KR']
    fechas = pd.date_range(start='2017-11-14', end='2018-06-14', freq='D')
    total_paises = len(paises)
    
    print(f"\n[INFO] Generando datos para {total_paises} paises...")
    
    for idx_pais, pais in enumerate(paises):
        print(f"\n[{idx_pais + 1}/{total_paises}] Generando YouTube Trending para {pais}...")
        youtube_data = []
        total_videos_esperados = len(fechas) * 125  # Promedio de 125 videos por día
        
        contador = 0
        for fecha in fechas:
            num_videos = np.random.randint(50, 201)
            
            for i in range(num_videos):
                video_id = f'VIDEO_{pais}_{fecha.strftime("%Y%m%d")}_{i+1:04d}'
                categoria_id = random.choice(list(categorias.keys()))
                
                views = np.random.randint(10000, 50000000)
                likes = int(views * np.random.uniform(0.01, 0.05))
                dislikes = int(likes * np.random.uniform(0.01, 0.10))
                comment_count = int(views * np.random.uniform(0.001, 0.01))
                
                titulo = f'Video Trending {categoria_id} {fecha.strftime("%Y-%m-%d")}'
                canal = f'Channel_{np.random.randint(1, 10000)}'
                
                youtube_data.append({
                    'video_id': video_id,
                    'trending_date': fecha.strftime('%y.%d.%m'),
                    'title': titulo,
                    'channel_title': canal,
                    'category_id': categoria_id,
                    'publish_time': (fecha - timedelta(days=np.random.randint(1, 365))).strftime('%Y-%m-%dT%H:%M:%S.000Z'),
                    'tags': f'"{random.choice(["funny", "music", "gaming", "tutorial", "vlog"])}"',
                    'views': views,
                    'likes': likes,
                    'dislikes': dislikes,
                    'comment_count': comment_count,
                    'thumbnail_link': f'https://i.ytimg.com/vi/{video_id}/default.jpg',
                    'comments_disabled': random.choice([True, False]),
                    'ratings_disabled': random.choice([True, False]),
                    'video_error_or_removed': random.choice([True, False]) if np.random.random() < 0.01 else False,
                    'description': f'Description for {titulo}'
                })
                contador += 1
            
            if len(fechas) > 0 and fecha == fechas[len(fechas)//2]:
                mostrar_progreso(contador, total_videos_esperados, f"  Videos {pais}")
        
        df_youtube = pd.DataFrame(youtube_data)
        df_youtube.to_csv(base_path / f'youtube_trending_{pais}.csv', index=False)
        print(f"  [OK] {len(df_youtube):,} videos guardados para {pais}")
    
    print("\n" + "=" * 70)
    print("[EXITO] YouTube Trending Dataset generado")
    print("=" * 70)
    return True


def main():
    """Función principal con progreso en tiempo real"""
    print("=" * 70)
    print("GENERADOR DE DATOS EXTREMOS - PROGRESO EN TIEMPO REAL")
    print("=" * 70)
    
    inicio_total = time.time()
    
    # Verificar qué falta
    base_path = Path("Portfolio/04_EXTREMO/data")
    
    resultados = []
    
    # 1. Transactions
    transactions_path = base_path / 'store_sales_completo' / 'transactions.csv'
    if not transactions_path.exists():
        print("\n[PENDIENTE] transactions.csv")
        resultados.append(("transactions.csv", generar_transactions_tiempo_real()))
    else:
        print("\n[OK] transactions.csv ya existe")
    
    # 2. Brazilian E-commerce
    brazilian_path = base_path / 'brazilian_ecommerce_completo'
    if not brazilian_path.exists() or len(list(brazilian_path.glob('*.csv'))) == 0:
        print("\n[PENDIENTE] Brazilian E-commerce Completo")
        resultados.append(("Brazilian E-commerce", generar_brazilian_ecommerce_tiempo_real()))
    else:
        print("\n[OK] Brazilian E-commerce ya existe")
    
    # 3. YouTube Trending
    youtube_path = base_path / 'youtube_trending'
    if not youtube_path.exists() or len(list(youtube_path.glob('*.csv'))) == 0:
        print("\n[PENDIENTE] YouTube Trending")
        resultados.append(("YouTube Trending", generar_youtube_trending_tiempo_real()))
    else:
        print("\n[OK] YouTube Trending ya existe")
    
    # Resumen final
    tiempo_total = time.time() - inicio_total
    print("\n" + "=" * 70)
    print("RESUMEN FINAL")
    print("=" * 70)
    
    total_archivos = len(list(base_path.rglob('*.csv')))
    print(f"\nTotal archivos CSV generados: {total_archivos}/27")
    print(f"Tiempo total: {tiempo_total:.1f} segundos ({tiempo_total/60:.1f} minutos)")
    
    print("\n[EXITO] Generacion completada!")
    print("=" * 70)


if __name__ == "__main__":
    main()

