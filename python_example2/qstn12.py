def sum_of_digits(number):
    # Convert the number to a string to iterate through its digits
    str_number = str(number)
  
    digit_sum = 0
    
    for digit_str in str_number:
        digit_sum += int(digit_str)
    
    return digit_sum

input_number = int(input("Enter an integer: "))

result = sum_of_digits(input_number)
print(f"The sum of digits in {input_number} is: {result}")
