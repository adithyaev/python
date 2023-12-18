def reverse_string(input_str):
    
    if len(input_str) <= 1:
        return input_str
    else:
        
        return reverse_string(input_str[1:]) + input_str[0]


input_string = "Hello, World!"

result = reverse_string(input_string)
print("Original string:", input_string)
print("Reversed string:", result)
