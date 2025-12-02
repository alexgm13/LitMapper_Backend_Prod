from pydantic_settings import BaseSettings, SettingsConfigDict
from urllib.parse import quote_plus

class Settings(BaseSettings):
    OPEN_API_KEY :str
    DB_USER: str 
    DB_PASSWORD: str
    DB_HOST: str 
    DB_PORT: str 
    DB_NAME: str
    URL_CORS: str
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    @property
    def DATABASE_URL(self) -> str:
        user = quote_plus(self.DB_USER)
        password = quote_plus(self.DB_PASSWORD)
        return f"postgresql://{user}:{password}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()

