### SCHOOL ADMIN

El sistema es una aplicación web para la gestión de colegios, estudiantes, facturas y pagos, desarrollada utilizando FastAPI y SQLAlchemy para la API y la manipulación de la base de datos, respectivamente. A continuación se presenta un resumen de sus características principales:

### Características Principales

1. **Gestión de Usuarios:**

   - **Creación y autenticación de usuarios:** Permite la creación de nuevos usuarios y la autenticación mediante tokens JWT.

2. **Gestión de Colegios:**

   - **CRUD de colegios:** Permite crear, leer, actualizar y eliminar registros de colegios.
   - **Información detallada de colegios:** Almacena detalles como nombre, país, estado y descripción.

3. **Gestión de Estudiantes:**

   - **CRUD de estudiantes:** Permite crear, leer, actualizar y eliminar registros de estudiantes.
   - **Información detallada de estudiantes:** Incluye nombre, apellidos, matrícula, grado y colegio

4. **Gestión de Facturas:**

   - **CRUD de facturas:** Permite crear, leer, actualizar y eliminar registros de facturas.
   - **Información detallada de facturas:** Incluye el monto, la fecha, el estudiante y el pago asociado.

5. **Gestión de Pagos:**

   - **CRUD de pagos:** Permite crear, leer, actualizar y eliminar registros de pagos.
   - **Información detallada de pagos:** Incluye el estudiante, el colegio y el tipo de pago asociado.

6. **Tipos de Pagos:**

   - **CRUD de tipos de pagos:** Permite crear, leer, actualizar y eliminar registros de tipos de pagos.
   - **Información detallada de tipos de pagos:** Incluye nombre y precio del tipo de pago.

7. **Grados:**

   - **CRUD de grados:** Permite crear, leer, actualizar y eliminar registros de grados.
   - **Información detallada de grados:** Incluye el nombre del grado y el colegio asociado.

8. **Autenticación y Seguridad:**

   - **Tokens JWT:** Autenticación basada en tokens JWT para proteger las rutas de la API.
   - **Dependencias de seguridad:** Uso de dependencias para garantizar que solo los usuarios autenticados puedan acceder a ciertas rutas.

9. **Configuración y despliegue:**

   - **Configuración basada en entorno:** Uso de variables de entorno para configurar la aplicación.
   - **Docker y Docker Compose:** Contenedorización de la aplicación y sus servicios asociados (base de datos PostgreSQL y pgAdmin) para facilitar el despliegue.

10. **Migraciones de Base de Datos:**

    - **Alembic:** Herramienta para manejar las migraciones de la base de datos.

11. **Testing:**
    - **Pytest:** Uso de pytest para escribir y ejecutar pruebas automatizadas.
    - **Fixtures:** Uso de fixtures para configurar el entorno de prueba, incluyendo la creación de usuarios y autenticación.

### Estructura del Proyecto

