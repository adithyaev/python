def is_palindrome(input_str):
   
    cleaned_str = ''.join(input_str.split()).lower()
    
   
    return cleaned_str == cleaned_str[::-1]


input_string = "A man a plan a canal Panama"


result = is_palindrome(input_string)
if result:
    print(f'The string "{input_string}" is a palindrome.')
else:
    print(f'The string "{input_string}" is not a palindrome.')
