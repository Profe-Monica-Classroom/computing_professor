from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.usuario import UsuarioModel
import random
import string
import base64
from io import BytesIO
from captcha.image import ImageCaptcha # Librería para generar imágenes captcha

# Blueprint para Autenticación (Login/Logout)
auth_bp = Blueprint('auth', __name__)
model = UsuarioModel()

# Función para generar un captcha de imagen mas moderno
def generar_captcha_imagen():
    # Generar una cadena aleatoria de 4 caracteres (letras y números)
    caracteres = string.ascii_uppercase + string.digits
    captcha_text = ''.join(random.choice(caracteres) for _ in range(4))
    session['captcha_text'] = captcha_text # Guardar en sesión para validar
    
    # Crear la imagen con la librería
    image = ImageCaptcha(width=200, height=80)
    data = image.generate(captcha_text)
    
    # Convertir la imagen a Base64 para enviarla al HTML sin archivos temporales
    buffered = BytesIO()
    buffered.write(data.getvalue())
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"

# Ruta para Login
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Validar Captcha Primero
        captcha_user = request.form.get('captcha_input', '').upper()
        if not captcha_user or captcha_user != session.get('captcha_text'):
            flash('Código de seguridad incorrecto. Inténtalo de nuevo.')
            return redirect(url_for('auth.login'))

        usuario = request.form['usuario']
        password = request.form['password']
        
        user = model.login(usuario, password)
        
        if user:
            session['user_id'] = user['idusuario']
            session['username'] = user['usuario']
            return redirect(url_for('persona.index'))
        else:
            flash('Usuario o contraseña incorrectos')
            
    captcha_img = generar_captcha_imagen()
    return render_template('login.html', captcha_img=captcha_img)

# Ruta para Registro
@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Validar Captcha
        captcha_user = request.form.get('captcha_input', '').upper()
        if not captcha_user or captcha_user != session.get('captcha_text'):
            flash('Código de seguridad incorrecto. Inténtalo de nuevo.')
            return render_template('registro.html', captcha_img=generar_captcha_imagen())

        usuario = request.form['usuario']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Las contraseñas no coinciden')
        else:
            success, message = model.registrar(usuario, password)
            if success:
                flash(message)
                return redirect(url_for('auth.login'))
            else:
                flash(message)
                
    captcha_img = generar_captcha_imagen()
    return render_template('registro.html', captcha_img=captcha_img)



# Ruta para cerrar sesión

@auth_bp.route('/logout')
def logout():
    # Limpiar todos los datos de la sesión
    session.clear()
    # Redirigir al login
    return redirect(url_for('auth.login'))
