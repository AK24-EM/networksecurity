import logging
from datetime import datetime
import os
import sys 
from networksecurity.exception import exception
log_file = f"{datetime.now().strftime('%d-%m-%Y')}_{datetime.now().strftime('%H_%M_%S')}_.log "

log_path = os.path.join(os.getcwd() , 'logs')
os.makedirs(log_path , exist_ok=True)

LOG_PATH_FILE = os.path.join(log_path , log_file)

logging.basicConfig(
    filename = LOG_PATH_FILE,

    format = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO
)

if __name__ == "__main__":
    raise NetworkSecurityException(e , sys)