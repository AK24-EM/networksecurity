import sys 
from networksecurity.logging import loggers


def error_detail_exception(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in file {0} at line {1}: {2}".format(
        file_name, line_number, str(error)
    )
    return error_message


class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_detail_exception(error_message, error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        loggers.logging.info("Enter the try")
        a = 1 / 0
        print(a)
        if a == ZeroDivisionError :
            loggers.logging.info("denominator should be greater then 0")
        logging.info("successfully executed")
    except Exception as e:
        raise NetworkSecurityException(e, sys)
