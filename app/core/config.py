from pydantic import BaseSettings


class Settings(BaseSettings):
    PAGINATION_DEFAULT_LIMIT: int = 10
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()
