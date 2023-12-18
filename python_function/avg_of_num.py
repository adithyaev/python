def calculate_avg(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    length = len(numbers)
    average = total/length
    return average

number_list = [2,4,3]
result = calculate_avg(number_list)

if result is not None:
    print(f"average is : {result}")
else:
    print('list is empty')
