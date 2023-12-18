def find_common_elements(list1, list2):
   
    common_elements_method = list(set(list1).intersection(list2))
    
   
    common_elements_set = list(set(list1) & set(list2))
    
    return common_elements_method, common_elements_set


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]


result_method, result_set = find_common_elements(list1, list2)
print("Common elements using intersection method:", result_method)
print("Common elements using set intersection:", result_set)
