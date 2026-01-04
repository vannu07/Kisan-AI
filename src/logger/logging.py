import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Try to use /tmp for logs in serverless environments, otherwise use logs/
log_dir = "/tmp/logs" if os.environ.get('VERCEL') else "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

handlers = [logging.StreamHandler(sys.stdout)]

# Only add file handler if we can write to the filesystem
try:
    os.makedirs(log_dir, exist_ok=True)
    handlers.append(logging.FileHandler(log_filepath))
except (OSError, PermissionError):
    # Running in a read-only environment (like Vercel), skip file logging
    pass

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=handlers
)

logger = logging.getLogger("kisanaiLogger")
