name_list = []
age_list = []
id_list = []

for i in range(3):
   

   name = input(f" enter the name : {i+1} : ")
   age = input('enter the age : ')
   id = input('enter the id : ')
   name_list.append(name)
   age_list.append(age)
   id_list.append(id)

search_name = input('enter the name you want to search : ')

index = name_list.index(search_name)
print(f"{search_name} is {age_list[index]} year old and their id: {id_list[index]}")




   
