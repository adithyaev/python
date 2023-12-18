class A:
    def __init__(self):
        print("from parent")
    
    def display1(self):
        print("display1... ")
    
    def display2(self):
        print("display2... ")

class B(A):
    def __init__(self):
        super().__init__()
        print("from child")
    
    def display3(self):
        print("display3... ")
    
    def display4(self):
        print("display4... ")

obj1 = A()
# print(obj1)
# print(obj1.display1())

obj2 = B()
print(obj2)
print(obj2.display1())
print(obj2.display3())


    

