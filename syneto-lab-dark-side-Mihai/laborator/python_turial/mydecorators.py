def my_decorator(func):
    def wrapper():
        print("somethon is happening before the function is called")
        func()
        print("somthing is happening after the function is called") 
    return wrapper


def do_twice(func):
    def wraper_do_twice():
        func()
        func()
    return wraper_do_twice()

def do_twice_with_any_args(func):
    def wraper_do_twice_args(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wraper_do_twice_args
        
        