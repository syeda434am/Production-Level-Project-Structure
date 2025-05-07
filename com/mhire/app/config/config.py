import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.openai_api_key = os.getenv("SOME_API_KEY")
            cls._instance.openai_endpoint = os.getenv("SOME_ENDPOINT")
            cls._instance.model = os.getenv("MODEL_NAME")
            cls._instance.db_url = os.getenv("DB_URL")
            # other config vars...
        return cls._instance
