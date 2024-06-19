import sys
from src.logger import logging
def message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message

class Custom_exception(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

# Example usage
try:
    # Simulate an error
    1 / 0
except Exception as e:
    logging.info("Divide by zero")
    raise Custom_exception(str(e), sys)
