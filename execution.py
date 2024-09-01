def timer(func):
    from time import time

    t1 = time()
    func
    t2 = time()

    diff = t2 - t1
    print(f"Time taken for {func.__name__}: {diff}s")


@timer
def prime(num):
    list = []
    for i in range(1, num + 1):
        if num % i == 0:
            list.append(i)
    return list