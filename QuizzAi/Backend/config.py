from dotenv import load_dotenv
import os

load_dotenv()
class Config:
    ENVIRONMENT = os.getenv("Deepseek","dev")
    API_KEY = os.getenv("API_KEY")
    HOST= "0.0.0.0"
    PORT: 8000
    MAX_PDF_SIZE=10*1024*1024

    @classmethod
    def isdev(cls):
        return cls.ENVIRONMENT=="dev"
    @classmethod
    def validate(cls):
        print(f"   Configuration loaded:")
        print(f"   Environment: {cls.ENVIRONMENT}")
        print(f"   Max PDF Size: {cls.MAX_PDF_SIZE / (1024*1024)} MB")

