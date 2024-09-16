"""
This is a fibonacci sequence where it outputs the sequence in a list form and 
outputs the nth number of the sequence
"""
class NegativeNumError(Exception):
    pass

def generator(num):
    # Outputs a fibonacci sequence at n elements
    fib_array = [0, 1]
    for i in range(1, num):
        next_num = fib_array[i] + fib_array[i - 1]
        fib_array.append(next_num)
    fib_array.remove(0)
    return fib_array

def get_nth_num(num):
    # outputs the nth number of the fibonacci sequence
    sequence = generator(num)
    nth_num = sequence[num - 1]
    return f"F{num}: {nth_num}"

loop = True
while loop:
    # Added a try-except block to deal with exceptions
    try:
        number = int(input("Enter the length of the fibonacci sequence: "))
        if number < 0:
            raise NegativeNumError("Number can't be negative")
        fib = generator(number)
        print(f"Fibonacci sequence of {number} numbers: {fib}")
        print(f"F{number}: {fib[number - 1]}")
        loop = False
    except NegativeNumError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Enter a number!")
    
    






