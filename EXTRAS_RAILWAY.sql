-- ✅ EJECUTAR DESPUÉS de EJECUTAR_EN_RAILWAY.sql
-- Características avanzadas: Vista y Procedimiento Almacenado

-- 1. Vista útil para inventario con indicadores de stock
CREATE OR REPLACE VIEW vista_inventario AS
SELECT 
    c.id,
    c.nombre,
    c.precio,
    c.stock,
    cat.nombre as categoria,
    c.fabricante,
    c.codigo_producto,
    CASE 
        WHEN c.stock <= 10 THEN 'Bajo'
        WHEN c.stock <= 50 THEN 'Medio'
        ELSE 'Alto'
    END as nivel_stock
FROM componentes c
LEFT JOIN categorias cat ON c.categoria_id = cat.id;

-- 2. Procedimiento almacenado para búsqueda avanzada
DELIMITER //
CREATE PROCEDURE BuscarComponentes(IN termino_busqueda VARCHAR(255))
BEGIN
    SELECT 
        c.*,
        cat.nombre as categoria_nombre
    FROM componentes c
    LEFT JOIN categorias cat ON c.categoria_id = cat.id
    WHERE 
        c.nombre LIKE CONCAT('%', termino_busqueda, '%') OR
        c.descripcion LIKE CONCAT('%', termino_busqueda, '%') OR
        c.fabricante LIKE CONCAT('%', termino_busqueda, '%') OR
        cat.nombre LIKE CONCAT('%', termino_busqueda, '%')
    ORDER BY c.nombre;
END //
DELIMITER ;

-- 3. Verificar que se crearon correctamente
SELECT COUNT(*) as total_componentes FROM vista_inventario;

-- 4. Probar el procedimiento almacenado
CALL BuscarComponentes('Arduino');