from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    EMAIL = os.getenv("EMAIL", "youremail@example.com")
    FULL_NAME = os.getenv("FULL_NAME", "Your Full Name")
    STACK = os.getenv("STACK", "Python/FastAPI")

settings = Settings()
