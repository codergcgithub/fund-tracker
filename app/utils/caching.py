from functools import lru_cache, wraps
from datetime import datetime, timedelta

def timed_lru_cache(seconds: int, maxsize: int = 128):
    """
    Decorator to create timed LRU cache. 
    Needed this to avoid sending too many requests to the provider and get blocked.
    :param seconds: int: expiration time in seconds
    :param maxsize: int: maximum cache size
    :return: function: wrapped function
    """
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.now() + func.lifetime

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.now() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.now() + func.lifetime
            return func(*args, **kwargs)

        return wrapped_func
    return wrapper_cache
