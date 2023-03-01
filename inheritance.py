"""Inheritance allows us to inherit attributes and methofs from a parent class
This is useful because we can create subclasses and get all the functionality of the parent class.
This also enables us to overwrite or add completely new functionality without affectiving the parent class in any way"""

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

"""We want to create types of employees: developers and managers. These can be good
candidates for subclasses. Developers and managers will have names, emails, etc.
These are all things Employee class already has. We can reuse the code from inheriting from Employee """
# When defining subclass, pass what class you want to inherit from
# If we want to pass in the developers main programming language as an attribute,
# take the init method from the class
class Developer(Employee):
    raise_amt = 1.10
# Let Employee class handle the other arguments using super().__init__ 
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # Employee.__init__(self, first, last, pay) also works
        self.prog_lang = prog_lang


"""Create another subclass called Manager
I'm also going to pass ina  list of employees the manager supervises"""
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# # By just passinging the Employee class into Developer subclass,
# # we return the information passed through Employee class
# dev_1 = Developer('Corey', 'Schafer', 50000)
# dev_2 = Developer('Test', 'User', 60000)
# print(dev_1.email)
# print(dev_2.email)
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# # to see the method resolution order
# # print(help(Developer))

# # If I changed the raise_amt in the subclass and run the Developer subclass versus Employee class, 
# # note the differences in the raise
# dev_1 = Developer('Corey', 'Schafer', 50000)
# print(dev_1.pay)
# dev_1.apply_raise()

# dev_1 = Employee('Corey', 'Schafer', 50000)
# dev_1.apply_raise()
# print(dev_1.pay)

"""Now that we have added prog_lang to the Developer subclass
The Developer class is going to expect prog_lang argument"""
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')
print(dev_1.email)
print(dev_1.prog_lang)

"""Run with manager subclasses"""
mgr_1 = Manager('Sue','Smith',90000,[dev_1])
print(mgr_1.email)
mgr_1.remove_emp(dev_1)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()


"""Python has built-in fuinctions call 'isinstance()' and 'issubclass()'"""
# isinstance() will tell us if an object is an instance of a class
print(isinstance(mgr_1,Manager)) # True
print(isinstance(mgr_1,Employee)) # True
print(isinstance(mgr_1,Developer)) # False

# issubclass() will tell us if a class is a subclass of another
print(issubclass(Developer,Employee)) # True
print(issubclass(Manager,Employee)) # True
print(issubclass(Manager,Developer)) # False
