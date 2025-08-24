import logging
import os
from datetime import datetime

# Log file ka naam (date-time ke sath)
LOG_FILE = f"app_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Logs folder ka path
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# File ka complete path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),   # File me log save hoga
        logging.StreamHandler()               # Console par bhi log dikhayega
    ]
)

