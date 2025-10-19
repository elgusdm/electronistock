# 🚀 Guía de Deploy Gratuito - ElectroniStock

## 📋 Opciones Recomendadas (GRATIS)

### 🥇 **Opción 1: Railway** (Más Fácil - Recomendado)

#### ✅ Ventajas:
- MySQL incluido gratis
- Deploy automático desde GitHub
- Configuración muy sencilla
- $5 USD de crédito mensual gratis
- SSL automático

#### 📝 Pasos:

1. **Crear cuenta en Railway**
   - Ve a [railway.app](https://railway.app)
   - Registrate con GitHub

2. **Subir código a GitHub**
   ```bash
   # En tu carpeta del proyecto
   git init
   git add .
   git commit -m "Initial commit - ElectroniStock"
   
   # Crear repo en GitHub y subirlo
   git remote add origin https://github.com/tu-usuario/electronistock
   git push -u origin main
   ```

3. **Deploy en Railway**
   - Clic en "New Project"
   - Seleccionar "Deploy from GitHub repo"
   - Elegir tu repositorio ElectroniStock
   - Railway detecta Flask automáticamente

4. **Agregar Base de Datos MySQL**
   - En el dashboard, clic "Add Service"
   - Seleccionar "Database" → "MySQL"
   - Railway crea la BD automáticamente

5. **Configurar Variables de Entorno**
   ```
   DB_HOST=mysql_host_generado_por_railway
   DB_NAME=railway
   DB_USER=root
   DB_PASSWORD=password_generado_por_railway
   DB_PORT=3306
   SECRET_KEY=tu_clave_secreta_nueva
   FLASK_ENV=production
   ```

6. **Ejecutar Schema de BD**
   - Usar el cliente MySQL de Railway
   - Ejecutar el contenido de `database_schema.sql`

---

### 🥈 **Opción 2: Render + ElephantSQL**

#### ✅ Ventajas:
- Totalmente gratis
- PostgreSQL gratuito
- Muy confiable

#### 📝 Pasos:

1. **Modificar para PostgreSQL** (necesario pequeño cambio)
2. **Deploy en Render**: [render.com](https://render.com)
3. **BD en ElephantSQL**: [elephantsql.com](https://elephantsql.com)

---

### 🥉 **Opción 3: GitHub Codespaces (Para Demo)**

#### ✅ Ventajas:
- Completamente en la nube
- Perfecto para presentaciones
- No requiere instalación local

#### 📝 Pasos:

1. **Subir a GitHub**
2. **Abrir en Codespaces**
3. **Usar Port Forwarding**
   ```bash
   # En Codespaces terminal
   python src/app.py
   ```
4. **Compartir URL temporal**

---

## 🎯 **Recomendación: Railway**

Es la opción más sencilla para tu proyecto. Aquí está todo listo:

### 📁 Archivos Creados para Deploy:
- ✅ `Procfile` - Comando de inicio
- ✅ `Dockerfile` - Configuración de contenedor
- ✅ `railway.toml` - Configuración Railway
- ✅ `.env.production` - Variables de producción
- ✅ `.dockerignore` - Archivos a ignorar

### 🔧 Modificaciones Hechas:
- ✅ `app.py` adaptado para producción
- ✅ Puerto dinámico configurado
- ✅ Host 0.0.0.0 para acceso público

## 🚀 Pasos Rápidos Railway:

1. **GitHub**
   ```bash
   git init
   git add .
   git commit -m "Deploy ElectroniStock"
   # Subir a GitHub
   ```

2. **Railway**
   - Conectar GitHub repo
   - Agregar MySQL service
   - Configurar variables de entorno
   - Ejecutar schema SQL

3. **¡Listo!**
   - Tu app estará en: `https://tu-app.railway.app`
   - Acceso mundial 24/7

## 💰 Costos:

### Railway:
- **Gratis**: $5 USD crédito mensual
- **Uso típico**: $0-2 USD/mes para este proyecto
- **BD MySQL**: Incluida en el plan gratuito

### Render:
- **Web Service**: 100% gratis (con limitaciones)
- **BD**: ElephantSQL gratis hasta 20MB

### GitHub Codespaces:
- **Gratis**: 120 horas/mes para estudiantes
- **Demo**: Perfecto para presentaciones

## 🎓 Para tu Proyecto Universitario:

**Railway es perfecto porque:**
- ✅ Fácil de configurar
- ✅ URL profesional para presentar
- ✅ Funciona 24/7
- ✅ MySQL incluido
- ✅ Gratis para proyectos estudiantiles

¿Quieres que te ayude con alguna opción específica?