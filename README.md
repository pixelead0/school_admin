# Proyecto Mattilda

## Descripción

Este proyecto implica la creación de un sistema backend con modelos para colegios, estudiantes y facturas, utilizando FastAPI, Postgres, Docker y posiblemente un marco de frontend como Vue.js.

## Uso

### Usando Makefile

El Makefile proporciona una forma sencilla de gestionar los contenedores Docker para el proyecto.

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

- **Ver registros:**

  ```sh
  make logs
  ```

- **Ejecutar pruebas:**
  ```sh
  make test
  ```

### Variables de Entorno

Cree un archivo `.env` con el siguiente contenido:

```
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=db
POSTGRES_HOST=db
POSTGRES_PORT=5432
SECRET_KEY=your_secret_key
ENVIRONMENT=development
PAGINATION_DEFAULT_LIMIT=10
```

### Docker Compose

Para ejecutar el proyecto utilizando Docker Compose, use el siguiente comando:

```sh
docker-compose up --build
```

m
