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

for name,age in zip(name_list,age_list):
   print(f"{name} is {age} years old.")


   
