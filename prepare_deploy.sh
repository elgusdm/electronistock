#!/bin/bash

# Script para preparar el proyecto para deploy
echo "🚀 Preparando ElectroniStock para deploy..."

# Verificar si git está inicializado
if [ ! -d ".git" ]; then
    echo "📁 Inicializando repositorio Git..."
    git init
    
    # Crear .gitignore si no existe
    if [ ! -f ".gitignore" ]; then
        echo "📝 Creando .gitignore..."
        cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
.venv/
venv/
ENV/
env/

# Environment variables
.env

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Database
*.db
*.sqlite3
EOF
    fi
    
    echo "✅ Git inicializado"
else
    echo "✅ Git ya está configurado"
fi

# Agregar archivos al staging
echo "📦 Agregando archivos..."
git add .

# Verificar status
echo "📊 Estado del repositorio:"
git status

echo ""
echo "🎯 Siguiente paso:"
echo "1. Haz commit: git commit -m 'Deploy ElectroniStock'"
echo "2. Crea repo en GitHub"
echo "3. Conecta: git remote add origin https://github.com/tu-usuario/electronistock"
echo "4. Sube: git push -u origin main"
echo ""
echo "💡 Luego ve a railway.app y conecta tu repositorio"