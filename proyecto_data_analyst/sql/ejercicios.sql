-- ============================================
-- EJERCICIOS PRÁCTICOS - PostgreSQL
-- Data Analyst
-- ============================================

-- ============================================
-- EJERCICIO 1: Consultas Básicas
-- ============================================

-- 1.1. Seleccionar todos los productos
-- TODO: Escribe tu consulta aquí


-- 1.2. Seleccionar productos con precio mayor a 100
-- TODO: Escribe tu consulta aquí


-- 1.3. Contar el total de clientes
-- TODO: Escribe tu consulta aquí


-- ============================================
-- EJERCICIO 2: JOINs
-- ============================================

-- 2.1. Mostrar ventas con nombre de producto y cliente
-- TODO: Escribe tu consulta aquí


-- 2.2. Mostrar todas las ventas con información completa
-- (producto, cliente, vendedor)
-- TODO: Escribe tu consulta aquí


-- ============================================
-- EJERCICIO 3: Agregaciones
-- ============================================

-- 3.1. Total de ventas por región
-- TODO: Escribe tu consulta aquí


-- 3.2. Promedio de ventas por mes
-- TODO: Escribe tu consulta aquí


-- 3.3. Top 5 productos más vendidos
-- TODO: Escribe tu consulta aquí


-- ============================================
-- EJERCICIO 4: GROUP BY y HAVING
-- ============================================

-- 4.1. Regiones con ventas totales mayores a 1000
-- TODO: Escribe tu consulta aquí


-- 4.2. Categorías de productos con más de 2 productos
-- TODO: Escribe tu consulta aquí


-- ============================================
-- EJERCICIO 5: Window Functions
-- ============================================

-- 5.1. Ranking de ventas por región
-- TODO: Escribe tu consulta aquí


-- 5.2. Ventas acumuladas por mes
-- TODO: Escribe tu consulta aquí


-- ============================================
-- EJERCICIO 6: CTEs (Common Table Expressions)
-- ============================================

-- 6.1. Ventas mensuales usando CTE
-- TODO: Escribe tu consulta aquí


-- ============================================
-- SOLUCIONES (comentadas - descomenta para ver)
-- ============================================

/*
-- SOLUCIÓN 1.1
SELECT * FROM productos;

-- SOLUCIÓN 1.2
SELECT * FROM productos WHERE precio > 100;

-- SOLUCIÓN 1.3
SELECT COUNT(*) AS total_clientes FROM clientes;

-- SOLUCIÓN 2.1
SELECT 
    v.fecha,
    p.nombre AS producto,
    c.nombre AS cliente,
    v.total
FROM ventas v
JOIN productos p ON v.producto_id = p.id
JOIN clientes c ON v.cliente_id = c.id;

-- SOLUCIÓN 3.1
SELECT 
    region,
    SUM(total) AS total_ventas
FROM ventas
GROUP BY region
ORDER BY total_ventas DESC;

-- SOLUCIÓN 3.2
SELECT 
    DATE_TRUNC('month', fecha) AS mes,
    AVG(total) AS promedio_ventas
FROM ventas
GROUP BY mes
ORDER BY mes;

-- SOLUCIÓN 3.3
SELECT 
    p.nombre,
    SUM(v.cantidad) AS total_vendido
FROM ventas v
JOIN productos p ON v.producto_id = p.id
GROUP BY p.nombre
ORDER BY total_vendido DESC
LIMIT 5;

-- SOLUCIÓN 4.1
SELECT 
    region,
    SUM(total) AS total_ventas
FROM ventas
GROUP BY region
HAVING SUM(total) > 1000
ORDER BY total_ventas DESC;

-- SOLUCIÓN 5.1
SELECT 
    fecha,
    producto_id,
    total,
    region,
    RANK() OVER (PARTITION BY region ORDER BY total DESC) AS ranking
FROM ventas;

-- SOLUCIÓN 5.2
SELECT 
    fecha,
    total,
    SUM(total) OVER (ORDER BY fecha) AS ventas_acumuladas
FROM ventas
ORDER BY fecha;

-- SOLUCIÓN 6.1
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
    LAG(total_mes) OVER (ORDER BY mes) AS mes_anterior
FROM ventas_mensuales
ORDER BY mes;
*/

