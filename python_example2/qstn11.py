def find_second_largest(numbers):
   
    if len(numbers) < 2:
        return "List should have at least two elements"
    
   
    largest = second_largest = float('-inf')
    
   
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest


number_list = [12, 45, 67, 23, 89, 34, 56]

result = find_second_largest(number_list)
print("Second largest number in the list:", result)
