# 1. Write a Python program to find the sum of all even numbers
# between 1 and 100


def sum_of_even_numbers():
    
    even_sum = 0
    for num in range(1,101):
        
        if num % 2 == 0:
            
            even_sum += num
    return even_sum

result = sum_of_even_numbers()
print(f"sum of even number : {result}")

  

