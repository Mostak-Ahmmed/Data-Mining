class stu:
    def __init__(self, s_name, marks):
        self.s_name = s_name
        self.marks = marks

student = stu('Mostak', 70)
print(f"Orginal - name: {student.s_name}, marks: {student.marks}")

student.s_name = 'Ahmmed'
student.marks = 80

print(f"Modified - name: {student.s_name}, marks: {student.marks}")