- **alembic/**: Contiene configuraciones y scripts para manejar las migraciones de la base de datos.
- **app/core/**: Contiene configuraciones de la aplicación, seguridad, y configuración de logging.
- **app/crud/**: Contiene funciones para realizar operaciones CRUD (Create, Read, Update, Delete) en los modelos de la base de datos.
- **app/db/**: Contiene la configuración de la base de datos y la inicialización de la sesión de la base de datos.
- **app/models/**: Contiene los modelos ORM de SQLAlchemy para representar las tablas de la base de datos.
- **app/routers/**: Contiene los enrutadores de FastAPI para definir las rutas de la API.
- **app/schemas/**: Contiene los esquemas de Pydantic para validación de datos y serialización.
- **app/tests/**: Contiene las pruebas automatizadas de la aplicación.
- **containers/**: Contiene los Dockerfiles para la aplicación y pgAdmin.
- **docker-compose.yml**: Archivo de configuración de Docker Compose para orquestar los servicios.
- **Makefile**: Contiene comandos para construir, ejecutar y gestionar la aplicación.

# Uso

Para levantar el proyecto, es necesario tener instalados ciertos requisitos y seguir algunos pasos para configurarlo y ejecutarlo correctamente. Aquí tienes una lista detallada de los requisitos y los pasos necesarios:

### Requisitos Previos

1. **Instalación de Docker y Docker Compose:**

   - Docker: Asegúrate de tener Docker instalado en tu sistema. Puedes descargarlo desde [aquí](https://www.docker.com/products/docker-desktop).
   - Docker Compose: Docker Compose suele venir incluido con Docker Desktop. Verifica la instalación con `docker-compose --version`.

2. **Clonar el Repositorio del Proyecto:**
   - Usa `git clone <URL_DEL_REPOSITORIO>` para clonar el repositorio del proyecto en tu máquina local.

### Archivos de Configuración

3. **Archivo `.env`:**

   - Asegúrate de que el archivo `.env` esté presente en el directorio raíz del proyecto. Este archivo contiene configuraciones sensibles y variables de entorno necesarias para el funcionamiento del proyecto.

   ```env
   POSTGRES_USER=user
   POSTGRES_PASSWORD=password
   POSTGRES_DB=db
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   SECRET_KEY=your_secret_key
   ENVIRONMENT=development
   PAGINATION_DEFAULT_LIMIT=10
   DATABASE_URL=postgresql+psycopg2://user:password@db:5432/db
   ```

### Instalación y Ejecución

**Construir y Levantar los Contenedores:**
Navega al directorio del proyecto y ejecuta el siguiente comando para construir y levantar los contenedores definidos en `docker-compose.yml`:

     ```bash
     docker-compose up --build
     ```

## Comandos Makefile

El proyecto incluye un `Makefile` con comandos útiles para gestionar el ciclo de vida de los contenedores y otras tareas comunes.

- **Ayuda**

  ```sh
  make help
  ```

  - **Construir el proyecto:**

  ```sh
  make build
  ```

- **Iniciar el proyecto:**

  ```sh
  make up
  ```

- **Detener el proyecto:**

  ```sh
  make down
  ```

- **Limpiar el proyecto (eliminar todos los contenedores, imágenes y volúmenes):**

  ```sh
  make clean
  ```

- **Reiniciar el proyecto:**

  ```sh
  make restart
  ```

- **Mostrar listado de los contenedores en ejecución:**

  ```sh
  make ps
  ```

- **Ver todos los registros:**

  ```sh
  make logs
  ```

- **Ver registros de la app:**

  ```sh
  make logs_api
  ```

- **Actualzar paquetes pip:**

  ```sh
  make requirements
  ```

- **Crear nueva migracion:**

  ```sh
  make revision msg="Nombre migracion"
  ```

- **Crear aplicar migracion:**

  ```sh
  make upgrade
  ```

- **Crear reversar migracion:**

  ```sh
  make downgrade
  ```

- **Ejecutar pruebas:**

  ```sh
  make test
  ```

- **Limpieza de código:**
  ```sh
  make lint
  ```

### Acceso a la Aplicación

**Acceso a la API:**

- Una vez que los contenedores estén levantados, la aplicación debería estar accesible en `http://localhost:8881`.

### Configuración Adicional (Opcional)

**pgAdmin:**

- Si necesitas acceder a la base de datos PostgreSQL a través de pgAdmin, asegúrate de que el contenedor pgAdmin esté configurado correctamente en `docker-compose.yml`. Accede a pgAdmin en `http://localhost:8484` con las credenciales definidas en `containers/pgadmin/pgadmin.env`.

  ```env
  PGADMIN_DEFAULT_EMAIL=admin@correo.com
  PGADMIN_DEFAULT_PASSWORD=toor
  ```

### Pruebas

. **Ejecución de Pruebas:**

- Puedes ejecutar las pruebas automatizadas usando el comando definido en el Makefile:

  ```bash
  make test
  ```
