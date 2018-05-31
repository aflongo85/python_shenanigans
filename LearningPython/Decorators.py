
import functools

def my_first_decorator(func):

    @functools.wraps(func)
    def function_that_wraps():
        print("Starting decorating")
        func()
        print("Finishing decorating")

    return function_that_wraps



@my_first_decorator
def func_to_be_decorated():
    print("HERE WE GO")


func_to_be_decorated()