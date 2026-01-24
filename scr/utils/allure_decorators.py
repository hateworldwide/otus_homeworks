import logging

from functools import wraps



def log_action(func):
    @wraps(func)
    def wrapper(self, *args):
        logger = logging.getLogger(self.__class__.__name__)
        logger.info(f"Execute function: \"{func.__name__}\" with args: {args}")
        try:
            result = func(self, *args)
            logger.info(f"Successfully done: \"{func.__name__}\"")
            return result
        except Exception as e:
            logger.exception(f"Error in {func.__name__}: {e}")
            raise
    return wrapper