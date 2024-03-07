import time

from loguru import logger


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        class_name = args[0].__class__.__name__
        end_time = time.time()
        execution_time = end_time - start_time
        logger.debug(f"{class_name}.{func.__name__} executed in {execution_time:.4f} seconds.")
        return result

    return wrapper
