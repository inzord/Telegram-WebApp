import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance.POSTGRES_USER = os.getenv("POSTGRES_USER")
            cls._instance.POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
            cls._instance.POSTGRES_HOST = os.getenv("POSTGRES_HOST")
            cls._instance.POSTGRES_PORT = os.getenv("POSTGRES_PORT")
            cls._instance.POSTGRES_DB = os.getenv("POSTGRES_DB")
            cls._instance.TOKEN = os.getenv("TOKEN")
            cls._instance.VUE_BASE_URL = os.getenv("VUE_BASE_URL")
            cls._instance.FASTAPI_BASE_URL = os.getenv("FASTAPI_BASE_URL")
        return cls._instance

    @property
    def sync_database_url(self) -> str:
        return (f"postgres://{self.POSTGRES_USER}:"
                f"{self.POSTGRES_PASSWORD}@"
                f"{self.POSTGRES_HOST}:"
                f"{self.POSTGRES_PORT}/"
                f"{self.POSTGRES_DB}")

    @property
    def get_vue_base_url(self) -> str:
        return self.VUE_BASE_URL


settings = Settings()
