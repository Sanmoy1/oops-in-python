class Student:
    def __init__(self, name, roll_no, program, total_marks, num_subjects):
        self.name = name
        self.roll_no = roll_no
        self.program = program
        self.total_marks = total_marks
        self.num_subjects = num_subjects

    def compute_average(self):
        return self.total_marks / self.num_subjects

    def display_info(self):
        print("Name: " + str(self.name))
        print("Roll No: " + str(self.roll_no))
        print("Program: " + str(self.program))
        print("Total Marks: " + str(self.total_marks))
        print("Number of Subjects: " + str(self.num_subjects))
        print("Average Marks: " + str(self.compute_average()))

    def get_total_marks(self):
        return self.total_marks


ob1 = Student("demo", 12, "btech", 290, 3)
ob2 = Student("demo2", 2, "btech", 285, 3)
ob3 = Student("demo3", 3, "btech", 270, 3)

print(ob1.compute_average())
print(ob2.compute_average())
print(ob3.compute_average())

if (ob3.get_total_marks() > ob2.get_total_marks()):
    if (ob3.get_total_marks() > ob1.get_total_marks()):
        print("Student 3 has highest marks")
    else:
        print("Student 1 has highest marks")
else:
    if (ob2.get_total_marks() > ob1.get_total_marks()):
        print("Student 2 has highest marks")
    else:
        print("Student 1 has highest marks")
