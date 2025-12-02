from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Todo FastAPI"
    database_url: str = "postgresql://postgres:postgres@localhost:5432/todo_db"
    
    # Mail configuration
    mail_username: str = ""
    mail_password: str = ""
    mail_from: str = ""
    mail_port: int = 587
    mail_server: str = ""
    mail_from_name: str = "Todo FastAPI"
    mail_starttls: bool = True
    mail_ssl_tls: bool = False
    use_credentials: bool = True
    validate_certs: bool = True

    model_config = SettingsConfigDict(env_file = ".env")

config = Settings()