# *args - positional arguments
def args_func(*args):
    for i, arg in enumerate(args, start=1):
        print(i, arg)


args_func('a', 'b', 'c', 'd', 'e')


# **kwargs - keyword/keyvalue arguments
def kwargs_func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


kwargs_func(name="Jan", age=21, sex="Male", nickname="Jed")
