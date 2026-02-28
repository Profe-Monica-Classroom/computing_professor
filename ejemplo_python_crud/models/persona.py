import sqlite3 # Importamos el módulo 'sqlite3' para interactuar con la base de datos SQLite (equivalente a usar PDO con MySQL en PHP)

class PersonaModel:
    # Constructor de la clase, se ejecuta al crear una instancia (equivalente a __CONSTRUCT en PHP)
    def __init__(self):
        # Definimos el nombre del archivo de la base de datos
        self.db_name = 'database.db'
        # Llamamos al método para inicializar la base de datos si no existe
        self.init_db()

    # Método para crear la tabla si no existe (en PHP solíamos tener un script SQL separado, aquí lo hacemos por código)
    def init_db(self):
        # Usamos 'with' para manejar la conexión. Se conecta y se desconecta automáticamente al terminar el bloque.
        # Es más seguro que abrir y cerrar manualmente (en PHP: $pdo = new PDO(...))
        with sqlite3.connect(self.db_name) as conn:
            # Creamos un cursor, que es el objeto que nos permite ejecutar comandos SQL
            cursor = conn.cursor()
            # Ejecutamos la consulta SQL para crear la tabla 'persona'
            # Usamos IF NOT EXISTS para que no de error si ya existe
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS persona (
                    idpersona INTEGER PRIMARY KEY AUTOINCREMENT, -- ID autoincremental
                    nombres TEXT NOT NULL,                       -- Campo de texto obligatorio
                    cedula TEXT NOT NULL,                        -- Campo de texto obligatorio
                    fecha_nmto TEXT NOT NULL,                    -- Campo de texto (fecha)
                    direccion TEXT NOT NULL,                     -- Campo de texto
                    email TEXT NOT NULL                          -- Campo de texto
                )
            ''')
            # Guardamos los cambios en la base de datos (commit)
            conn.commit()

    # Método para listar todos los registros (equivalente a Listar() en PHP)
    def listar(self):
        try:
            # Abrimos conexión a la base de datos
            with sqlite3.connect(self.db_name) as conn:
                # Configuramos para que los resultados se comporten como diccionarios/arrays asociativos
                # Esto permite acceder a los campos por nombre (ej: fila['nombres']), similar a PDO::FETCH_OBJ o PDO::FETCH_ASSOC
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                # Ejecutamos la consulta SELECT
                cursor.execute("SELECT * FROM persona")
                # fetchall() recupera TODAS las filas encontradas y las retorna como una lista
                return cursor.fetchall()
        except Exception as e:
            # Si ocurre un error, lo imprimimos en la consola
            print(f"Error al listar: {e}")
            return [] # Retornamos una lista vacía en caso de error

    # Método para obtener una sola persona por su ID (equivalente a Getting($id) en PHP)
    def obtener(self, idpersona):
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                # Usamos ? como marcador de posición para evitar Inyección SQL (Prepared Statements)
                # Es idéntico a usar prepare() y execute() en PDO de PHP
                cursor.execute("SELECT * FROM persona WHERE idpersona = ?", (idpersona,))
                # fetchone() recupera SOLO la primera fila encontrada
                return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener: {e}")
            return None

    # Método para eliminar un registro (equivalente a Eliminar($id) en PHP)
    def eliminar(self, idpersona):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                # Ejecutamos la sentencia DELETE usando parámetros seguros
                cursor.execute("DELETE FROM persona WHERE idpersona = ?", (idpersona,))
                # ¡Importante! En INSERT/UPDATE/DELETE siempre debemos hacer commit() para guardar cambios
                conn.commit()
        except Exception as e:
            print(f"Error al eliminar: {e}")

    # Método para guardar (Registrar o Actualizar)
    # Recibe todos los campos necesarios. En PHP recibíamos un objeto $data, aquí argumentos individuales
    def guardar(self, idpersona, nombres, cedula, fecha_nmto, direccion, email):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                # Verificamos si hay un ID válido para decidir si es ACTUALIZAR o INSERTAR
                # Equivalente a: $alm->idpersona > 0 ? Actualizar() : Registrar()
                if idpersona and int(idpersona) > 0:
                    # Lógica de ACTUALIZAR (UPDATE)
                    sql = '''UPDATE persona SET 
                                nombres = ?, 
                                cedula = ?,
                                fecha_nmto = ?,
                                direccion = ?, 
                                email = ?
                            WHERE idpersona = ?'''
                    # Pasamos los valores en una tupla, incluyendo el ID al final
                    cursor.execute(sql, (nombres, cedula, fecha_nmto, direccion, email, idpersona))
                else:
                    # Lógica de REGISTRAR (INSERT)
                    sql = "INSERT INTO persona (nombres, cedula, fecha_nmto, direccion, email) VALUES (?, ?, ?, ?, ?)"
                    # Pasamos los valores en una tupla
                    cursor.execute(sql, (nombres, cedula, fecha_nmto, direccion, email))
                
                # Confirmamos la transacción
                conn.commit()
        except Exception as e:
            print(f"Error al guardar: {e}")
