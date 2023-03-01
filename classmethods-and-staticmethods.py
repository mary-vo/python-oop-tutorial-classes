class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1

    # Each method within a class automatically takes the instance as the first argument
    def fullname(self):
        return f"{self.first},{self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #Employee.raise_amount works as well

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    """Static methods do not pass anything automatically (instance or class); they behave like regular functions
    but they're included int he class because thye have some logical connection to the class"""
    # Function that would take in a date and return whether or not that is a weekday    
    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

"""Regular methods automatically takes the first instance the argument (self)
How can we change the above class so it takes the class as the first argument?
Include @classmethod before defining the function inside the Class"""
# Class raise_amt
print(Employee.raise_amt)
# Instance raise_amt
print(emp_1.raise_amt)
print(emp_2.raise_amt)


# If we want to change this to 5%
# Employee.set_raise_amt(1.05)
# # Class raise_amt
# print(Employee.raise_amt)
# # Instance raise_amt
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)


"""This is the same as the above, but instead above, I am use a class method """
Employee.raise_amt = 1.05
print(Employee.raise_amt)
# Instance raise_amt
print(emp_1.raise_amt)
print(emp_2.raise_amt)

"""Peopl can typically use class methods as alternative contrsuctors;
Use the class methods to provide multiple wayys of creating an object
Exmaple: someone using employee class, but they get a string separated by hypens
and they need to parse stiring before creating new employees. They want to pass
the string in to have an employee created"""
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
# print(new_emp_1.email)
# print(new_emp_1.pay)

"""If someone is using the class this way, it may make sense to include logic to solve this issue
Add a new class method into Employee class
Instead of using the split method above, they can do this now:
"""
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

"""Static methods do not pass anything automatically (instance or class); they behave like regular functions
but they're included int he class because thye have some logical connection to the class"""
# Function that would take in a date and return whether or not that is a weekday
import datetime 
my_date = datetime.date(2016,7,10)
print(Employee.is_weekday(my_date))