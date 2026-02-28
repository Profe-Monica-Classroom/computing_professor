import sqlite3

class UsuarioModel:
    def __init__(self):
        self.db_name = 'database.db'
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            # Crear tabla usuario con campo password NO ENCRIPTADO solo para efectos educativos simples.
            # En un entorno real siempre usar hash (como bcrypt, argon2, etc) para guardar contraseñas.
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuario (
                    idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
            ''')
            
            # Crear usuario admin por defecto si no existe al iniciar la app
            cursor.execute("SELECT * FROM usuario WHERE usuario = 'admin'")
            if not cursor.fetchone():
                cursor.execute("INSERT INTO usuario (usuario, password) VALUES ('admin', 'admin')")
            else:
                # Sincronizar contraseña si el usuario ya existe (por si se cambió en el código)
                cursor.execute("UPDATE usuario SET password = 'admin' WHERE usuario = 'admin'")
            
            conn.commit()


    # Método para verificar credenciales de login
    def login(self, usuario, password):
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row # Para acceder a columnas por nombre
                cursor = conn.cursor()
                # Buscamos coincidencia exacta de usuario y contraseña (¡OJO! Texto plano no es seguro para prod)
                cursor.execute("SELECT * FROM usuario WHERE usuario = ? AND password = ?", (usuario, password))
                return cursor.fetchone() # Retorna el usuario si existe, o None si no
        except Exception as e:
            print(f"Error en login: {e}")
            return None

    # Método para registrar un nuevo usuario
    def registrar(self, usuario, password):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                # Verificar si el usuario ya existe
                cursor.execute("SELECT idusuario FROM usuario WHERE usuario = ?", (usuario,))
                if cursor.fetchone():
                    return False, "El nombre de usuario ya está en uso."
                
                # Insertar nuevo usuario
                cursor.execute("INSERT INTO usuario (usuario, password) VALUES (?, ?)", (usuario, password))
                conn.commit()
                return True, "Registro exitoso. Ahora puedes iniciar sesión."
        except Exception as e:
            print(f"Error en registro: {e}")
            return False, f"Error al procesar el registro: {e}"

