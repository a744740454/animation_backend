def valid_token(func):
    def inner(*args, **kwargs):
        print("hello")
        result = func(*args, **kwargs)
        return result

    return inner
