class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # the property decorator enables us to continue to use email
    # as an attribute instead of calling it like a method (i.e. email())
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"
    
    # Each method within a class automatically takes the instance as the first argument
    @property
    def fullname(self):
        return f"{self.first},{self.last}"
    
    @fullname.setter
    def fullname(self, name):
        first,last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    

emp_1 = Employee('John','Smith')
# emp_1.first = 'Jim'

emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname