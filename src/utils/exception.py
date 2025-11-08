import sys
from src.utils.logger import logging   # ✅ use logging configured in logger.py

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    return (
        f"Error occurred in script: [{file_name}] "
        f"at line: [{exc_tb.tb_lineno}] "
        f"with message: [{str(error)}]"
    )


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        message = error_message_detail(error_message, error_detail)
        self.error_message = message

        logging.error(message)  # ✅ <--- THIS WILL WRITE TO LOG FILE

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        x = 1 / 0
    except Exception as e:
        raise CustomException(e, sys)
