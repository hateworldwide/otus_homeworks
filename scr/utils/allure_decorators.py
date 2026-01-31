import allure
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

def screenshot_on_fail(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            try:
                png = self.driver.get_screenshot_as_png()
                allure.attach(
                    png,
                    name="Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception:
                pass
            raise e
    return wrapper
