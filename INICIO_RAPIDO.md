# 🚀 Guía de Inicio Rápido - ElectroniStock

## Pasos para Ejecutar la Aplicación

### 1. ⚙️ Configurar MySQL

1. Abre **MySQL Workbench**
2. Conecta a tu servidor MySQL local
3. Ejecuta el archivo `database_schema.sql` completo:
   - Crea la base de datos `componentes_electronicos`
   - Crea las tablas necesarias
   - Inserta datos de ejemplo

### 2. 🔧 Configurar Credenciales

Edita el archivo `.env` con tus credenciales:

```env
DB_HOST=localhost
DB_NAME=componentes_electronicos
DB_USER=root                 # Tu usuario MySQL
DB_PASSWORD=tu_contraseña    # Tu contraseña MySQL
DB_PORT=3306
SECRET_KEY=cambia_esta_clave_secreta
```

### 3. ▶️ Ejecutar la Aplicación

Opción 1 - Usando el script run.py:
```bash
"/Users/jmrr/Documents/Trabajos UNAM/5to semestre/BASE DE DATOS/DB-1/.venv/bin/python" run.py
```

Opción 2 - Directamente:
```bash
"/Users/jmrr/Documents/Trabajos UNAM/5to semestre/BASE DE DATOS/DB-1/.venv/bin/python" src/app.py
```

### 4. 🌐 Abrir la Aplicación

Abre tu navegador y ve a: `http://localhost:5000`

## 🎯 Funcionalidades a Probar

1. **Página Principal**: Navegación y resumen del sistema
2. **Componentes**: 
   - Ver lista de componentes
   - Agregar nuevo componente
   - Ver detalles de un componente
   - Editar información
   - Eliminar componente
3. **Categorías**:
   - Ver categorías existentes
   - Crear nueva categoría
4. **Búsqueda**:
   - Buscar por nombre, fabricante o descripción
   - Probar búsquedas como: "Arduino", "Resistencia", "LED"

## 🔍 Datos de Ejemplo Incluidos

El script de base de datos incluye:
- 10 categorías de componentes electrónicos
- 10+ componentes de ejemplo
- 3 proveedores de ejemplo
- Vista de inventario
- Procedimiento almacenado para búsquedas

## ⚠️ Solución de Problemas Comunes

### Error de Conexión MySQL:
```
Error al conectar a MySQL: Access denied for user...
```
**Solución**: Verifica usuario y contraseña en `.env`

### Error de Base de Datos:
```
Error: 1049 Unknown database 'componentes_electronicos'
```
**Solución**: Ejecuta el script `database_schema.sql` en MySQL Workbench

### Error de Dependencias:
```
ModuleNotFoundError: No module named 'flask'
```
**Solución**: Las dependencias ya están instaladas en el entorno virtual. Usa el comando completo con la ruta del Python del entorno virtual.

### Puerto en Uso:
```
Address already in use
```
**Solución**: Mata procesos en puerto 5000 o cambia el puerto en `app.py`

## 📱 Navegación de la App

```
Inicio (/)
├── Componentes (/componentes)
│   ├── Nuevo (/componentes/nuevo)
│   ├── Ver (/componentes/<id>)
│   └── Editar (/componentes/editar/<id>)
├── Categorías (/categorias)
│   └── Nueva (/categorias/nueva)
└── Búsqueda (/buscar)
```

## 🎨 Características Visuales

- **Responsive Design**: Funciona en móvil y desktop
- **Indicadores de Stock**:
  - 🔴 Rojo: Stock ≤ 10 (Bajo)
  - 🟡 Amarillo: Stock ≤ 50 (Medio)  
  - 🟢 Verde: Stock > 50 (Alto)
- **Interfaz Moderna**: Bootstrap 5 + Font Awesome
- **Animaciones Suaves**: Efectos CSS personalizados

¡Listo para usar! 🎉