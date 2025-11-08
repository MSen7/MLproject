import logging
import os
from datetime import datetime

# ✅ Always point logs to project root (not src)
PROJECT_ROOT = os.getcwd()  # <-- this guarantees root when executed from root

LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s in %(name)s:%(lineno)d - %(message)s",
    level=logging.INFO,
)
