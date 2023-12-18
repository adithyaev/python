class Student:
    count = 0
    students = []
    def __init__(self,s_id,name,age,grade):
        self.s_id = s_id
        self.name = name
        self.age = age
        self.grade = grade
        Student.count = Student.count + 1
        Student.students.append(self)
    
    def display_student(self):
        print("student id: ",self.s_id)
        print("student name: ",self.name )
        print("student age: ",self.age)
        print("student grade: ",self.grade)
    
    def student_count(self):
        print("total number of student: %d" % Student.count)

    def view_students(self):
        print("student list")
        for student in Student.students:
            student.display_student()

studen1 = Student(1,"adithya",20,55)
# studen1.display_student()
# studen1.student_count()
    


def add_student():
    student_id = int(input("Enter the student id: "))
    student_name = input("Enter the student name: ")
    student_age = int(input("Enter the student age: "))
    student_grade = input("Enter the student grade: ")

    Student(student_id,student_name,student_age,student_grade)

    print(f"\nstudent with id {student_id} added succesfully ")

# add_student()
# studen1.view_students()

while True:
    print('\n options')
    print('1.add student')
    print('2.views student')
    print('3.exit')

    choises = input("enter your choise 1, 2 ,3 : ")
    if choises == '1':
        add_student()
    elif choises == '2':
        studen1.view_students()
    elif choises == '3':
        print('exiting the program')
        break
    else:
        print("invalid choise")

