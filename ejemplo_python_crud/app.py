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
# Usamos una clave fija para que las sesiones no se cierren cada vez que reiniciamos el servidor durante el desarrollo.
app.secret_key = "unexpo-computacion1-seccion37-clave-segura"

# Registramos los controladores (Blueprints)
# 'url_prefix' nos permite separar rutas lógicas fácilmente.
# 'auth' tendrá rutas como '/auth/login', '/auth/logout'
app.register_blueprint(auth_bp, url_prefix='/auth')
# 'persona' será la raíz '/'
app.register_blueprint(persona_bp, url_prefix='/')

# INICIO DE LA APLICACION
if __name__ == '__main__':
    # debug=True permite ver errores detallados en el navegador y recargar automáticamente al salvar cambios.
    # NUNCA usar en producción real.
    app.run(debug=True)
