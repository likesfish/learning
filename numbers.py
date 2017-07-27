def fib(n):
    """Returns the nth number in the fibonacci sequence

    The fibonacci sequence is a series of numbers in which each number
    (Fibonacci number) is the sum of the two preceding numbers. The
    sequence begins with 1, 1, 2, 3, 5, 8, etc
    """
    x = 1
    y = 1
    for number in range(n-2):
        z = x + y
        print(z)
        x = y
        y = z
    return z

def minimum(numbers):
    lil = 999999

    for number in numbers:
        if number  < lil:
            lil = number

    return lil

def maximum(numbers):
    big = -999999

    for number in numbers:
        if number > big:
            big = number

    return big
