from mydecorators import my_decorator
from mydecorators import do_twice
from mydecorators import do_twice_with_any_args

def say_hello():
    print("hello!")
    
    
# say_hello = my_decorator(say_hello)
# say_hello()

#@my_decorator

#@do_twice

# def say_wohoo():
#     print("wohoo")

# say_wohoo()

# @do_twice

# def say_whee():
#     print("whee")
    
@do_twice_with_any_args

def say_something(*args , **kwargs):
    for idx in args:
        print(idx)
        
    for key in kwargs.keys():
        print(key)
        
say_something(1, 2, 3, {"a":2, "b":3, "c":4})
    






