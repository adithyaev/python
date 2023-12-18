class A:
    def __init__(self):
        print("from class A")
    
    def display1(self):
        print("display1... ")
    
    def display2(self):
        print("display2... ")

class B:
    def __init__(self):
        print("from class B")
    
    def display3(self):
        print("display3... ")
    
    def display4(self):
        print("display4... ")

class C(B,A):
    def __init__(self):
        super().__init__()
        print("from class C")
    
    def display5(self):
        print("display5... ")
    
    def display6(self):
        print("display6... ")

obj1 = A()
# print(obj1)
# print(obj1.display1())

obj2 = B()
# print(obj2)
# print(obj2.display1())
# print(obj2.display3())

obj3 = C()
print(obj3)
print(obj3.display1())
print(obj3.display3())
print(obj3.display5())




    

