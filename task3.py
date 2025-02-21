class Student:
    def __init__(self):
        pass
    def fun1(self):
        print('Student class')

class Marks:
    def __init__(self):
        pass
    def fun2(self):
        print('Marks class')


e1 = Student()
e2 = Marks()

e1.fun1()
e2.fun2()

print(isinstance(e1, Student))  
print(isinstance(e2, Marks))    

print(issubclass(Student, object))  
print(issubclass(Marks, object))    
