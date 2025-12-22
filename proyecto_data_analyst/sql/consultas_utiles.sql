-- ============================================
-- CONSULTAS ÚTILES PARA DATA ANALYST
-- PostgreSQL
-- ============================================

-- ============================================
-- 1. EXPLORACIÓN DE DATOS
-- ============================================

-- Ver estructura de una tabla
\d nombre_tabla

-- Ver todas las tablas
\dt

-- Ver esquemas
\dn

-- Contar registros en todas las tablas
SELECT 
    schemaname,
    tablename,
    n_live_tup AS registros
FROM pg_stat_user_tables
ORDER BY n_live_tup DESC;

-- ============================================
-- 2. ESTADÍSTICAS DESCRIPTIVAS
-- ============================================

-- Estadísticas básicas de una columna numérica
SELECT 
    COUNT(*) AS total_registros,
    MIN(total) AS minimo,
    MAX(total) AS maximo,
    AVG(total) AS promedio,
    STDDEV(total) AS desviacion_estandar,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY total) AS mediana
FROM ventas;

-- ============================================
-- 3. ANÁLISIS TEMPORAL
-- ============================================

-- Ventas por día
SELECT 
    DATE(fecha) AS dia,
    COUNT(*) AS num_ventas,
    SUM(total) AS total_dia
FROM ventas
GROUP BY dia
ORDER BY dia DESC;

-- Ventas por mes
SELECT 
    DATE_TRUNC('month', fecha) AS mes,
    COUNT(*) AS num_ventas,
    SUM(total) AS total_mes,
    AVG(total) AS promedio_venta
FROM ventas
GROUP BY mes
ORDER BY mes DESC;

-- Comparación mes a mes
WITH ventas_mensuales AS (
    SELECT 
        DATE_TRUNC('month', fecha) AS mes,
        SUM(total) AS total_mes
    FROM ventas
    GROUP BY mes
)
SELECT 
    mes,
    total_mes,
    LAG(total_mes) OVER (ORDER BY mes) AS mes_anterior,
    total_mes - LAG(total_mes) OVER (ORDER BY mes) AS diferencia,
    ROUND(
        ((total_mes - LAG(total_mes) OVER (ORDER BY mes)) / 
         LAG(total_mes) OVER (ORDER BY mes)) * 100, 
        2
    ) AS porcentaje_cambio
FROM ventas_mensuales
ORDER BY mes DESC;

-- ============================================
-- 4. ANÁLISIS POR CATEGORÍAS
-- ============================================

-- Ventas por categoría de producto
SELECT 
    p.categoria,
    COUNT(*) AS num_ventas,
    SUM(v.total) AS total_ventas,
    AVG(v.total) AS promedio_venta,
    SUM(v.cantidad) AS unidades_vendidas
FROM ventas v
JOIN productos p ON v.producto_id = p.id
GROUP BY p.categoria
ORDER BY total_ventas DESC;

-- Top productos por categoría
SELECT 
    categoria,
    nombre,
    total_vendido
FROM (
    SELECT 
        p.categoria,
        p.nombre,
        SUM(v.total) AS total_vendido,
        ROW_NUMBER() OVER (PARTITION BY p.categoria ORDER BY SUM(v.total) DESC) AS rn
    FROM ventas v
    JOIN productos p ON v.producto_id = p.id
    GROUP BY p.categoria, p.nombre
) ranked
WHERE rn <= 3
ORDER BY categoria, total_vendido DESC;

-- ============================================
-- 5. ANÁLISIS GEOGRÁFICO
-- ============================================

-- Ventas por región
SELECT 
    region,
    COUNT(*) AS num_ventas,
    SUM(total) AS total_ventas,
    AVG(total) AS ticket_promedio,
    COUNT(DISTINCT cliente_id) AS clientes_unicos
FROM ventas
GROUP BY region
ORDER BY total_ventas DESC;

-- ============================================
-- 6. ANÁLISIS DE CLIENTES
-- ============================================

-- Top clientes por valor
SELECT 
    c.nombre,
    c.ciudad,
    COUNT(*) AS num_compras,
    SUM(v.total) AS total_gastado,
    AVG(v.total) AS promedio_compra
FROM ventas v
JOIN clientes c ON v.cliente_id = c.id
GROUP BY c.id, c.nombre, c.ciudad
ORDER BY total_gastado DESC
LIMIT 10;

-- Clientes por ciudad
SELECT 
    ciudad,
    COUNT(*) AS num_clientes,
    COUNT(DISTINCT v.id) AS num_ventas,
    SUM(v.total) AS total_ventas
FROM clientes c
LEFT JOIN ventas v ON c.id = v.cliente_id
GROUP BY ciudad
ORDER BY num_clientes DESC;

-- ============================================
-- 7. ANÁLISIS DE VENDEDORES
-- ============================================

-- Performance de vendedores
SELECT 
    vd.nombre,
    vd.region,
    COUNT(*) AS num_ventas,
    SUM(v.total) AS total_ventas,
    AVG(v.total) AS promedio_venta,
    vd.salario
FROM ventas v
JOIN vendedores vd ON v.vendedor_id = vd.id
GROUP BY vd.id, vd.nombre, vd.region, vd.salario
ORDER BY total_ventas DESC;

-- ============================================
-- 8. EXPORTAR DATOS
-- ============================================

-- Exportar a CSV (desde psql)
-- \copy (SELECT * FROM ventas) TO 'ventas.csv' CSV HEADER;

-- Exportar resultado de consulta
-- \copy (SELECT p.nombre, SUM(v.total) FROM ventas v JOIN productos p ON v.producto_id = p.id GROUP BY p.nombre) TO 'ventas_por_producto.csv' CSV HEADER;

-- ============================================
-- 9. CONSULTAS AVANZADAS
-- ============================================

-- Productos que nunca se han vendido
SELECT 
    p.id,
    p.nombre,
    p.precio
FROM productos p
LEFT JOIN ventas v ON p.id = v.producto_id
WHERE v.id IS NULL;

-- Ventas con información completa (múltiples JOINs)
SELECT 
    v.fecha,
    p.nombre AS producto,
    p.categoria,
    c.nombre AS cliente,
    c.ciudad,
    vd.nombre AS vendedor,
    v.cantidad,
    v.precio_unitario,
    v.total,
    v.region
FROM ventas v
JOIN productos p ON v.producto_id = p.id
JOIN clientes c ON v.cliente_id = c.id
JOIN vendedores vd ON v.vendedor_id = vd.id
ORDER BY v.fecha DESC;

-- ============================================
-- 10. FUNCIONES DE VENTANA ÚTILES
-- ============================================

-- Ranking de ventas
SELECT 
    fecha,
    producto_id,
    total,
    RANK() OVER (ORDER BY total DESC) AS ranking_total,
    RANK() OVER (PARTITION BY DATE_TRUNC('month', fecha) ORDER BY total DESC) AS ranking_mensual
FROM ventas;

-- Ventas acumuladas
SELECT 
    fecha,
    total,
    SUM(total) OVER (ORDER BY fecha) AS acumulado_total,
    SUM(total) OVER (PARTITION BY region ORDER BY fecha) AS acumulado_region
FROM ventas
ORDER BY fecha;

-- Comparación con promedio
SELECT 
    fecha,
    total,
    AVG(total) OVER () AS promedio_general,
    total - AVG(total) OVER () AS diferencia_promedio
FROM ventas;

