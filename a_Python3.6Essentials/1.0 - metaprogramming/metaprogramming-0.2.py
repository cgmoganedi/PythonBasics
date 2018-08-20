from functools import wraps

#function decorator

def function_name(func):
    message = func.__qualname__

    @wraps(func)
    def wrapper(*args, **kwargs):
                print(message)
                return func(*args, **kwargs)
    return wrapper

#using your own decorator

@function_name
def adder(x,y):
    return x + y

print (adder(2,3))
