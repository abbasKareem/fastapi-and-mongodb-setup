from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "FARM Intro"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str = "mongodb+srv://abbas123:abbas123@cluster0.g2owv.mongodb.net/farmstack?retryWrites=true&w=majority"
    DB_NAME: str = "farmstack"


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()
