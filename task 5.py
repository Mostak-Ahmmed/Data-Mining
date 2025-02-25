class Student:
    def __init__(self, studentId, studentName):
        self.studentId = studentId
        self.studentName = studentName

s = Student(213902126, 'Mostak')

s.studentClass = "BSc in CSE"

print(s.__dict__)

del s.studentName

print(s.__dict__)
