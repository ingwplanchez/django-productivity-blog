# Blog de Productividad con Django

Este es un proyecto de blog personal desarrollado con el framework Django. Fue creado como parte de un proceso de aprendizaje para practicar y consolidar conceptos clave de desarrollo web con Django.

## Características Implementadas

El proyecto cuenta con las siguientes funcionalidades, construidas paso a paso para explorar las capacidades del framework:

  - **Modelos de Datos:** Se crearon modelos para `Post` (Publicaciones) y `Comment` (Comentarios), con relaciones de clave foránea para enlazar autores y comentarios a publicaciones.
  - **Panel de Administración:** Uso del panel de administración integrado de Django para la gestión completa de publicaciones y comentarios.
  - **Vistas y URLs:** Implementación de vistas basadas en funciones para listar todos los posts y ver el detalle de cada uno.
  - **Sistema de Plantillas:** Uso del motor de plantillas de Django para renderizar las páginas del blog, incluyendo herencia de plantillas (`base.html`) para un diseño consistente.
  - **Formularios de Comentarios:** Un formulario de comentarios integrado en la vista de detalle de cada post, permitiendo a los usuarios dejar sus opiniones.
  - **Autenticación Básica:** Lógica en las vistas para verificar si un usuario ha iniciado sesión antes de permitirle enviar un comentario.
  - **Archivos Estáticos y Multimedia:** Configuración para servir archivos estáticos (CSS) y multimedia (imágenes), con integración del framework CSS **Bootstrap** para un diseño responsivo y moderno.
  - **Editor de Texto Enriquecido:** Integración de **Django-CKEditor** en el panel de administración, permitiendo formatear el contenido de los posts con negritas, títulos y la posibilidad de insertar imágenes complementarias.

## Próximos Pasos

El proyecto está en constante desarrollo y se planean las siguientes mejoras:

  - **Sistema de Autenticación de Usuarios:** Implementación de vistas y URLs de frontend para que los usuarios puedan registrarse, iniciar sesión y cerrar sesión sin necesidad de usar el panel de administración.
  - **Paginación:** Agregar paginación a la lista de posts para mejorar el rendimiento y la experiencia de usuario al navegar por el blog.
  - **Vistas Basadas en Clases (Opcional)**: Refactorizar las vistas actuales para usar ListView y DetailView de Django. Esto hará que el código sea más limpio, reutilizable y escalable.

## Configuración del Entorno

Para ejecutar este proyecto localmente, sigue estos pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/ingwplanchez/django-productivity-blog.git
    cd django-productivity-blog
    ```
2.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows
    .\venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```
3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
  4.  **Configura la base de datos y crea el superusuario:**

   ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
  ```
5.  **Ejecuta el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    Ahora puedes acceder a la aplicación en `http://127.0.0.1:8000/blog/` y al panel de administración en `http://127.0.0.1:8000/admin/`.

