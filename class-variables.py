"""Class variables are all variables that are shared amonst all instances of a class

"""

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

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

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# These are prints the same thing
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Print out namespace of emp_1, see now raise_amount:
# print(emp_1.__dict__)
# print(Employee.__dict__)

"""When we set the class variable Emplyee.raise_amount, the instance and class"""
# Employee.raise_amount = 1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

"""When we set the raise_amount for a specific instance emp_1 only, 
notice that everyone's raise amount stayed the same"""
emp_1.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

"""If these print statements were above where we instantiated emp_1 and emp_2, we'd print 0 here"""
print(Employee.num_of_emps)
