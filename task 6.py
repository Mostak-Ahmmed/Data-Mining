class Std:
    def __init__(self, stdID, stdName):
        self.stdID = stdID
        self.stdName = stdName
        self.stdClass = None

    def display_attributes(self):
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

student = Std(213902126, 'Mostak')
student.stdClass = 'Bsc. in CSE'
print(student.__dict__)
