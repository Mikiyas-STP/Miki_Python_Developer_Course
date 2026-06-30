from functools import wraps

def deco(func):
    @wraps(func)
    def wrapper():
        return func()
    return wrapper

@deco
def test():
    """Hello"""
    pass

print(test.__name__)
print(test.__doc__)