def calculate_factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
       
        return n * calculate_factorial(n - 1)


user_input = int(input("Enter a non-negative integer to calculate its factorial: "))


if user_input < 0:
    print("Please enter a non-negative integer.")
else:
    
    result = calculate_factorial(user_input)
    print(f"The factorial of {user_input} is: {result}")
