def find_largest_element(arr):
    
    if not arr:
        return None  
    largest_element = arr[0]
    
    
    for element in arr:
        if element > largest_element:
            largest_element = element
    
    return largest_element

input_array = [23, 45, 67, 12, 89, 34, 56]


result = find_largest_element(input_array)
if result is not None:
    print("The largest element in the array is:", result)
else:
    print("The array is empty.")
