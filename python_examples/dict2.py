student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}

# for name,grade in student_grades.items():
#     print(f"{name} : {grade}")


high_grades = {
    name : grade for name,grade in student_grades.items() if grade > 90
    }
print(high_grades)

high_grades = {
    # name : grade for name,grade in student_grades.items() if grade>80 and grade<90
    name : grade for name,grade in student_grades.items() if 80 <= grade <= 90
    }
print(high_grades)