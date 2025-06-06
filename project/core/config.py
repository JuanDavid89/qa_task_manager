from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    app_name: str = "QA Task Manager"
    environment: str = Field("development", env="ENVIRONMENT")
    debug: bool = Field(True, env="DEBUG")
    database_url: str = Field(..., env="DATABASE_URL")
    secret_key: str = Field(..., env="SECRET_KEY")
    access_token_expire_minutes: int = 60 * 24  # 1 día
    
    class Config:
        env_file = ".env"  # Archivo donde puedes guardar variables locales de entorno
        env_file_encoding = "utf-8"

settings = Settings()
