def calculate_factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2,n+1):
        factorial *= i
    return factorial

limit = 3
result = calculate_factorial(limit)

if result is not None:
    print(f"factorial of {limit} is {result}")
else:
    print('factorial is not defined for negative numbers')

# return factorial,n
# result,number = calculate_factorial(5)

# if result is not None:
#     print(f"factorial of {number} is {result}")
# else:
#     print('factorial is not defined for negative numbers')
