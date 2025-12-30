-- ============================================
-- PROYECTO BÁSICO: Análisis de Ventas
-- Portfolio Data Analyst - Nivel Básico
-- ============================================

-- Objetivo: Demostrar consultas SQL básicas para análisis de ventas

-- ============================================
-- 1. CONSULTAS BÁSICAS
-- ============================================

-- Ver todas las ventas
SELECT * FROM ventas
ORDER BY fecha DESC
LIMIT 10;

-- Ventas de un período específico
SELECT 
    fecha,
    producto_id,
    total
FROM ventas
WHERE fecha >= '2024-11-01' AND fecha <= '2024-12-31'
ORDER BY fecha;

-- Total de ventas
SELECT 
    COUNT(*) AS total_ventas,
    SUM(total) AS total_dinero,
    AVG(total) AS promedio_venta
FROM ventas;

-- ============================================
-- 2. AGRUPACIONES BÁSICAS
-- ============================================

-- Ventas por región
SELECT 
    region,
    COUNT(*) AS num_ventas,
    SUM(total) AS total_ventas
FROM ventas
GROUP BY region
ORDER BY total_ventas DESC;

-- Ventas por mes
SELECT 
    DATE_TRUNC('month', fecha) AS mes,
    COUNT(*) AS num_ventas,
    SUM(total) AS total_mes
FROM ventas
GROUP BY mes
ORDER BY mes;

-- Top 5 productos más vendidos
SELECT 
    producto_id,
    SUM(cantidad) AS total_vendido,
    SUM(total) AS ingresos
FROM ventas
GROUP BY producto_id
ORDER BY total_vendido DESC
LIMIT 5;

-- ============================================
-- 3. JOINs BÁSICOS
-- ============================================

-- Ventas con información de productos
SELECT 
    v.fecha,
    p.nombre AS producto,
    v.cantidad,
    v.total
FROM ventas v
JOIN productos p ON v.producto_id = p.id
ORDER BY v.fecha DESC
LIMIT 10;

-- Ventas por categoría de producto
SELECT 
    p.categoria,
    COUNT(*) AS num_ventas,
    SUM(v.total) AS total_ventas
FROM ventas v
JOIN productos p ON v.producto_id = p.id
GROUP BY p.categoria
ORDER BY total_ventas DESC;

-- ============================================
-- 4. FILTROS Y CONDICIONES
-- ============================================

-- Ventas mayores a un monto
SELECT 
    fecha,
    producto_id,
    total
FROM ventas
WHERE total > 500
ORDER BY total DESC;

-- Ventas por cliente específico
SELECT 
    v.fecha,
    p.nombre AS producto,
    v.total
FROM ventas v
JOIN productos p ON v.producto_id = p.id
WHERE v.cliente_id = 1
ORDER BY v.fecha DESC;

-- ============================================
-- 5. EXPORTAR RESULTADOS
-- ============================================

-- Exportar ventas por región a CSV
-- \copy (SELECT region, COUNT(*) as ventas, SUM(total) as total FROM ventas GROUP BY region) TO 'ventas_por_region.csv' CSV HEADER;

-- ============================================
-- RESUMEN
-- ============================================
-- Este proyecto demuestra:
-- ✅ SELECT básico
-- ✅ WHERE con condiciones
-- ✅ GROUP BY y agregaciones
-- ✅ JOINs simples
-- ✅ ORDER BY para ordenar resultados
-- ✅ LIMIT para limitar resultados

