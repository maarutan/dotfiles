from services.logger import logger


def log_exceptions(func, status: str = "i"):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger(status, f"config {func.__name__}: {e}")

    return wrapper
