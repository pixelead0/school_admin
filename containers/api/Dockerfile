FROM python:3.10-slim-bullseye AS python-base

WORKDIR /app

# Instala las dependencias del sistema necesarias
RUN apt-get update \
    && apt-get install --no-install-recommends -y curl build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

# Instala el plugin de exportación de Poetry y desactiva la advertencia
RUN poetry self add poetry-plugin-export \
    && poetry config virtualenvs.create false \
    && poetry config warnings.export false

# Copia los archivos de configuración de Poetry y el archivo de entorno
COPY pyproject.toml poetry.lock ./
COPY .env ./

# Bloquea e instala las dependencias del proyecto
RUN poetry lock \
    && poetry install --only main --no-interaction --no-ansi

# Copia el código de la aplicación
COPY ./app /app
COPY ./alembic /alembic
COPY ./alembic.ini /alembic.ini
# Comando para iniciar la aplicación
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8881"]
