def student(name, age, department):
    
    student.args = ['name', 'age', 'department']
    print("Student Details:")
    print(f"Name: {name}, Age: {age}, Department: {department}")
    print("Function Arguments:", student.args)

student("Mostak", 24, "")
