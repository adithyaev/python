invite_people = []

def display_manage_list():
    print('list of invited people : ')
    
    for i in range(len(invite_people)):
          print(f"{i+1} : {invite_people[i]}")

    choose_name = input('choose a name from the list (or type "done" to finish ): ')
    if choose_name.lower() == 'done':
            return False
    if choose_name in invite_people:
            position = invite_people.index(choose_name) + 1
            print(f"{choose_name} is at position {position} in the list")
            response = input(f"do you still want  {choose_name} to attend the partty? (yes/no) : ")
            if response.lower() == 'no':
                invite_people.remove(choose_name)
                print(f"{choose_name} has remove from the list")
    else:
            print(f"{choose_name} is not in the list")
    return True

while True:
    name = input('enter the name of person : ')
    invite_people.append(name)
    if not display_manage_list():
        break 

print(invite_people)



# for i in range(3):
#     name = input('enter the name of person : ')
#     invite_people.append(name)
    
# print(invite_people)
# while True:
#     response = input('do you want to add another person? (yes/no) : ')
#     if response.lower() == 'yes' :
#         name = input('enter the name of another person : ')
#         invite_people.append(name)
#     else:
#         break
#     num_invited = len(invite_people)
#     print(f"you have invited {num_invited} peoples to the party")




