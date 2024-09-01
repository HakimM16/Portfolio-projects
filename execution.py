"""
This timer function calculates the the time taken for a function to run
"""
import time

def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        function = func(*args, **kwargs)
        t2 = time.time()
        diff = t2 - t1
        print(f"Time taken for {func.__name__}: {diff:.4f}s")
        return function
    return wrapper


@timer
def example():
    time.sleep(2)

example()
