-- ============================================
-- SCHEMA COMPLETO - Nivel Básico
-- Portfolio Data Analyst
-- ============================================

-- Crear base de datos (ejecutar como superusuario)
-- CREATE DATABASE retail_analysis_basico;

-- Conectarse a la base de datos
-- \c retail_analysis_basico

-- ============================================
-- 1. TABLA DE PRODUCTOS
-- ============================================

CREATE TABLE IF NOT EXISTS productos (
    producto_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    precio DECIMAL(10, 2)
);

COMMENT ON TABLE productos IS 'Catálogo de productos disponibles';
COMMENT ON COLUMN productos.producto_id IS 'ID único del producto';
COMMENT ON COLUMN productos.nombre IS 'Nombre del producto';
COMMENT ON COLUMN productos.categoria IS 'Categoría del producto (Ropa, Hogar, Deportes, etc.)';
COMMENT ON COLUMN productos.precio IS 'Precio unitario del producto';

-- ============================================
-- 2. TABLA DE CLIENTES
-- ============================================

CREATE TABLE IF NOT EXISTS clientes (
    cliente_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(50),
    segmento VARCHAR(50)
);

COMMENT ON TABLE clientes IS 'Información de clientes';
COMMENT ON COLUMN clientes.cliente_id IS 'ID único del cliente';
COMMENT ON COLUMN clientes.nombre IS 'Nombre del cliente';
COMMENT ON COLUMN clientes.ciudad IS 'Ciudad del cliente';
COMMENT ON COLUMN clientes.segmento IS 'Segmento del cliente (Consumer, Corporate, Home Office)';

-- ============================================
-- 3. TABLA DE VENTAS
-- ============================================

CREATE TABLE IF NOT EXISTS ventas (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    producto VARCHAR(100),
    region VARCHAR(50),
    cantidad INTEGER,
    precio_unitario DECIMAL(10, 2),
    total DECIMAL(10, 2),
    vendedor VARCHAR(100),
    cliente_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

COMMENT ON TABLE ventas IS 'Registro de todas las ventas';
COMMENT ON COLUMN ventas.id IS 'ID único de la venta';
COMMENT ON COLUMN ventas.fecha IS 'Fecha de la venta';
COMMENT ON COLUMN ventas.producto IS 'Nombre del producto vendido';
COMMENT ON COLUMN ventas.region IS 'Región donde se realizó la venta';
COMMENT ON COLUMN ventas.cantidad IS 'Cantidad de unidades vendidas';
COMMENT ON COLUMN ventas.precio_unitario IS 'Precio por unidad';
COMMENT ON COLUMN ventas.total IS 'Total de la venta (cantidad * precio_unitario)';
COMMENT ON COLUMN ventas.vendedor IS 'Nombre del vendedor';
COMMENT ON COLUMN ventas.cliente_id IS 'ID del cliente (FK a clientes)';

-- ============================================
-- 4. ÍNDICES PARA OPTIMIZACIÓN
-- ============================================

-- Índice en fecha (para consultas temporales)
CREATE INDEX IF NOT EXISTS idx_ventas_fecha ON ventas(fecha);

-- Índice en región (para agrupaciones)
CREATE INDEX IF NOT EXISTS idx_ventas_region ON ventas(region);

-- Índice en cliente_id (para JOINs)
CREATE INDEX IF NOT EXISTS idx_ventas_cliente ON ventas(cliente_id);

-- Índice en producto (para análisis por producto)
CREATE INDEX IF NOT EXISTS idx_ventas_producto ON ventas(producto);

-- ============================================
-- 5. VERIFICACIÓN
-- ============================================

-- Ver tablas creadas
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public'
ORDER BY table_name;

-- Ver índices creados
SELECT 
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename, indexname;

-- ============================================
-- RESUMEN
-- ============================================
-- Este schema crea:
-- ✅ 3 tablas principales (productos, clientes, ventas)
-- ✅ Relaciones entre tablas (Foreign Keys)
-- ✅ Índices para optimizar consultas
-- ✅ Comentarios en tablas y columnas
-- ✅ Estructura lista para análisis

