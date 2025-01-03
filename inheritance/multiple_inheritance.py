class college:
    def __init__(self, college_name, college_address):
        self.college_name = college_name
        self.college_address = college_address
    def display(self):
        print(f"College Name: {self.college_name}, College Address: {self.college_address}")

class teacher():
    def __init__(self, teacher_name, teacher_address):        
        self.teacher_name = teacher_name
        self.teacher_address = teacher_address
    def display(self):
        super().display()
        print(f"Teacher Name: {self.teacher_name}, Teacher Address: {self.teacher_address}")

class student( teacher, college):
    def __init__(self, college_name, college_address, teacher_name, teacher_address, student_name, student_address):
        college.__init__(self, college_name, college_address)
        teacher.__init__(self, teacher_name, teacher_address)
        self.student_name = student_name
        self.student_address = student_address
    def display(self):
        super().display()
        print(f"Student Name: {self.student_name}, Student Address: {self.student_address}")
        
obj = student('ABC College', 'ABC Address', 'XYZ Teacher', 'XYZ Address', 'John', 'John Address')
obj.display()