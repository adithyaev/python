class Staff:
     def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        

class Teacher(Staff):
    def __init__(self, name, age, salary,subject):
        super().__init__(name, age, salary)
        self.subject = subject

teacher = Teacher('adithya',25,5000,'maths')
print(teacher.name)
print(teacher.age)
print(teacher.salary)
print(teacher.subject)
    

        
        
        