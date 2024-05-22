from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    postgres_url: str

    class Config:
        env_file = ".env"

settings = Settings()
