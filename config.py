import os
from pathlib import Path

import dotenv
from loguru import logger

dotenv.load_dotenv()


logger.remove()  # Remove default handler

# Add only console handler initially to avoid permission issues during import
logger.add(
    sink=lambda msg: print(msg, end=""),  # Console output
    level="INFO",
    format="{time:HH:mm:ss} | {level} | {message}",
)

# Function to add file logger after startup
def setup_file_logger():
    """Setup file logging after application startup to ensure proper permissions"""
    try:
        # Ensure logs directory exists
        Path("logs").mkdir(exist_ok=True)

        # Add file logger
        logger.add(
            sink=Path("logs") / "app_{time:YYYY-MM-DD}.log",
            rotation="1 day",
            retention="30 days",
            level="INFO",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} | {message}",
            backtrace=True,
            diagnose=True,
        )
    except Exception as e:
        print(f"Failed to setup file logger: {e}")

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
BASE_URL = os.getenv("BASE_URL")
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
REDIS_URL = os.getenv("REDIS_URL")
AUTH_KEY = os.getenv("AUTH_KEY")
TERMINAL_ID = os.getenv("TERMINAL_ID")
TERMINAL_PASSWORD = os.getenv("TERMINAL_PASSWORD")

Path("logs").mkdir(exist_ok=True)
