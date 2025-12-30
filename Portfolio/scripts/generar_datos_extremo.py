"""
Generador de Datos EXTREMOS - Nivel SENIOR/EXPERTO/ÉLITE
Portfolio Data Analyst - Nivel EXTREMO

Genera datasets de Big Data con:
- Múltiples millones de registros
- Relaciones complejas
- Datos temporales extensos
- Múltiples fuentes integradas
- Datos para ML avanzado
- Detección de anomalías
- Análisis predictivo complejo
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta
import random
import warnings
warnings.filterwarnings('ignore')


def generar_big_data_time_series():
    """Genera dataset masivo de series temporales - Nivel EXTREMO"""
    print("\n" + "=" * 70)
    print("GENERANDO BIG DATA TIME SERIES - NIVEL EXTREMO")
    print("=" * 70)
    print("[INFO] Esto generara millones de registros. Puede tardar varios minutos...")
    
    base_path = Path("Portfolio/04_EXTREMO/data/store_sales_completo")
    base_path.mkdir(parents=True, exist_ok=True)
    
    np.random.seed(42)
    random.seed(42)
    
    # Stores - 200 tiendas
    print("\n[1] Generando Stores Dataset...")
    stores_data = []
    ciudades = [f'City_{i}' for i in range(1, 51)]
    estados = [f'State_{i}' for i in range(1, 21)]
    tipos = ['A', 'B', 'C', 'D', 'E']
    
    for i in range(200):
        stores_data.append({
            'store_nbr': i + 1,
            'city': random.choice(ciudades),
            'state': random.choice(estados),
            'type': random.choice(tipos),
            'cluster': np.random.randint(1, 21),
            'area_m2': np.random.randint(100, 5000),
            'empleados': np.random.randint(5, 50)
        })
    
    df_stores = pd.DataFrame(stores_data)
    df_stores.to_csv(base_path / 'stores.csv', index=False)
    print(f"   [OK] {len(df_stores)} tiendas guardadas")
    
    # Products - 10,000 productos
    print("\n[2] Generando Products Dataset...")
    productos_data = []
    categorias = [f'Category_{i}' for i in range(1, 51)]
    familias = [f'Family_{i}' for i in range(1, 201)]
    clases = [f'Class_{i}' for i in range(1, 501)]
    
    for i in range(10000):
        productos_data.append({
            'item_nbr': i + 1,
            'family': random.choice(familias),
            'class': random.choice(clases),
            'perishable': random.choice([0, 1]),
            'category': random.choice(categorias),
            'precio_base': round(np.random.uniform(1, 500), 2),
            'costo': round(np.random.uniform(0.5, 300), 2)
        })
    
    df_products = pd.DataFrame(productos_data)
    df_products.to_csv(base_path / 'products.csv', index=False)
    print(f"   [OK] {len(df_products)} productos guardados")
    
    # Oil prices - Datos históricos de petróleo (variable externa)
    print("\n[3] Generando Oil Prices Dataset...")
    fechas_oil = pd.date_range(start='2010-01-01', end='2024-12-31', freq='D')
    oil_data = []
    precio_base = 50.0
    
    for fecha in fechas_oil:
        # Simular volatilidad del petróleo
        cambio = np.random.normal(0, 2)
        precio_base += cambio
        precio_base = max(20, min(150, precio_base))  # Rango realista
        
        oil_data.append({
            'date': fecha.strftime('%Y-%m-%d'),
            'dcoilwtico': round(precio_base, 2)
        })
    
    df_oil = pd.DataFrame(oil_data)
    df_oil.to_csv(base_path / 'oil.csv', index=False)
    print(f"   [OK] {len(df_oil)} registros de petróleo guardados")
    
    # Holidays and Events - Calendario completo
    print("\n[4] Generando Holidays and Events Dataset...")
    holidays_data = []
    tipos_evento = ['Holiday', 'Event', 'Bridge', 'Transfer', 'Additional', 'Work Day']
    locales = ['National', 'Regional', 'Local']
    
    fechas_holidays = pd.date_range(start='2010-01-01', end='2024-12-31', freq='D')
    for fecha in fechas_holidays:
        if np.random.random() < 0.05:  # 5% probabilidad de ser festivo
            holidays_data.append({
                'date': fecha.strftime('%Y-%m-%d'),
                'type': random.choice(tipos_evento),
                'locale': random.choice(locales),
                'locale_name': random.choice(['Ecuador', 'National', 'Regional']),
                'description': f'Event {fecha.strftime("%Y-%m-%d")}',
                'transferred': random.choice([True, False])
            })
    
    df_holidays = pd.DataFrame(holidays_data)
    df_holidays.to_csv(base_path / 'holidays_events.csv', index=False)
    print(f"   [OK] {len(df_holidays)} eventos guardados")
    
    holiday_dates_set = set(h['date'] for h in holidays_data)
    
    # TRAIN DATA - MILLONES de registros
    print("\n[5] Generando TRAIN Dataset (BIG DATA)...")
    print("   [INFO] Generando 2+ millones de registros. Esto puede tardar 5-10 minutos...")
    
    fechas_train = pd.date_range(start='2013-01-01', end='2017-08-31', freq='D')
    train_data = []
    chunk_size = 50000
    total_chunks = (len(fechas_train) * 200 * 100) // chunk_size
    
    chunk_count = 0
    for fecha in fechas_train:
        for store_nbr in range(1, 201):  # 200 tiendas
            # Solo algunos productos por tienda cada día (optimización)
            productos_por_tienda = np.random.choice(range(1, 10001), size=min(100, np.random.randint(50, 200)), replace=False)
            
            for item_nbr in productos_por_tienda:
                # Simular ventas con estacionalidad y factores externos
                base_sales = np.random.randint(0, 100)
                
                # Factor día de la semana
                dia_semana = fecha.weekday()
                if dia_semana in [5, 6]:  # Fin de semana
                    base_sales *= 1.5
                
                # Factor festivo
                fecha_str = fecha.strftime('%Y-%m-%d')
                es_festivo = fecha_str in holiday_dates_set
                if es_festivo:
                    base_sales *= 1.3
                
                # Factor aleatorio
                base_sales = int(base_sales * np.random.uniform(0.5, 1.5))
                base_sales = max(0, base_sales)
                
                if base_sales > 0:  # Solo guardar si hay ventas
                    train_data.append({
                        'date': fecha_str,
                        'store_nbr': store_nbr,
                        'item_nbr': item_nbr,
                        'unit_sales': base_sales,
                        'onpromotion': bool(np.random.randint(0, 2))
                    })
                
                # Guardar en chunks para no llenar memoria
                if len(train_data) >= chunk_size:
                    chunk_count += 1
                    df_chunk = pd.DataFrame(train_data)
                    if chunk_count == 1:
                        df_chunk.to_csv(base_path / 'train.csv', index=False, mode='w', header=True)
                    else:
                        df_chunk.to_csv(base_path / 'train.csv', index=False, mode='a', header=False)
                    train_data = []
                    print(f"   [PROGRESO] Chunk {chunk_count} guardado ({chunk_count * chunk_size:,} registros)")
    
    # Guardar último chunk
    if train_data:
        df_chunk = pd.DataFrame(train_data)
        df_chunk.to_csv(base_path / 'train.csv', index=False, mode='a', header=False)
        chunk_count += 1
    
    # Contar registros finales
    total_registros = sum(1 for _ in open(base_path / 'train.csv')) - 1  # -1 por header
    print(f"   [OK] {total_registros:,} registros de ventas guardados en train.csv")
    
    # Transactions - Transacciones diarias por tienda
    print("\n[6] Generando Transactions Dataset...")
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
    print(f"   [OK] {len(df_transactions)} registros de transacciones guardados")
    
    print("\n" + "=" * 70)
    print("[EXITO] Big Data Time Series generado correctamente")
    print(f"Total aproximado: {total_registros:,} registros de ventas")
    print("=" * 70)


def generar_brazilian_ecommerce_completo():
    """Genera dataset completo de e-commerce brasileño - Nivel EXTREMO"""
    print("\n" + "=" * 70)
    print("GENERANDO BRAZILIAN E-COMMERCE COMPLETO - NIVEL EXTREMO")
    print("=" * 70)
    
    base_path = Path("Portfolio/04_EXTREMO/data/brazilian_ecommerce_completo")
    base_path.mkdir(parents=True, exist_ok=True)
    
    np.random.seed(42)
    random.seed(42)
    
    # Customers - 100,000 clientes
    print("\n[1] Generando Customers Dataset (100K clientes)...")
    customers_data = []
    estados_br = ['SP', 'RJ', 'MG', 'RS', 'PR', 'SC', 'BA', 'GO', 'PE', 'CE', 'DF', 'ES', 'MT', 'MS', 'PA', 'PB', 'AM', 'RN', 'AL', 'PI']
    ciudades = [f'City_{i}' for i in range(1, 1001)]
    
    for i in range(100000):
        customers_data.append({
            'customer_id': f'CUST-{i+1:06d}',
            'customer_unique_id': f'UNIQ-{np.random.randint(1, 50000):06d}',
            'customer_zip_code_prefix': np.random.randint(1000, 99999),
            'customer_city': random.choice(ciudades),
            'customer_state': random.choice(estados_br)
        })
    
    df_customers = pd.DataFrame(customers_data)
    df_customers.to_csv(base_path / 'customers.csv', index=False)
    print(f"   [OK] {len(df_customers):,} clientes guardados")
    
    # Sellers - 10,000 vendedores
    print("\n[2] Generando Sellers Dataset...")
    sellers_data = []
    for i in range(10000):
        sellers_data.append({
            'seller_id': f'SELL-{i+1:06d}',
            'seller_zip_code_prefix': np.random.randint(1000, 99999),
            'seller_city': random.choice(ciudades),
            'seller_state': random.choice(estados_br)
        })
    
    df_sellers = pd.DataFrame(sellers_data)
    df_sellers.to_csv(base_path / 'sellers.csv', index=False)
    print(f"   [OK] {len(df_sellers):,} vendedores guardados")
    
    # Products - 50,000 productos
    print("\n[3] Generando Products Dataset...")
    products_data = []
    categorias = [f'Category_{i}' for i in range(1, 101)]
    nombres_productos = [f'Product_{i}' for i in range(1, 50001)]
    
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
    
    df_products = pd.DataFrame(products_data)
    df_products.to_csv(base_path / 'products.csv', index=False)
    print(f"   [OK] {len(df_products):,} productos guardados")
    
    # Orders - 200,000 órdenes
    print("\n[4] Generando Orders Dataset (200K órdenes)...")
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
    
    df_orders = pd.DataFrame(orders_data)
    df_orders.to_csv(base_path / 'orders.csv', index=False)
    print(f"   [OK] {len(df_orders):,} órdenes guardadas")
    
    # Order Items - 500,000 items
    print("\n[5] Generando Order Items Dataset (500K items)...")
    order_items_data = []
    chunk_size = 50000
    
    for i, order in enumerate(orders_data):
        if i % 10000 == 0:
            print(f"   [PROGRESO] Procesando orden {i:,}/{len(orders_data):,}")
        
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
        
        # Guardar en chunks
        if len(order_items_data) >= chunk_size:
            df_chunk = pd.DataFrame(order_items_data)
            if i == chunk_size:
                df_chunk.to_csv(base_path / 'order_items.csv', index=False, mode='w', header=True)
            else:
                df_chunk.to_csv(base_path / 'order_items.csv', index=False, mode='a', header=False)
            order_items_data = []
    
    # Guardar último chunk
    if order_items_data:
        df_chunk = pd.DataFrame(order_items_data)
        df_chunk.to_csv(base_path / 'order_items.csv', index=False, mode='a', header=False)
    
    total_items = sum(1 for _ in open(base_path / 'order_items.csv')) - 1
    print(f"   [OK] {total_items:,} items guardados")
    
    # Order Reviews - 300,000 reviews
    print("\n[6] Generando Order Reviews Dataset...")
    reviews_data = []
    scores = [1, 2, 3, 4, 5]
    
    for i, order in enumerate(orders_data[:300000]):
        if order['order_status'] == 'delivered' and np.random.random() > 0.3:  # 70% deja review
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
    
    df_reviews = pd.DataFrame(reviews_data)
    df_reviews.to_csv(base_path / 'order_reviews.csv', index=False)
    print(f"   [OK] {len(df_reviews):,} reviews guardadas")
    
    # Order Payments - 600,000 pagos
    print("\n[7] Generando Order Payments Dataset...")
    payments_data = []
    tipos_pago = ['credit_card', 'boleto', 'voucher', 'debit_card']
    
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
    
    df_payments = pd.DataFrame(payments_data)
    df_payments.to_csv(base_path / 'order_payments.csv', index=False)
    print(f"   [OK] {len(payments_data):,} pagos guardados")
    
    # Geolocation - Datos geográficos
    print("\n[8] Generando Geolocation Dataset...")
    geolocation_data = []
    for i in range(10000):
        geolocation_data.append({
            'geolocation_zip_code_prefix': np.random.randint(1000, 99999),
            'geolocation_lat': round(np.random.uniform(-35, 5), 6),
            'geolocation_lng': round(np.random.uniform(-75, -30), 6),
            'geolocation_city': random.choice(ciudades),
            'geolocation_state': random.choice(estados_br)
        })
    
    df_geolocation = pd.DataFrame(geolocation_data)
    df_geolocation.to_csv(base_path / 'geolocation.csv', index=False)
    print(f"   [OK] {len(df_geolocation):,} ubicaciones guardadas")
    
    print("\n" + "=" * 70)
    print("[EXITO] Brazilian E-commerce COMPLETO generado")
    print(f"Total: ~1.2 millones de registros")
    print("=" * 70)


def generar_youtube_trending():
    """Genera dataset masivo de YouTube Trending - Nivel EXTREMO"""
    print("\n" + "=" * 70)
    print("GENERANDO YOUTUBE TRENDING DATASET - NIVEL EXTREMO")
    print("=" * 70)
    
    base_path = Path("Portfolio/04_EXTREMO/data/youtube_trending")
    base_path.mkdir(parents=True, exist_ok=True)
    
    np.random.seed(42)
    random.seed(42)
    
    # Categorías de YouTube
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
    
    # Países
    paises = ['US', 'GB', 'CA', 'AU', 'DE', 'FR', 'ES', 'IT', 'BR', 'MX', 'IN', 'JP', 'KR']
    
    print("\n[1] Generando YouTube Trending Dataset por país...")
    fechas = pd.date_range(start='2017-11-14', end='2018-06-14', freq='D')
    
    for pais in paises:
        print(f"\n   Generando datos para {pais}...")
        youtube_data = []
        
        for fecha in fechas:
            # 50-200 videos trending por día por país
            num_videos = np.random.randint(50, 201)
            
            for i in range(num_videos):
                video_id = f'VIDEO_{pais}_{fecha.strftime("%Y%m%d")}_{i+1:04d}'
                categoria_id = random.choice(list(categorias.keys()))
                
                # Métricas realistas
                views = np.random.randint(10000, 50000000)
                likes = int(views * np.random.uniform(0.01, 0.05))
                dislikes = int(likes * np.random.uniform(0.01, 0.10))
                comment_count = int(views * np.random.uniform(0.001, 0.01))
                
                # Título y descripción
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
        
        df_youtube = pd.DataFrame(youtube_data)
        df_youtube.to_csv(base_path / f'youtube_trending_{pais}.csv', index=False)
        print(f"   [OK] {len(df_youtube):,} videos guardados para {pais}")
    
    print("\n" + "=" * 70)
    print("[EXITO] YouTube Trending Dataset generado")
    print(f"Total: ~{sum([len(pd.read_csv(base_path / f'youtube_trending_{pais}.csv')) for pais in paises]):,} videos")
    print("=" * 70)


def main():
    """Función principal"""
    print("=" * 70)
    print("GENERADOR DE DATOS EXTREMOS - NIVEL SENIOR/EXPERTO/ELITE")
    print("=" * 70)
    print("\nEste script genera datasets de BIG DATA para nivel EXTREMO:")
    print("  - Store Sales Time Series: 2+ millones de registros")
    print("  - Brazilian E-commerce: 1.2+ millones de registros")
    print("  - YouTube Trending: 100K+ videos por país")
    print("\n[ADVERTENCIA] Esto generara archivos grandes (100+ MB)")
    print("y puede tardar 10-20 minutos en completarse.")
    
    print("\nGenerando datos automaticamente...")
    
    try:
        generar_big_data_time_series()
        generar_brazilian_ecommerce_completo()
        generar_youtube_trending()
        
        print("\n" + "=" * 70)
        print("[EXITO] TODOS LOS DATOS EXTREMOS GENERADOS")
        print("=" * 70)
        print("\nLos datasets estan listos para:")
        print("  - Analisis de Big Data")
        print("  - Machine Learning avanzado")
        print("  - Optimizacion extrema de PostgreSQL")
        print("  - Procesamiento en chunks")
        print("  - Analisis predictivo complejo")
        print("  - Deteccion de anomalias")
        print("\n[INFO] Estos datasets requieren:")
        print("  - Procesamiento en chunks")
        print("  - Optimizacion avanzada de PostgreSQL")
        print("  - Particionado de tablas")
        print("  - Indices avanzados")
        print("  - Vistas materializadas")
        
    except Exception as e:
        print(f"\n[ERROR] Error al generar datos: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

