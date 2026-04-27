""" #######################################################################################
# RECURSO ACADÉMICO CREADO POR LA PROFESORA MÓNICA TAHAN CON EL USO DE GOOGLE ANTIGRAVITY #
# ACADEMY RESOURCE CREATED BY PROFESSOR MÓNICA TAHAN WITH THE USE OF GOOGLE ANTIGRAVITY   #
# Este programa web desarrollado con Flask permite registrar, modificar, eliminar y       #
# consultar personas   #
# This script is a web application that allows you to register, modify, delete and        #
# consult people                                                                          #
# Product Owner: Prof. Mónica Tahan                                                       #
# Autor: Mónica Tahan y Google Antigravity AI                                             #
# Author: Mónica Tahan and Google Antigravity AI                                          #
# Versión: 1.0                                                                            #
# Version: 1.0                                                                            #
# Fecha: 28/02/2026                                                                       # 
# Date: 02/28/2026                                                                        #
# Licencia: GNU/GPL                                                                       #
# License: GNU/GPL                                                                        #
###########################################################################################
"""

from flask import Flask # Importamos la clase principal
from controllers.persona import persona_bp # Importamos el controlador Persona
from controllers.auth import auth_bp # Importamos el controlador Auth
import os

app = Flask(__name__)

# CONFIGURACION DE SESIONES Y SEGURIDAD
# Para producción en Hugging Face (que usa iframes), necesitamos que las cookies sean estables y compatibles.
app.secret_key = "unexpo-computacion1-seccion37-clave-segura"

# Configuraciones para que la sesión funcione dentro del iframe de Hugging Face
app.config.update(
    SESSION_COOKIE_SAMESITE='None',
    SESSION_COOKIE_SECURE=True
)

# Registramos los controladores (Blueprints)
# 'url_prefix' nos permite separar rutas lógicas fácilmente.
# 'auth' tendrá rutas como '/auth/login', '/auth/logout'
app.register_blueprint(auth_bp, url_prefix='/auth')
# 'persona' será la raíz '/'
app.register_blueprint(persona_bp, url_prefix='/')

# INICIO DE LA APLICACION
if __name__ == '__main__':
    # Obtenemos el puerto de las variables de entorno para Hugging Face (default 7860)
    port = int(os.environ.get("PORT", 7860))
    # Escuchamos en 0.0.0.0 para que el contenedor sea accesible
    app.run(host='0.0.0.0', port=port, debug=False)

