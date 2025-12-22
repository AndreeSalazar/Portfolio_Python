"""
Generador de Datos Sintéticos para Portfolio
Crea datasets realistas para demostrar el stack completo mientras se configuran credenciales de Kaggle
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timedelta
import random

def generar_datos_basico():
    """Genera datos sintéticos para nivel básico"""
    print("=" * 70)
    print("Generando datos sinteticos - NIVEL BASICO")
    print("=" * 70)
    
    base_path = Path("Portfolio/01_Basico/data")
    base_path.mkdir(parents=True, exist_ok=True)
    (base_path / 'retail_sales').mkdir(parents=True, exist_ok=True)
    (base_path / 'superstore').mkdir(parents=True, exist_ok=True)
    (base_path / 'hr_analytics').mkdir(parents=True, exist_ok=True)
    
    np.random.seed(42)
    random.seed(42)
    
    # 1. Retail Sales Dataset
    print("\n[1] Generando Retail Sales Dataset...")
    fechas = pd.date_range(start='2023-01-01', end='2024-12-31', freq='D')
    productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E']
    regiones = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro']
    
    ventas_data = []
    for i in range(5000):
        fecha = random.choice(fechas)
        producto = random.choice(productos)
        region = random.choice(regiones)
        cantidad = np.random.randint(1, 50)
        precio_unitario = round(np.random.uniform(10, 500), 2)
        total = round(cantidad * precio_unitario, 2)
        
        ventas_data.append({
            'fecha': fecha,
            'producto': producto,
            'region': region,
            'cantidad': cantidad,
            'precio_unitario': precio_unitario,
            'total': total,
            'vendedor': f'Vendedor_{np.random.randint(1, 20)}',
            'cliente_id': np.random.randint(1, 500)
        })
    
    df_ventas = pd.DataFrame(ventas_data)
    df_ventas.to_csv(base_path / 'retail_sales/ventas.csv', index=False)
    print(f"   [OK] {len(df_ventas)} registros guardados")
    
    # Productos
    productos_data = []
    for i, prod in enumerate(productos, 1):
        productos_data.append({
            'producto_id': i,
            'nombre': prod,
            'categoria': random.choice(['Electronica', 'Ropa', 'Hogar', 'Deportes']),
            'precio': round(np.random.uniform(10, 500), 2)
        })
    
    df_productos = pd.DataFrame(productos_data)
    df_productos.to_csv(base_path / 'retail_sales/productos.csv', index=False)
    print(f"   [OK] {len(df_productos)} productos guardados")
    
    # Clientes
    ciudades = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao']
    clientes_data = []
    for i in range(1, 501):
        clientes_data.append({
            'cliente_id': i,
            'nombre': f'Cliente_{i}',
            'ciudad': random.choice(ciudades),
            'segmento': random.choice(['Consumer', 'Corporate', 'Home Office'])
        })
    
    df_clientes = pd.DataFrame(clientes_data)
    df_clientes.to_csv(base_path / 'retail_sales/clientes.csv', index=False)
    print(f"   [OK] {len(df_clientes)} clientes guardados")
    
    # 2. Superstore Dataset
    print("\n[2] Generando Superstore Dataset...")
    superstore_data = []
    categorias = ['Furniture', 'Office Supplies', 'Technology']
    subcategorias = {
        'Furniture': ['Chairs', 'Tables', 'Bookcases'],
        'Office Supplies': ['Paper', 'Binders', 'Storage'],
        'Technology': ['Phones', 'Computers', 'Accessories']
    }
    
    for i in range(3000):
        fecha_orden = random.choice(fechas)
        fecha_envio = fecha_orden + timedelta(days=np.random.randint(1, 10))
        categoria = random.choice(categorias)
        subcategoria = random.choice(subcategorias[categoria])
        
        superstore_data.append({
            'Order ID': f'ORD-{i+1:05d}',
            'Order Date': fecha_orden.strftime('%Y-%m-%d'),
            'Ship Date': fecha_envio.strftime('%Y-%m-%d'),
            'Customer Name': f'Customer_{np.random.randint(1, 200)}',
            'Segment': random.choice(['Consumer', 'Corporate', 'Home Office']),
            'Country': 'Spain',
            'City': random.choice(ciudades),
            'State': random.choice(['Madrid', 'Cataluna', 'Valencia', 'Andalucia']),
            'Region': random.choice(regiones),
            'Product ID': f'PROD-{np.random.randint(1, 100):03d}',
            'Category': categoria,
            'Sub-Category': subcategoria,
            'Product Name': f'{subcategoria} {np.random.randint(1, 50)}',
            'Sales': round(np.random.uniform(10, 2000), 2),
            'Quantity': np.random.randint(1, 10),
            'Discount': round(np.random.uniform(0, 0.3), 2),
            'Profit': round(np.random.uniform(-100, 500), 2)
        })
    
    df_superstore = pd.DataFrame(superstore_data)
    df_superstore.to_csv(base_path / 'superstore/superstore.csv', index=False)
    print(f"   [OK] {len(df_superstore)} registros guardados")
    
    # 3. HR Analytics Dataset
    print("\n[3] Generando HR Analytics Dataset...")
    departamentos = ['IT', 'Sales', 'Marketing', 'HR', 'Finance', 'Operations']
    posiciones = {
        'IT': ['Developer', 'Data Analyst', 'SysAdmin'],
        'Sales': ['Sales Rep', 'Sales Manager', 'Account Manager'],
        'Marketing': ['Marketing Specialist', 'Content Manager', 'SEO Specialist'],
        'HR': ['HR Manager', 'Recruiter', 'HR Generalist'],
        'Finance': ['Accountant', 'Financial Analyst', 'Controller'],
        'Operations': ['Operations Manager', 'Logistics', 'Supply Chain']
    }
    
    hr_data = []
    for i in range(1500):
        dept = random.choice(departamentos)
        pos = random.choice(posiciones[dept])
        edad = np.random.randint(22, 65)
        salario_base = np.random.randint(30000, 100000)
        experiencia = np.random.randint(0, 20)
        
        hr_data.append({
            'employee_id': i + 1,
            'nombre': f'Empleado_{i+1}',
            'departamento': dept,
            'posicion': pos,
            'edad': edad,
            'salario': salario_base + (experiencia * 2000),
            'experiencia_anos': experiencia,
            'performance_score': np.random.randint(1, 6),
            'satisfaction_score': np.random.randint(1, 6),
            'fecha_contratacion': (datetime.now() - timedelta(days=experiencia*365)).strftime('%Y-%m-%d')
        })
    
    df_hr = pd.DataFrame(hr_data)
    df_hr.to_csv(base_path / 'hr_analytics/hr_data.csv', index=False)
    print(f"   [OK] {len(df_hr)} registros guardados")
    
    print("\n" + "=" * 70)
    print("[EXITO] Datos basicos generados correctamente")
    print("=" * 70)


def generar_datos_intermedio():
    """Genera datos sintéticos para nivel intermedio"""
    print("\n" + "=" * 70)
    print("Generando datos sinteticos - NIVEL INTERMEDIO")
    print("=" * 70)
    
    base_path = Path("Portfolio/02_Intermedio/data")
    base_path.mkdir(parents=True, exist_ok=True)
    (base_path / 'ecommerce').mkdir(parents=True, exist_ok=True)
    (base_path / 'online_retail').mkdir(parents=True, exist_ok=True)
    (base_path / 'marketing').mkdir(parents=True, exist_ok=True)
    
    np.random.seed(42)
    random.seed(42)
    
    # 1. E-commerce Dataset
    print("\n[1] Generando E-commerce Dataset...")
    fechas = pd.date_range(start='2022-01-01', end='2024-12-31', freq='D')
    paises = ['Spain', 'France', 'Germany', 'Italy', 'UK', 'Portugal']
    
    # Customers
    customers_data = []
    for i in range(1000):
        customers_data.append({
            'customer_id': i + 1,
            'nombre': f'Customer_{i+1}',
            'email': f'customer{i+1}@email.com',
            'pais': random.choice(paises),
            'fecha_registro': random.choice(fechas[:365]).strftime('%Y-%m-%d')
        })
    
    df_customers = pd.DataFrame(customers_data)
    df_customers.to_csv(base_path / 'ecommerce/customers.csv', index=False)
    print(f"   [OK] {len(df_customers)} clientes guardados")
    
    # Products
    productos_data = []
    categorias = ['Electronics', 'Clothing', 'Home', 'Sports', 'Books']
    for i in range(200):
        productos_data.append({
            'product_id': i + 1,
            'nombre': f'Product_{i+1}',
            'categoria': random.choice(categorias),
            'precio': round(np.random.uniform(5, 500), 2),
            'costo': round(np.random.uniform(2, 300), 2)
        })
    
    df_products = pd.DataFrame(productos_data)
    df_products.to_csv(base_path / 'ecommerce/products.csv', index=False)
    print(f"   [OK] {len(df_products)} productos guardados")
    
    # Orders
    orders_data = []
    estados = ['Completed', 'Processing', 'Shipped', 'Cancelled']
    for i in range(5000):
        fecha_orden = random.choice(fechas)
        customer_id = np.random.randint(1, 1001)
        total = round(np.random.uniform(20, 1000), 2)
        
        orders_data.append({
            'order_id': i + 1,
            'customer_id': customer_id,
            'fecha_orden': fecha_orden.strftime('%Y-%m-%d'),
            'fecha_envio': (fecha_orden + timedelta(days=np.random.randint(1, 7))).strftime('%Y-%m-%d'),
            'estado': random.choice(estados),
            'region': random.choice(['Norte', 'Sur', 'Este', 'Oeste']),
            'total': total
        })
    
    df_orders = pd.DataFrame(orders_data)
    df_orders.to_csv(base_path / 'ecommerce/orders.csv', index=False)
    print(f"   [OK] {len(df_orders)} ordenes guardadas")
    
    # Order Items
    order_items_data = []
    for order in orders_data:
        num_items = np.random.randint(1, 5)
        for j in range(num_items):
            product_id = np.random.randint(1, 201)
            cantidad = np.random.randint(1, 5)
            precio_unitario = round(np.random.uniform(10, 200), 2)
            descuento = round(np.random.uniform(0, 0.2), 2)
            subtotal = round(cantidad * precio_unitario * (1 - descuento), 2)
            
            order_items_data.append({
                'item_id': len(order_items_data) + 1,
                'order_id': order['order_id'],
                'product_id': product_id,
                'cantidad': cantidad,
                'precio_unitario': precio_unitario,
                'descuento': descuento,
                'subtotal': subtotal
            })
    
    df_order_items = pd.DataFrame(order_items_data)
    df_order_items.to_csv(base_path / 'ecommerce/order_items.csv', index=False)
    print(f"   [OK] {len(df_order_items)} items guardados")
    
    # 2. Online Retail (UCI style)
    print("\n[2] Generando Online Retail Dataset...")
    online_retail_data = []
    paises = ['United Kingdom', 'France', 'Germany', 'Spain', 'Italy']
    
    for i in range(10000):
        fecha = random.choice(fechas)
        online_retail_data.append({
            'InvoiceNo': f'INV-{np.random.randint(1000, 9999)}',
            'StockCode': f'STK-{np.random.randint(100, 999)}',
            'Description': f'Product Description {np.random.randint(1, 100)}',
            'Quantity': np.random.randint(1, 20),
            'InvoiceDate': fecha.strftime('%Y-%m-%d %H:%M:%S'),
            'UnitPrice': round(np.random.uniform(1, 50), 2),
            'CustomerID': np.random.randint(1000, 5000) if np.random.random() > 0.1 else None,
            'Country': random.choice(paises)
        })
    
    df_online_retail = pd.DataFrame(online_retail_data)
    df_online_retail.to_csv(base_path / 'online_retail/online_retail.csv', index=False)
    print(f"   [OK] {len(df_online_retail)} registros guardados")
    
    # 3. Marketing Analytics
    print("\n[3] Generando Marketing Analytics Dataset...")
    canales = ['Google Ads', 'Facebook', 'Instagram', 'Email', 'Organic', 'Direct']
    marketing_data = []
    
    for i in range(2000):
        fecha = random.choice(fechas)
        canal = random.choice(canales)
        impresiones = np.random.randint(1000, 100000)
        clicks = int(impresiones * np.random.uniform(0.01, 0.05))
        conversiones = int(clicks * np.random.uniform(0.02, 0.10))
        costo = round(impresiones * np.random.uniform(0.001, 0.01), 2)
        revenue = round(conversiones * np.random.uniform(10, 100), 2)
        
        marketing_data.append({
            'campaign_id': i + 1,
            'fecha': fecha.strftime('%Y-%m-%d'),
            'canal': canal,
            'impresiones': impresiones,
            'clicks': clicks,
            'conversiones': conversiones,
            'costo': costo,
            'revenue': revenue,
            'roi': round((revenue - costo) / costo * 100, 2) if costo > 0 else 0
        })
    
    df_marketing = pd.DataFrame(marketing_data)
    df_marketing.to_csv(base_path / 'marketing/marketing_analytics.csv', index=False)
    print(f"   [OK] {len(df_marketing)} registros guardados")
    
    print("\n" + "=" * 70)
    print("[EXITO] Datos intermedios generados correctamente")
    print("=" * 70)


def generar_datos_avanzado():
    """Genera datos sintéticos para nivel avanzado (más grandes)"""
    print("\n" + "=" * 70)
    print("Generando datos sinteticos - NIVEL AVANZADO")
    print("=" * 70)
    print("[INFO] Esto puede tardar unos minutos...")
    
    base_path = Path("Portfolio/03_Avanzado/data")
    base_path.mkdir(parents=True, exist_ok=True)
    (base_path / 'brazilian_ecommerce').mkdir(parents=True, exist_ok=True)
    (base_path / 'store_sales').mkdir(parents=True, exist_ok=True)
    (base_path / 'banking').mkdir(parents=True, exist_ok=True)
    
    np.random.seed(42)
    random.seed(42)
    
    # Brazilian E-commerce style (simplificado pero grande)
    print("\n[1] Generando Brazilian E-commerce Dataset...")
    
    # Customers
    customers_data = []
    estados_br = ['SP', 'RJ', 'MG', 'RS', 'PR', 'SC', 'BA', 'GO']
    for i in range(5000):
        customers_data.append({
            'customer_id': f'CUST-{i+1:06d}',
            'customer_unique_id': f'UNIQ-{i+1:06d}',
            'customer_zip_code_prefix': np.random.randint(1000, 99999),
            'customer_city': f'City_{np.random.randint(1, 100)}',
            'customer_state': random.choice(estados_br)
        })
    
    df_customers = pd.DataFrame(customers_data)
    df_customers.to_csv(base_path / 'brazilian_ecommerce/customers.csv', index=False)
    print(f"   [OK] {len(df_customers)} clientes guardados")
    
    # Orders
    fechas = pd.date_range(start='2020-01-01', end='2024-12-31', freq='D')
    orders_data = []
    estados_orden = ['delivered', 'shipped', 'processing', 'cancelled']
    
    for i in range(10000):
        fecha_orden = random.choice(fechas)
        customer_id = f'CUST-{np.random.randint(1, 5001):06d}'
        
        orders_data.append({
            'order_id': f'ORD-{i+1:06d}',
            'customer_id': customer_id,
            'order_status': random.choice(estados_orden),
            'order_purchase_timestamp': fecha_orden.strftime('%Y-%m-%d %H:%M:%S'),
            'order_approved_at': (fecha_orden + timedelta(hours=2)).strftime('%Y-%m-%d %H:%M:%S'),
            'order_delivered_carrier_date': (fecha_orden + timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S'),
            'order_delivered_customer_date': (fecha_orden + timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S'),
            'order_estimated_delivery_date': (fecha_orden + timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S')
        })
    
    df_orders = pd.DataFrame(orders_data)
    df_orders.to_csv(base_path / 'brazilian_ecommerce/orders.csv', index=False)
    print(f"   [OK] {len(df_orders)} ordenes guardadas")
    
    # Order Items
    order_items_data = []
    for order in orders_data[:5000]:  # Limitar para no hacer muy grande
        num_items = np.random.randint(1, 4)
        for j in range(num_items):
            order_items_data.append({
                'order_id': order['order_id'],
                'order_item_id': j + 1,
                'product_id': f'PROD-{np.random.randint(1, 1000):06d}',
                'seller_id': f'SELL-{np.random.randint(1, 500):06d}',
                'shipping_limit_date': (pd.to_datetime(order['order_purchase_timestamp']) + timedelta(days=10)).strftime('%Y-%m-%d %H:%M:%S'),
                'price': round(np.random.uniform(10, 500), 2),
                'freight_value': round(np.random.uniform(5, 50), 2)
            })
    
    df_order_items = pd.DataFrame(order_items_data)
    df_order_items.to_csv(base_path / 'brazilian_ecommerce/order_items.csv', index=False)
    print(f"   [OK] {len(df_order_items)} items guardados")
    
    # Store Sales Time Series
    print("\n[2] Generando Store Sales Time Series...")
    stores_data = []
    for i in range(50):
        stores_data.append({
            'store_nbr': i + 1,
            'city': f'City_{i+1}',
            'state': random.choice(['State_A', 'State_B', 'State_C']),
            'type': random.choice(['A', 'B', 'C']),
            'cluster': np.random.randint(1, 20)
        })
    
    df_stores = pd.DataFrame(stores_data)
    df_stores.to_csv(base_path / 'store_sales/stores.csv', index=False)
    print(f"   [OK] {len(df_stores)} tiendas guardadas")
    
    # Sales data
    sales_data = []
    fechas_sales = pd.date_range(start='2023-01-01', end='2024-12-31', freq='D')
    productos = [f'PROD-{i}' for i in range(1, 101)]
    
    for fecha in fechas_sales[:365]:  # Un año de datos
        for store in range(1, 51):
            for producto in productos[:10]:  # 10 productos por tienda
                if np.random.random() > 0.3:  # 70% probabilidad de venta
                    sales_data.append({
                        'date': fecha.strftime('%Y-%m-%d'),
                        'store_nbr': store,
                        'item_nbr': producto,
                        'unit_sales': np.random.randint(1, 50),
                        'onpromotion': random.choice([True, False])
                    })
    
    df_sales = pd.DataFrame(sales_data)
    df_sales.to_csv(base_path / 'store_sales/train.csv', index=False)
    print(f"   [OK] {len(df_sales)} registros de ventas guardados")
    
    # Banking Dataset
    print("\n[3] Generando Banking Dataset...")
    banking_data = []
    for i in range(5000):
        banking_data.append({
            'customer_id': i + 1,
            'age': np.random.randint(18, 80),
            'job': random.choice(['admin', 'technician', 'services', 'management', 'retired']),
            'marital': random.choice(['married', 'single', 'divorced']),
            'education': random.choice(['primary', 'secondary', 'tertiary']),
            'default': random.choice(['yes', 'no']),
            'balance': np.random.randint(-2000, 50000),
            'housing': random.choice(['yes', 'no']),
            'loan': random.choice(['yes', 'no']),
            'contact': random.choice(['cellular', 'telephone', 'unknown']),
            'day': np.random.randint(1, 32),
            'month': random.choice(['jan', 'feb', 'mar', 'apr', 'may', 'jun']),
            'duration': np.random.randint(0, 3000),
            'campaign': np.random.randint(1, 50),
            'pdays': np.random.randint(-1, 1000),
            'previous': np.random.randint(0, 10),
            'poutcome': random.choice(['success', 'failure', 'other', 'unknown']),
            'y': random.choice(['yes', 'no'])
        })
    
    df_banking = pd.DataFrame(banking_data)
    df_banking.to_csv(base_path / 'banking/banking_data.csv', index=False)
    print(f"   [OK] {len(df_banking)} registros guardados")
    
    print("\n" + "=" * 70)
    print("[EXITO] Datos avanzados generados correctamente")
    print("=" * 70)


def main():
    """Función principal"""
    print("=" * 70)
    print("GENERADOR DE DATOS SINTETICOS - PORTFOLIO DATA ANALYST")
    print("=" * 70)
    print("\nEste script genera datos sinteticos realistas para demostrar")
    print("el stack completo mientras se configuran credenciales de Kaggle.")
    print("\nNiveles a generar:")
    print("  - Basico: 3 datasets (~10K registros)")
    print("  - Intermedio: 3 datasets (~20K registros)")
    print("  - Avanzado: 3 datasets (~50K registros)")
    
    # Generar automáticamente sin confirmación
    print("\nGenerando datos automaticamente...")
    
    try:
        generar_datos_basico()
        generar_datos_intermedio()
        generar_datos_avanzado()
        
        print("\n" + "=" * 70)
        print("[EXITO] TODOS LOS DATOS GENERADOS CORRECTAMENTE")
        print("=" * 70)
        print("\nLos datos estan listos para usar en:")
        print("  - PostgreSQL")
        print("  - Python (pandas)")
        print("  - Jupyter Notebooks")
        print("  - Excel")
        print("\nPuedes empezar a trabajar inmediatamente!")
        
    except Exception as e:
        print(f"\n[ERROR] Error al generar datos: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

