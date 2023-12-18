invite_people = []
for i in range(3):
    name = input('enter the name of perso : ')
    invite_people.append(name)
    
print(invite_people)
while True:
    response = input('do you want to add another person? (yes/no) : ')
    if response.lower() == 'yes' :
        name = input('enter the name of another person : ')
        invite_people.append(name)
    else:
        break
num_invited = len(invite_people)
print(f"you have invited {num_invited} peoples to the party")


