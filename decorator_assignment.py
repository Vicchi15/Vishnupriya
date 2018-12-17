import inspect

def dump_args(func):
    """Decorator to print function call details - parameters names and effective values.
    """
    def wrapper(*args, **kwargs):
        func_args = inspect.signature(func).bind(*args, **kwargs).arguments
        func_args_str =  ','.join('{} = {}'.format(*item) for item in func_args.items())
        print(func_args_str)
        return func(*args, **kwargs)
    return wrapper

@dump_args
def test(a, b=1, c=2, *args, **kwargs):
    pass

test(1)
test(1, 3, 8, 9)
test(1, d=5)
test(1, 2, 3, 4, 5, d=6, g=12.9, e=20)
