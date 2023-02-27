# """ Early example of Class
# Here, we are defining each instance individually
# This is very manual and can introduce types
# See below for an example of how to automatically create each instance"""

# class Employee:
#     pass

# # At this point, class without attributes or methods
# # Each of these are unique instances of Employee class
# emp_1 = Employee()
# emp_2 = Employee()

# print(emp_1)
# print(emp_2)

# # Each instance has attributes that are unique to them
# emp_1.first = 'Corey'
# emp_1.last = 'Schager'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000

# print(emp_1.email)
# print(emp_2.email)



"""
How to programmatically have the class build each instance as opposed to defining 
the variables (first,last,pay,email) each time
first, last, pay, and email are attributes of the class Employee
"""
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    # Each method within a class automatically takes the instance as the first argument
    def fullname(self):
        return f"{self.first},{self.last}"


# Now when we create our isntances of employee class, we can pass in values speicfied in the init method
# init method takes the instance which we call self, first, last, and pay as arguments
# When we create employee, the instance is passed automatically, so we can leave out self

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
print(emp_1.email)
print(emp_2.email)

# Let's say you want the ability to display full name for employee
# You COULD print a concat of each employees first and last name
# Instead, you can also add this as a new function in the Employee class
# print(f"{emp_1.first},{emp_1.last}")

# After adding fullname() to Employee class, you can print the full name by calling the function
# The {} insteads method, without it, Python will think you're calling an attribute
print(emp_1.fullname())
# You can also call a class methods using class name
print(Employee.fullname(emp_1))
"""The two above statements do the same thing.
emp_1.fullname() is an instance, don't need self passed in.
When we call method on call, it does not know which isntance we want to run the method with;
so we HAVE to pass in the instance (self)"""