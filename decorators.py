def name(func):
    def _wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    _wrapper.__name__ = func.__name__
    return _wrapper
