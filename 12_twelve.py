#Q1 Problem: Write a decorator that measures the time a function takes to execute.
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"{func.__name__} ran in {round((end - start), 4) } time")
        return result
    return wrapper

@timer
def exampleOne(z):
    time.sleep(z)

exampleOne(3)

#Q2 Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@debug
def exampleTwo(name,  greeting="Namaste"):
    print(f"{greeting} {name} !")


exampleTwo("Atul", "Hello")

#Q3 Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
def cache(func):
    cache_valus = {}
    print(cache_valus)
    def wrapper(*args, **kwargs):
        if args in cache_valus:
            return cache_valus[args]
        result = func(*args)
        cache_valus[args] = result
        return result
    return wrapper
@cache
def exampleThree(a, b):
    time.sleep(2)
    my_result = a + b
    return my_result

print(exampleThree(2,3))
print(exampleThree(2,3))


