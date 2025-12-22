-- ============================================
-- Script para crear base de datos de práctica
-- Data Analyst - PostgreSQL
-- ============================================

-- Crear base de datos (ejecutar como superusuario)
-- CREATE DATABASE practica_data_analyst;
-- \c practica_data_analyst

-- ============================================
-- TABLA: Ventas
-- ============================================
CREATE TABLE IF NOT EXISTS ventas (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    producto_id INTEGER NOT NULL,
    cliente_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    region VARCHAR(50) NOT NULL,
    vendedor_id INTEGER NOT NULL
);

-- ============================================
-- TABLA: Productos
-- ============================================
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INTEGER NOT NULL,
    fecha_creacion DATE DEFAULT CURRENT_DATE
);

-- ============================================
-- TABLA: Clientes
-- ============================================
CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    ciudad VARCHAR(50) NOT NULL,
    pais VARCHAR(50) NOT NULL,
    fecha_registro DATE DEFAULT CURRENT_DATE
);

-- ============================================
-- TABLA: Vendedores
-- ============================================
CREATE TABLE IF NOT EXISTS vendedores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    region VARCHAR(50) NOT NULL,
    salario DECIMAL(10, 2) NOT NULL
);

-- ============================================
-- INSERTAR DATOS DE EJEMPLO
-- ============================================

-- Productos
INSERT INTO productos (nombre, categoria, precio, stock) VALUES
('Laptop Dell', 'Electrónicos', 899.99, 50),
('Mouse Logitech', 'Accesorios', 29.99, 200),
('Teclado Mecánico', 'Accesorios', 79.99, 150),
('Monitor Samsung', 'Electrónicos', 299.99, 75),
('Auriculares Sony', 'Audio', 149.99, 100),
('Tablet iPad', 'Electrónicos', 499.99, 30),
('Cámara Canon', 'Fotografía', 799.99, 25),
('Impresora HP', 'Oficina', 199.99, 40);

-- Clientes
INSERT INTO clientes (nombre, email, ciudad, pais) VALUES
('Juan Pérez', 'juan.perez@email.com', 'Madrid', 'España'),
('María García', 'maria.garcia@email.com', 'Barcelona', 'España'),
('Carlos López', 'carlos.lopez@email.com', 'Valencia', 'España'),
('Ana Martínez', 'ana.martinez@email.com', 'Sevilla', 'España'),
('Luis Rodríguez', 'luis.rodriguez@email.com', 'Bilbao', 'España'),
('Laura Sánchez', 'laura.sanchez@email.com', 'Madrid', 'España'),
('Pedro Fernández', 'pedro.fernandez@email.com', 'Barcelona', 'España'),
('Sofía Torres', 'sofia.torres@email.com', 'Valencia', 'España');

-- Vendedores
INSERT INTO vendedores (nombre, email, region, salario) VALUES
('Roberto Silva', 'roberto.silva@empresa.com', 'Norte', 3500.00),
('Carmen Ruiz', 'carmen.ruiz@empresa.com', 'Sur', 3600.00),
('Miguel Díaz', 'miguel.diaz@empresa.com', 'Este', 3400.00),
('Elena Moreno', 'elena.moreno@empresa.com', 'Oeste', 3700.00);

-- Ventas (datos de ejemplo para últimos 3 meses)
INSERT INTO ventas (fecha, producto_id, cliente_id, cantidad, precio_unitario, total, region, vendedor_id) VALUES
('2024-10-15', 1, 1, 2, 899.99, 1799.98, 'Norte', 1),
('2024-10-20', 2, 2, 5, 29.99, 149.95, 'Sur', 2),
('2024-10-25', 3, 3, 3, 79.99, 239.97, 'Este', 3),
('2024-11-01', 4, 4, 1, 299.99, 299.99, 'Oeste', 4),
('2024-11-05', 5, 5, 2, 149.99, 299.98, 'Norte', 1),
('2024-11-10', 6, 6, 1, 499.99, 499.99, 'Sur', 2),
('2024-11-15', 7, 7, 1, 799.99, 799.99, 'Este', 3),
('2024-11-20', 8, 8, 2, 199.99, 399.98, 'Oeste', 4),
('2024-12-01', 1, 2, 1, 899.99, 899.99, 'Norte', 1),
('2024-12-05', 2, 3, 10, 29.99, 299.90, 'Sur', 2),
('2024-12-10', 3, 4, 2, 79.99, 159.98, 'Este', 3),
('2024-12-15', 4, 5, 3, 299.99, 899.97, 'Oeste', 4),
('2024-12-20', 5, 6, 4, 149.99, 599.96, 'Norte', 1);

-- ============================================
-- CONSULTAS DE VERIFICACIÓN
-- ============================================

-- Ver todas las tablas
SELECT 'Tablas creadas exitosamente' AS mensaje;

-- Contar registros
SELECT 
    'Productos' AS tabla, COUNT(*) AS total FROM productos
UNION ALL
SELECT 
    'Clientes' AS tabla, COUNT(*) AS total FROM clientes
UNION ALL
SELECT 
    'Vendedores' AS tabla, COUNT(*) AS total FROM vendedores
UNION ALL
SELECT 
    'Ventas' AS tabla, COUNT(*) AS total FROM ventas;

-- Ver algunas ventas
SELECT 
    v.fecha,
    p.nombre AS producto,
    c.nombre AS cliente,
    v.cantidad,
    v.total,
    v.region
FROM ventas v
JOIN productos p ON v.producto_id = p.id
JOIN clientes c ON v.cliente_id = c.id
ORDER BY v.fecha DESC
LIMIT 10;

