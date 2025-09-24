import functools
from utils.logger import logger

def handle_exception(func):

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            logger.error(f"Exception in {func.__name__}: {e}",exc_info=True)
            return f"An error occured: {str(e)}"
    return wrapper