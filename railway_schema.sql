-- Schema para Railway (sin CREATE DATABASE)
-- Ejecutar en el MySQL Client de Railway

-- Tabla de categorías
CREATE TABLE IF NOT EXISTS categorias (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de componentes
CREATE TABLE IF NOT EXISTS componentes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0,
    categoria_id INT,
    fabricante VARCHAR(100),
    codigo_producto VARCHAR(50),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE SET NULL,
    INDEX idx_nombre (nombre),
    INDEX idx_fabricante (fabricante),
    INDEX idx_categoria (categoria_id)
);

-- Tabla de proveedores
CREATE TABLE IF NOT EXISTS proveedores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    contacto VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(100),
    direccion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de relación componentes-proveedores
CREATE TABLE IF NOT EXISTS componente_proveedor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    componente_id INT NOT NULL,
    proveedor_id INT NOT NULL,
    precio_proveedor DECIMAL(10, 2),
    tiempo_entrega_dias INT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (componente_id) REFERENCES componentes(id) ON DELETE CASCADE,
    FOREIGN KEY (proveedor_id) REFERENCES proveedores(id) ON DELETE CASCADE,
    UNIQUE KEY unique_componente_proveedor (componente_id, proveedor_id)
);

-- Insertar categorías de ejemplo
INSERT IGNORE INTO categorias (nombre, descripcion) VALUES
('Resistencias', 'Componentes pasivos que limitan el flujo de corriente eléctrica'),
('Capacitores', 'Componentes que almacenan energía eléctrica en un campo eléctrico'),
('Semiconductores', 'Dispositivos electrónicos como diodos, transistores, circuitos integrados'),
('Conectores', 'Elementos para realizar conexiones eléctricas'),
('Inductores', 'Componentes que almacenan energía en un campo magnético'),
('Sensores', 'Dispositivos que detectan y responden a estímulos del ambiente'),
('Microcontroladores', 'Circuitos integrados que contienen procesador, memoria y periféricos'),
('Displays', 'Pantallas y elementos de visualización'),
('Fuentes de Poder', 'Dispositivos para suministro y regulación de energía'),
('Herramientas', 'Equipos y herramientas para electrónica');

-- Insertar componentes de ejemplo
INSERT IGNORE INTO componentes (nombre, descripcion, precio, stock, categoria_id, fabricante, codigo_producto) VALUES
('Resistencia 1KΩ 1/4W', 'Resistencia de película de carbón, 1000 ohms, 1/4 watt', 0.50, 500, 1, 'Vishay', 'CFR-25JB-52-1K0'),
('Capacitor Electrolítico 470μF 25V', 'Capacitor electrolítico radial, 470 microfaradios, 25 voltios', 2.30, 150, 2, 'Panasonic', 'ECA-1EM471'),
('Arduino Uno R3', 'Microcontrolador basado en ATmega328P', 25.99, 25, 7, 'Arduino', 'A000066'),
('LED Rojo 5mm', 'LED rojo de 5mm, alta luminosidad', 0.75, 200, 3, 'Kingbright', 'WP7113ID'),
('Transistor NPN 2N2222', 'Transistor bipolar NPN para uso general', 1.25, 100, 3, 'ON Semiconductor', '2N2222AG'),
('Sensor de Temperatura DS18B20', 'Sensor digital de temperatura programable', 8.50, 30, 6, 'Maxim Integrated', 'DS18B20+'),
('Display LCD 16x2', 'Pantalla LCD de caracteres 16x2 con backlight', 12.99, 15, 8, 'Hitachi', 'HD44780'),
('Potenciómetro 10KΩ', 'Potenciómetro rotatorio lineal de 10k ohms', 3.50, 50, 1, 'Bourns', '3386P-1-103LF'),
('Protoboard 830 puntos', 'Protoboard sin soldadura de 830 puntos de conexión', 8.99, 20, 4, 'Busboard', 'BB830'),
('Fuente 5V 2A', 'Fuente de alimentación regulada 5V 2A', 15.99, 10, 9, 'Mean Well', 'RS-15-5');

-- Insertar proveedores de ejemplo
INSERT IGNORE INTO proveedores (nombre, contacto, telefono, email, direccion) VALUES
('Steren Electrónica', 'Juan Pérez', '55-1234-5678', 'ventas@steren.com.mx', 'Ciudad de México'),
('Electrónica Saber', 'María García', '55-8765-4321', 'info@electronicasaber.com', 'Guadalajara, Jalisco'),
('AGE Electrónica', 'Carlos López', '55-5555-1234', 'pedidos@age.com.mx', 'Monterrey, NL');

-- Crear vista útil
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