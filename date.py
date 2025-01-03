'''
Implement a date class. wrie a member functions to initialize an object of the class for the following:
1. day to 1, month to 1, year to 1970
2. day to user input, month to 1, year to 1970
3. day to user input, month to user input, year to 1970
4. day to user input, month to user input, year to user input
5. getting the previous day
6. getting the next day
7. printing the day in the format dd/mm/yyyy
8. create a object of the class and then display the next and previous day.
'''
class date:
    def __init__(self,day=1,month=1,year=1970):
        self.day=day
        self.month=month
        self.year=year
        
    def next_day(self):
        self.day+=1
        if self.day>30:
            self.day=1
            self.month+=1
        if self.month>12:
            self.month=1
            self.year+=1
            
    def prev_day(self):
        self.day-=1
        if self.day<1:
            self.day=30
            self.month-=1
        if self.month<1:
            self.month=12
            self.year-=1
            
    def print_date(self):
        print(f'{self.day}/{self.month}/{self.year}')
obj=date(30,12,2020)
obj.next_day()
obj.print_date()
obj.prev_day()
obj.print_date() 
