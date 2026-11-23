# Proyecto Python-Django: Blog

## Descripción breve y estructura del proyecto

El siguiente repositorio es un proyecto de Blog con un sistema de usuarios, posteos y etiquetas a estos posteos.

* **`blog_django/`**: Configuración general del proyecto Django (`settings.py`, `urls.py`, `wsgi.py` y `asgi.py`).

* **`accounts/`**: Aplicación encargada de la gestión de usuarios (`User`). Cubre el registro, inicio y cierre de sesión además de la edición del perfil (`Profile`) de la cuenta. Para esto, se cuentan con formularios, vistas y plantillas (`templates/accounts/`). 

* **`blogs_django/`**: Aplicación encargada de la gestión de posteos. Se tiene el CRUD de publicaciones (`Post`) y etiquetas (`Tag`) reservada sólo para administradores, carga de imagen por post, búsqueda, gestión de estados de las publicaciones (`borrador`, `publicado`, `archivado`) y vistas propias del usuario (`my_posts`), junto con sus formularios, rutas y plantillas en `templates/blogs_django/` entre otros. En cada caso se consideran los permisos de lectura, edición y eliminación según el usuario que haya iniciado la sesión.

* **`manage.py`**: Utilidad de línea de comandos de Django para ejecutar migraciones, crear superusuarios, correr el servidor de desarrollo y administrar el proyecto.
* **`requirements.txt`**: Lista de dependencias del entorno Python, incluyendo Django.
* **`db.sqlite3`**: Base de datos local en SQLite utilizada en desarrollo.
* **`.gitignore` y `.gitattributes`**: Reglas de Git para ignorar archivos temporales/locales (como entornos virtuales o caché) y normalizar atributos del repositorio.
* **`README.md`**: Documentación general del proyecto y guía de uso.

## Intrucciones de instalación

### Crear un entorno virtual

- `python -m venv venv`

### Instalar las dependencias

- `pip install -r requirements.txt` (incluye Django)

### Inicializar el servidor

- `python manage.py runserver`

### En caso de realizar cambios en los modelos de las aplicaciones y migrar

- `python manage.py makemigrations`
- `python manage.py migrate`

### Crear un superusuario

- `python manage.py createsuperuser`

## Archivo `db.sqlite3` y `media/`

El repositorio cuenta con una base de datos de prueba existente con un usuario admin (clave: 1234) y tres usuarios user1, user2 y user3 con las constraseñas user1password, user2password y user3password respectivamente. Ninguno de los usuario ni los posteos vinculados tienen fotos asociadas. Sin embargo, de agregarles, las mismas estarán en las carpetas `media/blogs_django/` y  `media/accounts/` según sea una foto de perfil o de una publicación.

## Comentarios del proyecto

### Problemas con Pillow

Al usar mi `venv` en Python, tuve dificultades intentando instalar Pillow. Por lo tanto, reemplacé en los modelos de los posts y cuentas el campo `ImageField` por `FileField`.

### Utilización de IA

- Interfaz de usuario: El front-end de este proyecto fue realizado con la asistencia de Gemini. Dado que se prioriza la entrega del proyecto, se utilizó fuertemente Tailwind CSS para la creación de clases en HTML.
- Corrección de funcionalidades: Con el testeo manual humano de algunas funciones, se han detectado bugs posteriormente corregidos con asistencia de Gemini. Este uso se debió a que las componentes a cambiar interactuaban con varias partes del modelo MVT y se debía realizar un seguimiento riguroso de estos cambios.

### Funcionalidades posibles que no se pudieron implementar

Algunas de las funcionalidades deseadas es tener un sistema de likes (dar/quitar like, ver la lista de usuarios que dieron like, permisos, etcétera) y comentarios a los posteos. Estas no las pude implementar dado que excedían lo requerido en el proyecto y el tiempo que le podía dedicar.

## Sobre el autor

Andrés R. Saravia: Computólogo, Matemático Aplicado y Analista de Datos
- [Página personal](https://andresrsaravia.github.io)
- [LinkedIn](https://www.linkedin.com/in/andresrsaravia/)
