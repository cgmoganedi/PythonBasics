# using a Signature

def my_func(*args, **kwargs):
    bound_values = my_sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)
