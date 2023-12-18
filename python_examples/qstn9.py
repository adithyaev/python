# Given boolean variables is_sunny = True and is_warm = False, write
# expressions to check if:
# a. It is sunny and warm
# b. It is either sunny or warm
# c. It is not warm

is_sunny = True
is_warm = False

a = is_sunny and is_warm
print('it is sunny and warm : ',a)

b = is_sunny or is_warm
print(' It is either sunny or warm : ',b)

c = not is_warm
print('It is not warm : ',c)

