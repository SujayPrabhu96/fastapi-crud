from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Todo FastAPI"
    database_url: str = "postgresql://postgres:postgres@localhost:5432/todo_db"

    model_config = SettingsConfigDict(env_file = ".env")

config = Settings()