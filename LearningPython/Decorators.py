
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




def decorator_with_parameters(password):
    def a_decorator(func):
        @functools.wraps(func)
        def function_wrapper():
            if password == "ciao":
                func()
                print("OK - Permission granted")
            else:
                print("Invalid Password")
        return function_wrapper
    return a_decorator




@decorator_with_parameters("ciao")
def my_admin_function():
    print("I want to change important things")


my_admin_function()


