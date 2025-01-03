'''
write a program in python to implement a class student in which the class will have the following members: name, rollno, program, total_marks and subject_count. The class should have the following methods:

1. __init__(): This method should initialize the members of the class.
2. Computing average marks of the students.
3. Displaying the student details.
4. Create 3 student objects and print the average marks of the students.
5. Display the name of the student with the highest marks.
'''


class student:
    def __init__(self, name, rollno, program, total_marks, subject_count):
        self.name = name
        self.rollno = rollno
        self.program = program
        self.total_marks = total_marks
        self.subject_count = subject_count

    def avg_marks(self):
        return self.total_marks/self.subject_count

    def student_details(self):
        print("name: ", self.name)
        print("rollno: ", self.rollno)
        print("program: ", self.program)
        print("total_marks: ", self.total_marks)
        print("subject_count: ", self.subject_count)


def main():
    s1 = student("s1", 1, "Btech", 320, 4)
    s2 = student("s2", 2, "Btech", 225, 3)
    s3 = student("s3", 3, "Btech", 440, 5)

    if s1.total_marks > s2.total_marks and s1.total_marks > s3.total_marks:
        print("student with highest marks is: ", s1.name)
    elif s2.total_marks > s1.total_marks and s2.total_marks > s3.total_marks:
        print("student with highest marks is: ", s2.name)
    else:
        print("student with highest marks is: ", s3.name)

    print("average marks of s1: ", s1.avg_marks())
    print("average marks of s2: ", s2.avg_marks())
    print("average marks of s3: ", s3.avg_marks())
    s1.student_details()


if __name__ == '__main__':
    main()
