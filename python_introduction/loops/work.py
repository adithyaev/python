# Create a program that prints the Fibonacci sequence up to a specified number n.
#  The Fibonacci sequence is a series of numbers 
# where each number is the sum of the two preceding ones, usually starting with 0 and 1.


# n = 0
# while n>=0:
#     print(n)
#     n = n+1

# def add(a,b):
#     return a+b
# num1 = int(input('enter number1 : '))
# num2 = int(input('enter number2 : '))
# result = add(num1,num2)
# print(result)
# print(f"sum of {num1} and {num2} is {result}")


def fibonacci(n):
    fibonacci_series = []
    n1,n2 = 0,1

    while n1 <= n:
        fibonacci_series.append(n1)
        n1,n2 = n2,n1 + n2
    return fibonacci_series

n = int(input('enter a limit : '))
fibonacci_series = fibonacci(n)
print(fibonacci_series)