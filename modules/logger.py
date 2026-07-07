import logging
import json
import os
from datetime import datetime, timedelta

# Load settings.json
config_path = os.path.join("config", "settings.json")

with open(config_path, "r") as file:
    settings = json.load(file)

# Logging settings
log_file = settings["logging"]["log_file"]
log_level = settings["logging"]["level"]
retain_days = settings["logging"]["retain_days"]
auto_delete = settings["logging"]["auto_delete_old_logs"]

# Create logs folder
os.makedirs(os.path.dirname(log_file), exist_ok=True)

# Delete old log file if required
if auto_delete and os.path.exists(log_file):

    modified_time = datetime.fromtimestamp(os.path.getmtime(log_file))

    if datetime.now() - modified_time > timedelta(days=retain_days):
        os.remove(log_file)

# Convert INFO -> logging.INFO
level = getattr(logging, log_level.upper(), logging.INFO)

# Create logger
logger = logging.getLogger("SmartDocumentAnalysis")

logger.setLevel(level)

# Prevent duplicate logs
logger.handlers.clear()

# File Handler
file_handler = logging.FileHandler(log_file)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# Console Handler (optional)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)