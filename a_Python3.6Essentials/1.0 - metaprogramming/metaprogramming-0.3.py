#using singleton design patterns in python

class my_counter(metaclass=Singleton):
    pass
# or you can do this inside the class

class my_counter():
    __metaclass__ = Singleton
    pass
