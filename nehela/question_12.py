class Employee:
    def __init__(self,name,emp_id,desgnation, salary):
        self.name = name
        self.emp_id= emp_id
        self.desgnation = desgnation
        self.salary = salary

    def salary_hike(self,perc):
        self.salary += self.salary * (perc /100)

    def promotion(self, new_desig, salary_hike_perc):
        self.desgnation = new_desig
        self.salary_hike(salary_hike_perc)

    def display_details(self):
        print("name" + self.name)
        print("Employee ID: " + str(self.emp_id))
        print("Designation: "+ str(self.desgnation))
        print("Monthly Salary: " + str(self.salary))


emp = Employee("Mahesh", 100, "P", 150)
emp.display_details()

emp.salary_hike(30)
emp.display_details()

