class Date:
    def __init__(self,day=1,month=1,year=1970):
        self.day = day
        self.month = month
        self.year = year

    def leap_year(self):
        return (self.year%4 == 0 and self.year% 100 != 0) or (self.year % 400 == 0)
    
    def days_month(self):
        if self.month in [4,6,9,11]:
            return 30
        elif self.month == 2:
            return 29 if self.leap_year() else 28
        else:
            return 31
    
    def next_day(self):
        # day= 31, month = 12, year = 2000
        self.day +=1 #31+1 =32

        if self.day>self.days_month(): #32>31
            self.day=1 #day= 1
            self.month +=1 #13

            if self.month>12: #13>12
                self.month =1 #1
                self.year +=1 #year = 2001

    def previous_day(self):
        # day = 1, month = 1, year 2001
        self.day -=1 # 1-1=0
        
        if self.day<1: #0<1
            self.month-=1 #1-1 =0
            if self.month <1: #0<1
                self.month = 12
                self.year -=1
                self.day = 31
        
            
    def print_date(self):
        print(f"{self.day}/{self.month}/{self.year}")

date1 = Date()
date1.print_date()

date2 = Date(10)
date2.print_date()

date3 = Date(10,9)
date3.print_date()

date4 = Date(1,1,2015)
date4.print_date()

date4.previous_day()
date4.print_date()

date4.next_day()
date4.print_date()