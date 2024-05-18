from pydantic import BaseSettings


class Settings(BaseSettings):
    PAGINATION_DEFAULT_LIMIT: int = 10
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = "postgresql+psycopg2://user:password@db:5432/db"
    SECRET_KEY: str = "QWAZXS"  # Agrega la clave secreta para JWT
    ALGORITHM: str = "HS256"  # Algoritmo para JWT

    class Config:
        env_file = ".env"


settings = Settings()
