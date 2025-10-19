# ElectroniStock - Sistema de Gestión de Componentes Electrónicos

Sistema web desarrollado con Flask y MySQL para la gestión integral de inventario de componentes electrónicos.

## 🚀 Características Principales

- **Gestión de Componentes**: CRUD completo para componentes electrónicos
- **Categorización**: Organización por categorías personalizables
- **Búsqueda Avanzada**: Búsqueda por nombre, fabricante, descripción
- **Control de Stock**: Indicadores visuales de niveles de inventario
- **Interfaz Responsiva**: Diseño moderno compatible con dispositivos móviles
- **Base de Datos Relacional**: Esquema optimizado para componentes electrónicos

## 📋 Requisitos del Sistema

- Python 3.8 o superior
- MySQL 5.7 o superior (o MySQL Workbench)
- Navegador web moderno

## 🛠️ Instalación

### 1. Configurar la Base de Datos

1. Abre MySQL Workbench
2. Ejecuta el script `database_schema.sql` para crear la base de datos y las tablas
3. El script incluye datos de ejemplo para probar la aplicación

### 2. Configurar el Entorno Python

```bash
# El entorno virtual ya está configurado en .venv
# Las dependencias ya están instaladas
```

### 3. Configurar Variables de Entorno

Edita el archivo `.env` con tus credenciales de MySQL:

```env
DB_HOST=localhost
DB_NAME=componentes_electronicos
DB_USER=tu_usuario_mysql
DB_PASSWORD=tu_contraseña_mysql
DB_PORT=3306
SECRET_KEY=cambia_esta_clave_secreta
```

### 4. Ejecutar la Aplicación

```bash
# Desde la carpeta raíz del proyecto
"/Users/jmrr/Documents/Trabajos UNAM/5to semestre/BASE DE DATOS/DB-1/.venv/bin/python" src/app.py
```

La aplicación estará disponible en: `http://localhost:5000`

## 📁 Estructura del Proyecto

```
DB-1/
├── src/
│   └── app.py              # Aplicación principal Flask
├── templates/
│   ├── base.html          # Template base
│   ├── index.html         # Página principal
│   ├── buscar.html        # Página de búsqueda
│   ├── componentes/       # Templates de componentes
│   │   ├── lista.html
│   │   ├── nuevo.html
│   │   ├── detalle.html
│   │   └── editar.html
│   └── categorias/        # Templates de categorías
│       ├── lista.html
│       └── nueva.html
├── static/
│   ├── css/
│   │   └── style.css      # Estilos personalizados
│   └── js/
│       └── script.js      # JavaScript personalizado
├── database_schema.sql    # Script de base de datos
├── requirements.txt       # Dependencias Python
├── .env                  # Variables de entorno
└── README.md            # Este archivo
```

## 🎯 Funcionalidades

### Componentes
- ✅ Listar todos los componentes
- ✅ Agregar nuevo componente
- ✅ Ver detalles del componente
- ✅ Editar componente existente
- ✅ Eliminar componente
- ✅ Búsqueda por múltiples criterios

### Categorías
- ✅ Gestión de categorías
- ✅ Asignación de componentes a categorías
- ✅ Visualización por categorías

### Sistema
- ✅ Interfaz responsive
- ✅ Indicadores de stock (bajo/medio/alto)
- ✅ Validaciones de formulario
- ✅ Mensajes de confirmación
- ✅ API REST básica

## 📊 Base de Datos

### Tablas Principales

1. **categorias**
   - `id`: Identificador único
   - `nombre`: Nombre de la categoría
   - `descripcion`: Descripción opcional
   - `fecha_creacion`: Timestamp de creación

2. **componentes**
   - `id`: Identificador único
   - `nombre`: Nombre del componente
   - `descripcion`: Descripción detallada
   - `precio`: Precio unitario
   - `stock`: Cantidad disponible
   - `categoria_id`: Referencia a categoría
   - `fabricante`: Empresa fabricante
   - `codigo_producto`: Código del fabricante
   - `fecha_creacion`: Timestamp de creación
   - `fecha_actualizacion`: Timestamp de última actualización

3. **proveedores** (tabla auxiliar)
   - Información de proveedores
   - Relación muchos a muchos con componentes

## 🔧 Personalización

### Agregar Nuevas Funcionalidades

1. **Nuevas rutas**: Agregar en `src/app.py`
2. **Nuevos templates**: Crear en `templates/`
3. **Estilos**: Modificar `static/css/style.css`
4. **JavaScript**: Extender `static/js/script.js`

### Modificar Base de Datos

1. Actualizar `database_schema.sql`
2. Modificar consultas en `src/app.py`
3. Actualizar templates según sea necesario

## 🚨 Solución de Problemas

### Error de Conexión a MySQL
- Verificar que MySQL esté ejecutándose
- Comprobar credenciales en `.env`
- Verificar que la base de datos exista

### Error de Dependencias
- Verificar que todas las dependencias estén instaladas
- Comprobar la versión de Python

### Errores de Templates
- Verificar rutas de archivos
- Comprobar sintaxis de Jinja2

## 📝 Notas de Desarrollo

- La aplicación usa Bootstrap 5 para el diseño
- Font Awesome para los iconos
- MySQL Connector para la base de datos
- Jinja2 para los templates

## 🔐 Seguridad

- Cambiar `SECRET_KEY` en producción
- Usar HTTPS en producción
- Validar todas las entradas de usuario
- Implementar autenticación si es necesario

## 📈 Próximas Mejoras

- [ ] Sistema de usuarios y autenticación
- [ ] Reportes y gráficos
- [ ] Exportación a Excel/PDF
- [ ] Código de barras para componentes
- [ ] Historial de movimientos de stock
- [ ] Alertas de stock bajo
- [ ] API REST completa
- [ ] Modo oscuro

## 👤 Autor

Desarrollado para el curso de Base de Datos - 5to Semestre UNAM

## 📄 Licencia

Este proyecto es para uso educativo.