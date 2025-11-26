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
            print(
                f"Intentando conectar a: {db_config['host']}:{db_config['port']}")
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
    SELECT c.*, cat.nombre as categoria_nombre,
           (SELECT COUNT(*) FROM componente_proveedor cp WHERE cp.componente_id = c.id) as proveedores_count
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
        # Obtener proveedores asociados al componente
        proveedores_comp = db.execute_query(
            """
            SELECT p.*, cp.precio_proveedor, cp.tiempo_entrega_dias
            FROM componente_proveedor cp
            JOIN proveedores p ON cp.proveedor_id = p.id
            WHERE cp.componente_id = %s
            ORDER BY p.nombre
            """,
            (componente_id,)
        )

        # Obtener lista de proveedores disponibles (para vincular)
        proveedores = db.execute_query(
            "SELECT * FROM proveedores ORDER BY nombre")

        return render_template('componentes/detalle.html', componente=componente[0], proveedores_comp=proveedores_comp or [], proveedores=proveedores or [])
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


@app.route('/proveedores')
def listar_proveedores():
    proveedores = db.execute_query("SELECT * FROM proveedores ORDER BY nombre")
    return render_template('proveedores/lista.html', proveedores=proveedores)


@app.route('/proveedores/nuevo', methods=['GET', 'POST'])
def nuevo_proveedor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form.get('contacto')
        telefono = request.form.get('telefono')
        email = request.form.get('email')
        direccion = request.form.get('direccion')

        query = "INSERT INTO proveedores (nombre, contacto, telefono, email, direccion) VALUES (%s, %s, %s, %s, %s)"
        params = (nombre, contacto, telefono, email, direccion)
        if db.execute_query(query, params):
            flash('Proveedor agregado exitosamente', 'success')
            return redirect(url_for('listar_proveedores'))
        else:
            flash('Error al agregar proveedor', 'error')

    return render_template('proveedores/nuevo.html')


@app.route('/proveedores/<int:proveedor_id>')
def ver_proveedor(proveedor_id):
    proveedor = db.execute_query(
        "SELECT * FROM proveedores WHERE id = %s", (proveedor_id,))
    if not proveedor:
        flash('Proveedor no encontrado', 'error')
        return redirect(url_for('listar_proveedores'))

    proveedor = proveedor[0]
    # Obtener componentes que suministra
    componentes = db.execute_query(
        """
        SELECT c.*, cp.precio_proveedor, cp.tiempo_entrega_dias
        FROM componente_proveedor cp
        JOIN componentes c ON cp.componente_id = c.id
        WHERE cp.proveedor_id = %s
        ORDER BY c.nombre
        """,
        (proveedor_id,)
    )
    return render_template('proveedores/detalle.html', proveedor=proveedor, componentes=componentes or [])


@app.route('/proveedores/editar/<int:proveedor_id>', methods=['GET', 'POST'])
def editar_proveedor(proveedor_id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        contacto = request.form.get('contacto')
        telefono = request.form.get('telefono')
        email = request.form.get('email')
        direccion = request.form.get('direccion')

        query = "UPDATE proveedores SET nombre=%s, contacto=%s, telefono=%s, email=%s, direccion=%s WHERE id=%s"
        params = (nombre, contacto, telefono, email, direccion, proveedor_id)
        if db.execute_query(query, params):
            flash('Proveedor actualizado', 'success')
        else:
            flash('Error al actualizar proveedor', 'error')

        return redirect(url_for('listar_proveedores'))

    proveedor = db.execute_query(
        "SELECT * FROM proveedores WHERE id = %s", (proveedor_id,))
    if proveedor:
        return render_template('proveedores/editar.html', proveedor=proveedor[0])
    else:
        flash('Proveedor no encontrado', 'error')
        return redirect(url_for('listar_proveedores'))


@app.route('/proveedores/eliminar/<int:proveedor_id>', methods=['POST'])
def eliminar_proveedor(proveedor_id):
    query = "DELETE FROM proveedores WHERE id = %s"
    if db.execute_query(query, (proveedor_id,)):
        flash('Proveedor eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar proveedor', 'error')
    return redirect(url_for('listar_proveedores'))


@app.route('/componentes/<int:componente_id>/proveedores/add', methods=['POST'])
def add_proveedor_a_componente(componente_id):
    proveedor_id = request.form.get('proveedor_id')
    precio = request.form.get('precio_proveedor') or None
    tiempo = request.form.get('tiempo_entrega_dias') or None

    if not proveedor_id:
        flash('Debes seleccionar un proveedor', 'error')
        return redirect(url_for('ver_componente', componente_id=componente_id))

    query = "INSERT INTO componente_proveedor (componente_id, proveedor_id, precio_proveedor, tiempo_entrega_dias) VALUES (%s, %s, %s, %s)"
    params = (componente_id, proveedor_id, precio, tiempo)
    res = db.execute_query(query, params)
    if res:
        flash('Proveedor vinculado al componente', 'success')
    else:
        flash('Error al vincular proveedor (¿ya existe?)', 'error')
    return redirect(url_for('ver_componente', componente_id=componente_id))


@app.route('/componentes/<int:componente_id>/proveedores/remove/<int:proveedor_id>', methods=['POST'])
def remove_proveedor_de_componente(componente_id, proveedor_id):
    query = "DELETE FROM componente_proveedor WHERE componente_id=%s AND proveedor_id=%s"
    if db.execute_query(query, (componente_id, proveedor_id)):
        flash('Proveedor desvinculado del componente', 'success')
    else:
        flash('Error al desvincular proveedor', 'error')
    return redirect(url_for('ver_componente', componente_id=componente_id))


if __name__ == '__main__':
    # Configuración para producción
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
