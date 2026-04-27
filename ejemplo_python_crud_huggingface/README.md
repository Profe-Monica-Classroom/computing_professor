# ☁️ Proyecto CRUD: Registro de Personas (Cloud - Hugging Face & Docker)

Esta versión del sistema de Registro de Personas está optimizada para el despliegue en la nube a través de **Hugging Face Spaces** utilizando contenedores **Docker**.

---

# ☁️ CRUD Project: Registration of Persons (Cloud - Hugging Face & Docker)

This version of the Registration of Persons system is optimized for cloud deployment via **Hugging Face Spaces** using **Docker** containers.

---

## 🛠️ Características Especiales (Special Features)
- **Despliegue**: Dockerizado para máxima compatibilidad.
- **Producción**: Utiliza `Gunicorn` como servidor profesional.
- **Seguridad de Sesión**: Configuración fija de `secret_key` y cookies `SameSite=None` para permitir el funcionamiento dentro de iFrames (requerido por Hugging Face).
- **Estabilidad**: Configurado con un solo trabajador (`workers 1`) para garantizar la persistencia de la sesión.

---

## Special Features

- **Deployment**: Dockerized for maximum compatibility.
- **Production**: Uses `Gunicorn` as a professional server.
- **Session Security**: Fixed `secret_key` configuration and `SameSite=None` cookies to allow operation within iFrames (required by Hugging Face).
- **Stability**: Configured with a single worker (`workers 1`) to ensure session persistence.

---

## 🚀 Despliegue

### Opción A: Mediante el formulario de Upload Files de Hugging Face
Sube la carpeta con el proyecto directamente a tu Space en Hugging Face.

### Opción B: Mediante Git
1. Crea un nuevo Space de tipo **Docker**.
2. Haz el commit del contenido de esta carpeta:
   ```bash
   git add .
   git commit -m "Despliegue inicial en Hugging Face"
   git push origin main
   ```

---

## 🚀 Deployment

### Option A: Using the Hugging Face Upload Files form
Upload the folder with the project directly to your Space on Hugging Face.

### Option B: Using Git
1. Create a new **Docker** type Space.
2. Commit the contents of this folder:
   ```bash
   git add .
   git commit -m "Initial deployment on Hugging Face"
   git push origin main
   ```

---

## 🔧 Archivos Clave (Key Files)
- `Dockerfile`: Instrucciones para construir el contenedor.
- `app.py`: Configuración optimizada para la nube.
- `requirements.txt`: Dependencias requeridas.

---

## 🔧 Key Files
- `Dockerfile`: Instructions for building the container.
- `app.py`: Configuration optimized for the cloud.
- `requirements.txt`: Required dependencies.

---

## 🎓 Créditos

- **Product Owner**: Prof. Mónica Tahan
- **Desarrollo**: Mónica Tahan & Google Antigravity AI
- **Institución**: UNEXPO - Nucleo Guarenas
- **Asignatura**: Computación 1
- **Sección**: 37

---
> [!NOTA]
> Este proyecto tiene fines puramente didácticos para la enseñanza de estructuras de datos y desarrollo web en ingeniería.

---

## 🎓 Credits

- **Product Owner**: Prof. Mónica Tahan
- **Development**: Mónica Tahan & Google Antigravity AI
- **Institution**: UNEXPO - Nucleo Guarenas
- **Course**: Computación 1
- **Section**: 37

---
> [!NOTE]
> This project is for purely didactic purposes for teaching data structures and web development in engineering.
