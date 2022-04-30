def name(func):
    def _wrapper():
        print(func.__name__)
        return func()
    _wrapper.__name__ = func.__name__
    return _wrapper
