-- ============================================
-- PROYECTO INTERMEDIO: Performance de Vendedores
-- Portfolio Data Analyst - Nivel Intermedio
-- ============================================

-- Objetivo: Demostrar consultas SQL complejas con JOINs múltiples y Window Functions

-- ============================================
-- 1. ANÁLISIS CON JOINs MÚLTIPLES
-- ============================================

-- Performance completo de vendedores con información de ventas y productos
WITH ventas_completas AS (
    SELECT 
        v.fecha,
        v.vendedor_id,
        vd.nombre AS vendedor,
        vd.region,
        vd.salario,
        p.nombre AS producto,
        p.categoria,
        v.cantidad,
        v.total,
        c.nombre AS cliente,
        c.ciudad AS ciudad_cliente
    FROM ventas v
    JOIN vendedores vd ON v.vendedor_id = vd.id
    JOIN productos p ON v.producto_id = p.id
    JOIN clientes c ON v.cliente_id = c.id
)
SELECT * FROM ventas_completas
LIMIT 20;

-- ============================================
-- 2. WINDOW FUNCTIONS - RANKING
-- ============================================

-- Ranking de vendedores por ventas totales
SELECT 
    vd.nombre AS vendedor,
    vd.region,
    SUM(v.total) AS total_ventas,
    COUNT(*) AS num_ventas,
    AVG(v.total) AS promedio_venta,
    RANK() OVER (ORDER BY SUM(v.total) DESC) AS ranking_global,
    RANK() OVER (PARTITION BY vd.region ORDER BY SUM(v.total) DESC) AS ranking_region
FROM ventas v
JOIN vendedores vd ON v.vendedor_id = vd.id
GROUP BY vd.id, vd.nombre, vd.region
ORDER BY total_ventas DESC;

-- ============================================
-- 3. WINDOW FUNCTIONS - ANÁLISIS TEMPORAL
-- ============================================

-- Ventas con comparación mes a mes
WITH ventas_mensuales AS (
    SELECT 
        v.vendedor_id,
        vd.nombre AS vendedor,
        DATE_TRUNC('month', v.fecha) AS mes,
        SUM(v.total) AS ventas_mes
    FROM ventas v
    JOIN vendedores vd ON v.vendedor_id = vd.id
    GROUP BY v.vendedor_id, vd.nombre, mes
)
SELECT 
    vendedor,
    mes,
    ventas_mes,
    LAG(ventas_mes) OVER (PARTITION BY vendedor_id ORDER BY mes) AS mes_anterior,
    ventas_mes - LAG(ventas_mes) OVER (PARTITION BY vendedor_id ORDER BY mes) AS diferencia,
    ROUND(
        ((ventas_mes - LAG(ventas_mes) OVER (PARTITION BY vendedor_id ORDER BY mes)) / 
         LAG(ventas_mes) OVER (PARTITION BY vendedor_id ORDER BY mes)) * 100, 
        2
    ) AS porcentaje_cambio
FROM ventas_mensuales
ORDER BY vendedor, mes;

-- ============================================
-- 4. CTEs COMPLEJOS - ANÁLISIS MULTIDIMENSIONAL
-- ============================================

-- Análisis completo de performance
WITH metrics_vendedores AS (
    SELECT 
        v.vendedor_id,
        COUNT(DISTINCT v.cliente_id) AS clientes_unicos,
        COUNT(*) AS total_ventas,
        SUM(v.total) AS ingresos_totales,
        AVG(v.total) AS ticket_promedio,
        SUM(v.cantidad) AS unidades_vendidas
    FROM ventas v
    GROUP BY v.vendedor_id
),
comparacion AS (
    SELECT 
        vd.nombre AS vendedor,
        vd.region,
        vd.salario,
        mv.clientes_unicos,
        mv.total_ventas,
        mv.ingresos_totales,
        mv.ticket_promedio,
        mv.unidades_vendidas,
        mv.ingresos_totales / vd.salario AS roi_salario
    FROM vendedores vd
    JOIN metrics_vendedores mv ON vd.id = mv.vendedor_id
)
SELECT 
    *,
    RANK() OVER (ORDER BY ingresos_totales DESC) AS rank_ingresos,
    RANK() OVER (ORDER BY roi_salario DESC) AS rank_roi,
    RANK() OVER (PARTITION BY region ORDER BY ingresos_totales DESC) AS rank_region
FROM comparacion
ORDER BY ingresos_totales DESC;

-- ============================================
-- 5. ANÁLISIS COMPARATIVO AVANZADO
-- ============================================

-- Comparación de vendedores con percentiles
WITH ventas_por_vendedor AS (
    SELECT 
        v.vendedor_id,
        vd.nombre AS vendedor,
        SUM(v.total) AS total_ventas
    FROM ventas v
    JOIN vendedores vd ON v.vendedor_id = vd.id
    GROUP BY v.vendedor_id, vd.nombre
)
SELECT 
    vendedor,
    total_ventas,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY total_ventas) OVER () AS mediana,
    CASE 
        WHEN total_ventas >= PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY total_ventas) OVER () 
        THEN 'Top 25%'
        WHEN total_ventas >= PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY total_ventas) OVER () 
        THEN 'Top 50%'
        ELSE 'Bottom 50%'
    END AS categoria_performance
FROM ventas_por_vendedor
ORDER BY total_ventas DESC;

-- ============================================
-- RESUMEN
-- ============================================
-- Este proyecto demuestra:
-- ✅ JOINs múltiples
-- ✅ Window Functions (RANK, LAG, PARTITION BY)
-- ✅ CTEs complejos
-- ✅ Análisis multidimensional
-- ✅ Comparaciones avanzadas

