def count_vowels(input_str):
    # Define a set of vowels
    vowels = set("aeiouAEIOU")
    
   
    vowel_count = 0
    
   
    for char in input_str:
        
        if char in vowels:
            vowel_count += 1

    return vowel_count


input_string = "Hello, World!"


result = count_vowels(input_string)
print("Number of vowels in the string:", result)
