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

# Example 
@timer
def example():
    time.sleep(2)

example()

"""
Timing for how long selection sort takes
"""
def create_array(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]

@timer
def selection_sort(a=create_array()):
    sort_len = 0 
    while sort_len < len(a):
        min_idx = None
        for i, elem in enumerate(a[sort_len:]):
            if min_idx == None or elem < a[min_idx]:
                min_idx = i + sort_len
        a[sort_len], a[min_idx] = a[min_idx], a[sort_len]
        sort_len += 1
    return a

a = create_array()
print(f"Unsorted: {a}")
a = selection_sort(a)
print(f"sorted: {a}")
