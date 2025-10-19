# ElectroniStock - Sistema de Gestión de Componentes Electrónicos

Sistema web desarrollado con Flask y MySQL para la gestión integral de inventario de componentes electrónicos.

## 🚀 Características Principales

- **Gestión de Componentes**: CRUD completo para componentes electrónicos
- **Categorización**: Organización por categorías personalizables
- **Búsqueda Avanzada**: Búsqueda por nombre, fabricante, descripción
- **Control de Stock**: Indicadores visuales de niveles de inventario
- **Interfaz Responsiva**: Diseño moderno compatible con dispositivos móviles
- **Base de Datos Relacional**: Esquema optimizado para componentes electrónicos


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


## 📝 Notas de Desarrollo

- La aplicación usa Bootstrap 5 para el diseño
- Font Awesome para los iconos
- MySQL Connector para la base de datos
- Jinja2 para los templates


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

elgusdm
Desarrollado para el curso de Base de Datos - 5to Semestre UNAM

## 📄 Licencia

Este proyecto es para uso educativo.
