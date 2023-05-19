'''
Logging is a very useful tool in a programmer’s toolbox. 
It can help you develop a better understanding of the flow of a program and discover scenarios that you might not even have thought of while developing.
'''

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
logs_path = os.path.join(os.getcwd(), 'logs',LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )

# if __name__ == '__main__':
#     logging.info("Logging has started")