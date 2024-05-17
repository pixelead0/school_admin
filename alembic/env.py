import os
from logging.config import fileConfig

from dotenv import load_dotenv  # Asegúrate de importar load_dotenv
from sqlalchemy import engine_from_config, pool

from alembic import context
from app.db.base import Base  # Importa tu Base
from app.models import *  # Importa todos tus modelos

load_dotenv()  # Carga las variables de entorno desde el archivo .env

# Carga la URL de la base de datos desde el archivo .env
DATABASE_URL = os.getenv("DATABASE_URL")

config = context.config

# Carga la URL de la base de datos en el archivo alembic.ini
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
