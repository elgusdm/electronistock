-- Inserciones de ejemplo para relacionar componentes con proveedores
-- Ejecutar en MySQL (WorkBench o Railway) después de que existan las tablas y datos base

INSERT INTO componente_proveedor (componente_id, proveedor_id, precio_proveedor, tiempo_entrega_dias) VALUES
(1, 1, 0.45, 3),
(2, 2, 2.10, 5),
(3, 1, 23.50, 7),
(4, 3, 0.65, 2),
(5, 2, 1.10, 4),
(6, 3, 8.10, 10),
(7, 1, 11.99, 6),
(8, 2, 3.20, 4),
(9, 3, 8.50, 5),
(10,1,15.50,7);
