import os

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

dotenv_path = os.path.join(os.path.dirname(__file__), "../../.env")


class DBSettings(BaseSettings):
    postgres_user: str = "postgres"
    postgres_password: str
    postgres_server: str = "postgres"
    postgres_port: str = "5432"
    postgres_db: str = "postgres"
    postgres_db_test: str = "postgres_test"

    model_config = SettingsConfigDict(env_file=dotenv_path, extra="ignore")


class AppSettings(BaseSettings):
    project_name: str = "pychecker"
    project_host: str = "127.0.0.1"
    project_port: int = 8080

    secret_key: str

    algorithm: str = "HS256"

    db_set: DBSettings = DBSettings()
    database_dsn: str = str(
        PostgresDsn(
            f"postgresql+asyncpg://{db_set.postgres_user}:"
            f"{db_set.postgres_password}@{db_set.postgres_server}:"
            f"{db_set.postgres_port}/{db_set.postgres_db}"
        )
    )
    database_test_dsn: str = str(
        PostgresDsn(
            f"postgresql+asyncpg://{db_set.postgres_user}:"
            f"{db_set.postgres_password}@{db_set.postgres_server}:"
            f"{db_set.postgres_port}/{db_set.postgres_db_test}",
        )
    )

    model_config = SettingsConfigDict(env_file=dotenv_path, extra="ignore")


app_settings = AppSettings()
