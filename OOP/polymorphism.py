import math
num1 = 10
num2 = 5
sum = num1 + num2
# print(sum)
fname = 'adithya'
lname = 'ev'
# print(f"{fname} {lname}")
# print(fname + '' + lname)

cources = ['python','react','flutter','javascript','angular']

user_data = {
    'name' : 'adithya',
    'email' : 'adithya@gmail.com',
    'contact' : '9876546756'
}

# print(len(user_data))
# print(len(fname))
# print(len(cources))

class Polygon:
    def render(self):
        print("rendering a polygon")

    def calculate_area(self):
        pass

class Square(Polygon):
    def __init__(self,side_length):
        self.side_length = side_length

    def render(self):
        print('rendering a square')
    
    def calculate_area(self):
        area = self.side_length ** 2
        print(f"area of square is {area} units")

class Circle(Polygon):
    def __init__(self,radius):
        self.radius = radius

    def render(self):
        print('rendering a circle')
    
    def calculate_area(self):
        area = math.pi * self.radius ** 2
        print(f"area of circle is {area : .2F} units") 

square1 = Square(4)
square1.render()
square1.calculate_area()

circle1 = Circle(4)
circle1.render()
circle1.calculate_area()


