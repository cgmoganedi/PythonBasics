class CannotInit(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Cannot instantiate")
