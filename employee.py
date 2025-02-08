class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def calculate_paycheck(self): # Calculate Weekly paycheck, yearly / 52 weeks per year
        return self.salary/52