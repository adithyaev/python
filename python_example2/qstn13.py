def find_intersection(array1, array2):
   
    intersection_set = set(array1).intersection(array2)
    

    intersection_list = list(intersection_set)
    
    return intersection_list


array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]

result = find_intersection(array1, array2)
print("Intersection of the arrays:", result)
