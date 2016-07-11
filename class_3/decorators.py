
class Calculator(object):
    def add(self, a, b):
        self._check_params(a, b)
        print(a + b)


class only_int_arguments(object):
    def __init__(self, allow_floats=False):
        self.allow_floats = allow_floats

    def __call__(self, f):
        def new_f(a, b):
            if type(a) != int or type(b) != int:
                raise ValueError("Only int arguments!")
            f(a, b)
        return new_f


@only_int_arguments(allow_floats=True)
def add(a, b):
    print(a + b)

add("hello", "world")
