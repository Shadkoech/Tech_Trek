# Fibonacci numbers module

def fib(n): # write a Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b # same as (a = b) and (b = a+b)
    print()  # This is how to print a new line in the output to go to another fxn

def fib2(n):  # return Fibonacci series up to n
    result = []  # Empty list named result is initialized. It shall store the numbers in the Fibonacci series
    a, b = 0, 1  # initializes a and b that rep initial numbers in the Fibonacci series
    while a < n:
        result.append(a)  # stores value of a each cycle into the result list
        a, b = b, a+b
    return result

