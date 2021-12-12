def valid_token(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return inner
