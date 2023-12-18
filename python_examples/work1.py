list_guest = []


for i in range(3):
    name = input("enter the guest names : ")
    list_guest.append(name)
while True:
   add_more = input('Do you want to add another person?(yes/no) : ').lower()

   if add_more == 'yes':
      name = input('enter another person name : ')
      list_guest.append(name)
   elif add_more == 'no':
      break
   else:
      print("please enter Yes/No")

print( 'invited guest names : ')
for guest in list_guest:
  print(guest)
