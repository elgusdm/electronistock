from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')
app.secret_key = os.getenv('SECRET_KEY', 'tu_clave_secreta_aqui')

# Configuración de la base de datos
db_config = {
    'host': os.getenv('MYSQLHOST', os.getenv('DB_HOST', 'localhost')),
    'database': os.getenv('MYSQLDATABASE', os.getenv('DB_NAME', 'componentes_electronicos')),
    'user': os.getenv('MYSQLUSER', os.getenv('DB_USER', 'root')),
    'password': os.getenv('MYSQLPASSWORD', os.getenv('DB_PASSWORD', 'gus03tavo')),
    'port': int(os.getenv('MYSQLPORT', os.getenv('DB_PORT', 3306)))
}


class DatabaseConnection:
    def __init__(self):
        self.connection = None
    
    def connect(self):
        try:
            print(f"Intentando conectar a: {db_config['host']}:{db_config['port']}")
            self.connection = mysql.connector.connect(**db_config)
            print("✅ Conexión exitosa a MySQL")
            return True
        except Error as e:
            print(f"❌ Error al conectar a MySQL: {e}")
            print(f"Configuración: {db_config}")
            return False
    
    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def execute_query(self, query, params=None):
        if not self.connection or not self.connection.is_connected():
            if not self.connect():
                return None

        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            if query.strip().upper().startswith('SELECT'):
                result = cursor.fetchall()
            else:
                self.connection.commit()
                result = cursor.rowcount
            cursor.close()
            return result
        except Error as e:
            print(f"Error ejecutando query: {e}")
            return None


# Instancia global de la conexión
db = DatabaseConnection()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/componentes')
def listar_componentes():
    query = """
    SELECT c.*, cat.nombre as categoria_nombre 
    FROM componentes c 
    LEFT JOIN categorias cat ON c.categoria_id = cat.id
    ORDER BY c.nombre
    """
    componentes = db.execute_query(query)
    return render_template('componentes/lista.html', componentes=componentes)


@app.route('/componentes/nuevo', methods=['GET', 'POST'])
def nuevo_componente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        categoria_id = request.form['categoria_id']
        fabricante = request.form['fabricante']

        query = """
        INSERT INTO componentes (nombre, descripcion, precio, stock, categoria_id, fabricante)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (nombre, descripcion, precio, stock, categoria_id, fabricante)

        if db.execute_query(query, params):
            flash('Componente agregado exitosamente', 'success')
            return redirect(url_for('listar_componentes'))
        else:
            flash('Error al agregar componente', 'error')

    # Obtener categorías para el formulario
    categorias = db.execute_query("SELECT * FROM categorias ORDER BY nombre")
    return render_template('componentes/nuevo.html', categorias=categorias)


@app.route('/componentes/<int:componente_id>')
def ver_componente(componente_id):
    query = """
    SELECT c.*, cat.nombre as categoria_nombre 
    FROM componentes c 
    LEFT JOIN categorias cat ON c.categoria_id = cat.id 
    WHERE c.id = %s
    """
    componente = db.execute_query(query, (componente_id,))
    if componente:
        return render_template('componentes/detalle.html', componente=componente[0])
    else:
        flash('Componente no encontrado', 'error')
        return redirect(url_for('listar_componentes'))


@app.route('/componentes/editar/<int:componente_id>', methods=['GET', 'POST'])
def editar_componente(componente_id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        categoria_id = request.form['categoria_id']
        fabricante = request.form['fabricante']

        query = """
        UPDATE componentes 
        SET nombre=%s, descripcion=%s, precio=%s, stock=%s, categoria_id=%s, fabricante=%s
        WHERE id=%s
        """
        params = (nombre, descripcion, precio, stock,
                  categoria_id, fabricante, componente_id)

        if db.execute_query(query, params):
            flash('Componente actualizado exitosamente', 'success')
            return redirect(url_for('ver_componente', componente_id=componente_id))
        else:
            flash('Error al actualizar componente', 'error')

    # Obtener datos actuales del componente
    componente = db.execute_query(
        "SELECT * FROM componentes WHERE id = %s", (componente_id,))
    categorias = db.execute_query("SELECT * FROM categorias ORDER BY nombre")

    if componente:
        return render_template('componentes/editar.html', componente=componente[0], categorias=categorias)
    else:
        flash('Componente no encontrado', 'error')
        return redirect(url_for('listar_componentes'))


@app.route('/componentes/eliminar/<int:componente_id>', methods=['POST'])
def eliminar_componente(componente_id):
    query = "DELETE FROM componentes WHERE id = %s"
    if db.execute_query(query, (componente_id,)):
        flash('Componente eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar componente', 'error')
    return redirect(url_for('listar_componentes'))


@app.route('/categorias')
def listar_categorias():
    categorias = db.execute_query("SELECT * FROM categorias ORDER BY nombre")
    return render_template('categorias/lista.html', categorias=categorias)


@app.route('/categorias/nueva', methods=['GET', 'POST'])
def nueva_categoria():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']

        query = "INSERT INTO categorias (nombre, descripcion) VALUES (%s, %s)"
        params = (nombre, descripcion)

        if db.execute_query(query, params):
            flash('Categoría agregada exitosamente', 'success')
            return redirect(url_for('listar_categorias'))
        else:
            flash('Error al agregar categoría', 'error')

    return render_template('categorias/nueva.html')


@app.route('/buscar')
def buscar():
    termino = request.args.get('q', '')
    if termino:
        query = """
        SELECT c.*, cat.nombre as categoria_nombre 
        FROM componentes c 
        LEFT JOIN categorias cat ON c.categoria_id = cat.id
        WHERE c.nombre LIKE %s OR c.descripcion LIKE %s OR c.fabricante LIKE %s
        ORDER BY c.nombre
        """
        params = (f'%{termino}%', f'%{termino}%', f'%{termino}%')
        componentes = db.execute_query(query, params)
    else:
        componentes = []

    return render_template('buscar.html', componentes=componentes, termino=termino)


@app.route('/categorias/editar/<int:categoria_id>', methods=['POST'])
def editar_categoria(categoria_id):
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']

    query = "UPDATE categorias SET nombre=%s, descripcion=%s WHERE id=%s"
    params = (nombre, descripcion, categoria_id)

    if db.execute_query(query, params):
        flash('Categoría actualizada exitosamente', 'success')
    else:
        flash('Error al actualizar categoría', 'error')

    return redirect(url_for('listar_categorias'))


@app.route('/api/componentes')
def api_componentes():
    """API endpoint para obtener componentes en formato JSON"""
    categoria_id = request.args.get('categoria_id')
    if categoria_id:
        query = "SELECT * FROM componentes WHERE categoria_id = %s"
        componentes = db.execute_query(query, (categoria_id,))
    else:
        componentes = db.execute_query("SELECT * FROM componentes")
    return jsonify(componentes or [])


if __name__ == '__main__':
    # Configuración para producción
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
