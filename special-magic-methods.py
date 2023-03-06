"""Special magics enable us to emulate some built-in behavior within Python;
It's also how we implement operator overloading
"""
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
        self.pay = int(self.pay * self.raise_amt) #Employee.raise_amount works as well
# To print out something in the backend for developers
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last,self.pay)
# To print out something for the end users/consumers
    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)
    
    def __add__(self, other): #self = left and other = right side of the addition
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())



emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
# When we print out emp instance, we get a vague employee object
# We could change the behavior to print out something more understandable
# Note when we added the __repr__ method, the instance prints out something more readable
print(emp_1) #<__main__.Employee object at 0x00000242EA883FD0> vs. Employee('Corey','Schafer','50000')


# These print the exact same objects for repr and str respectively
print(repr(emp_1))
print(str(emp_1))
print(emp_1.__repr__())
print(emp_1.__str__())

# The addition has different behavior depending on the object you're working with
print(1+2)
print(int.__add__(1,2))
print('a'+'b')
print(str.__add__('a','b'))

"""Before adding the __add__() function in the Employee class"""
# TypeError: unsupported operand type(s) for +: 'Employee' and 'Employee'
# print(emp_1+emp_2)

"""After adding the __add__() function in the Employee class"""
print(emp_1+emp_2)

"""len is also a special method"""
print(len('test'))
print('test'.__len__())

"""Run this len on emp_1 before adding the __len__() function"""
# TypeError: object of type 'Employee' has no len()
# print(len(emp_1)) 

"""Run this len on emp_1 after adding the __len__() function"""
print(len(emp_1)) 