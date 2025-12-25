import os
import dotenv

dotenv.load_dotenv()


CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
BASE_URL = os.getenv("BASE_URL")
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
REDIS_URL = os.getenv("REDIS_URL")
AUTH_KEY = os.getenv("AUTH_KEY")
TERMINAL_ID = os.getenv("TERMINAL_ID")
TERMINAL_PASSWORD = os.getenv("TERMINAL_PASSWORD")

