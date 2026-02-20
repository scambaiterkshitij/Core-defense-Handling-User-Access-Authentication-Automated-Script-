import os
from config import LOG_PATHS

def find_auth_log():
    for path in LOG_PATHS:
        if os.path.exists(path):
            return path
    return None
