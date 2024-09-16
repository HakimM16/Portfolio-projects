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

loop = True
while loop:
    try:
        number = int(input("Enter the length of the fibonacci sequence: "))
        fib = generator(number)
        print(f"Fibonacci equence of length {number}: {fib}")
        print(f"F{number}: {fib[number - 1]}")
        loop = False
    except ValueError:
        print("Enter a number!")
    
    






