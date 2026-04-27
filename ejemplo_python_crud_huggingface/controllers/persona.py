from flask import Blueprint, render_template, request, redirect, url_for, session, g

# Para proteger la ruta, necesitamos verificar si el usuario está en la sesión
# Este es un DECORADOR, algo que envuelve una función para modificar su comportamiento sin cambiar su código.
# Es equivalente a poner un 'if(!isset($_SESSION))' al principio de cada método en PHP.
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Si 'user_id' no existe en la sesión, REDIRIGIMOS al login.
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        # Si existe, permitimos ejecutar la función original (f).
        return f(*args, **kwargs)
    return decorated_function

# Importamos las dependencias
from models.persona import PersonaModel

persona_bp = Blueprint('persona', __name__)

model = PersonaModel()

# Ahora usamos @login_required para proteger las rutas
# Esta ruta SOLO funcionará si hay una sesión activa.
@persona_bp.route('/')
@login_required 
def index():
    personas = model.listar()
    # Enviamos 'user' a la plantilla para saludar "Hola, Admin"
    return render_template('index.html', personas=personas, user=session['username'])

# Muestra el formulario de crear/editar
@persona_bp.route('/crud')
@login_required # Protegido
def crud():
    idpersona = request.args.get('idpersona')
    alm = None
    if idpersona:
        alm = model.obtener(idpersona) # Para editar
    return render_template('form.html', alm=alm, user=session['username'])

# Procesa el formulario (Guardar)
@persona_bp.route('/guardar', methods=['POST'])
@login_required
def guardar():
    # Obtenemos datos del formulario
    idpersona = request.form.get('idpersona')
    nombres = request.form.get('Nombres')
    cedula = request.form.get('Cedula')
    fecha_nmto = request.form.get('FechaNacimiento')
    direccion = request.form.get('direccion')
    email = request.form.get('correo')
    
    # Llamamos al modelo para guardar en DB
    model.guardar(idpersona, nombres, cedula, fecha_nmto, direccion, email)
    
    # Redirigimos al índice
    return redirect(url_for('persona.index'))

# Elimina un registro
@persona_bp.route('/eliminar')
@login_required
def eliminar():
    idpersona = request.args.get('idpersona')
    model.eliminar(idpersona)
    return redirect(url_for('persona.index'))
