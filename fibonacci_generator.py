def generator(num):
    # Outputs a fibonacci sequence at n elements
    fib_array = [0, 1]
    for i in range(1, num):
        next_num = fib_array[i] + fib_array[i - 1]
        fib_array.append(next_num)
    fib_array.remove(0)
    return fib_array


def get_nth_num(num):
    sequence = generator(num)
    nth_num = sequence[num - 1]
    return f"F{num}: {nth_num}"

print(get_nth_num(0))


