#!/usr/bin/env python3
"""
Script para ejecutar ElectroniStock
Sistema de Gestión de Componentes Electrónicos
"""

import sys
import os
from pathlib import Path

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from src.app import app

    if __name__ == '__main__':
        print("🚀 Iniciando ElectroniStock...")
        print("📱 Aplicación disponible en: http://localhost:5000")
        print("⚡ Presiona Ctrl+C para detener el servidor")
        print("-" * 50)

        # Ejecutar la aplicación
        app.run(
            debug=True,
            host='127.0.0.1',
            port=5000,
            use_reloader=True
        )

except ImportError as e:
    print("❌ Error al importar la aplicación:")
    print(f"   {e}")
    print("\n💡 Soluciones:")
    print("   1. Verifica que estés en el directorio correcto")
    print("   2. Asegúrate de que el archivo src/app.py exista")
    print("   3. Instala las dependencias: pip install -r requirements.txt")

except Exception as e:
    print("❌ Error al iniciar la aplicación:")
    print(f"   {e}")
    print("\n💡 Verifica:")
    print("   1. La configuración de la base de datos en .env")
    print("   2. Que MySQL esté ejecutándose")
    print("   3. Que la base de datos 'componentes_electronicos' exista")
