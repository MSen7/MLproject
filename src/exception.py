import sys
import logging
from logger import *

logging.basicConfig(
    filename="app.log",
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = f"Error occurred in script [{file_name}] at line [{exc_tb.tb_lineno}] with message [{error}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail):
        super().__init__(error)
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        return self.error_message


