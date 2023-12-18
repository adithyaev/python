def is_perfect_square(number):
   
    sqrt = int(number**0.5)
    return number == sqrt**2

input_number = int(input("Enter a number: "))


result = is_perfect_square(input_number)
if result:
    print(f"{input_number} is a perfect square.")
else:
    print(f"{input_number} is not a perfect square.")
