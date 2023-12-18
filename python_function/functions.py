# function without parameters
def welcome():
    print('welcome')
# calling the function
welcome()

# function with parameters
def welcome_user(username):
    print(f"hello {username}")
# calling the function with argument
welcome_user('adithya')

# function with default parameter value
def greet_user(place,username = 'guest' ):
    print(f"hello {username} {place}")

# calling the function without passing an argument
# greet_user() # TypeError: greet_user() missing 1 required positional argument: 'place'
greet_user('kozhikode') # calling the function without passing an argument for username
greet_user('wayanad','dhaya') # calling the function with arguments for both place and username

# function with return value

def add(x,y):
    return x + y

result = add(1,5)
print(f"the sum is : {result}")

