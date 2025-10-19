-- ✅ EJECUTAR TODO ESTE CÓDIGO EN EL MYSQL CLIENT DE RAILWAY

-- 1. Crear tablas
CREATE TABLE categorias (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE componentes (
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
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE SET NULL
);

CREATE TABLE proveedores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    contacto VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(100),
    direccion TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Insertar categorías
INSERT INTO categorias (nombre, descripcion) VALUES
('Resistencias', 'Componentes pasivos que limitan el flujo de corriente'),
('Capacitores', 'Componentes que almacenan energía eléctrica'),
('Semiconductores', 'Diodos, transistores, circuitos integrados'),
('Conectores', 'Elementos para conexiones eléctricas'),
('Inductores', 'Componentes que almacenan energía magnética'),
('Sensores', 'Dispositivos que detectan estímulos del ambiente'),
('Microcontroladores', 'Circuitos con procesador y memoria'),
('Displays', 'Pantallas y elementos de visualización'),
('Fuentes de Poder', 'Dispositivos de suministro de energía'),
('Herramientas', 'Equipos y herramientas para electrónica');

-- 3. Insertar componentes
INSERT INTO componentes (nombre, descripcion, precio, stock, categoria_id, fabricante, codigo_producto) VALUES
('Resistencia 1KΩ', 'Resistencia 1000 ohms 1/4W', 0.50, 500, 1, 'Vishay', 'R1K'),
('Capacitor 470μF', 'Capacitor electrolítico 470μF 25V', 2.30, 150, 2, 'Panasonic', 'C470'),
('Arduino Uno R3', 'Microcontrolador ATmega328P', 25.99, 25, 7, 'Arduino', 'UNO'),
('LED Rojo 5mm', 'LED rojo alta luminosidad', 0.75, 200, 3, 'Kingbright', 'LED5R'),
('Transistor 2N2222', 'Transistor NPN uso general', 1.25, 100, 3, 'ON Semi', '2N2222'),
('Sensor DS18B20', 'Sensor temperatura digital', 8.50, 30, 6, 'Maxim', 'DS18B20'),
('LCD 16x2', 'Display LCD con backlight', 12.99, 15, 8, 'Hitachi', 'LCD16x2'),
('Potenciómetro 10K', 'Potenciómetro rotatorio 10KΩ', 3.50, 50, 1, 'Bourns', 'POT10K'),
('Protoboard 830', 'Protoboard 830 puntos', 8.99, 20, 4, 'Busboard', 'BB830'),
('Fuente 5V 2A', 'Fuente regulada 5V 2A', 15.99, 10, 9, 'Mean Well', 'PSU5V2A');

-- 4. Insertar proveedores
INSERT INTO proveedores (nombre, contacto, telefono, email, direccion) VALUES
('Steren Electrónica', 'Juan Pérez', '55-1234-5678', 'ventas@steren.com.mx', 'CDMX'),
('Electrónica Saber', 'María García', '55-8765-4321', 'info@electronicasaber.com', 'Guadalajara'),
('AGE Electrónica', 'Carlos López', '55-5555-1234', 'pedidos@age.com.mx', 'Monterrey');