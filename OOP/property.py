class EmployeeBad:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@gmail.com'
        self.fullname = first_name + ' ' + last_name


class EmployeeGood:
    """
    using the property decorator its possible to dynamically change other instance attributes when
    an instance attribute is changed. If the attribute is in the constructor it will need to be protected otherwise
    the programme will go into a recursive loop trying to update the attribute that's being set (don't have that issue
    here see: https://docs.python.org/3/library/functions.html#property for more details).

    @property decorator allows for methods to be called like attributes, note how it doesn't actually set the value
    as a new instance attribute.
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return self.first_name + '.' + self.last_name + '@gmail.com'

    @property
    def fullname(self):
        return self.first_name + ' ' + self.last_name

    @fullname.setter
    def fullname(self, value):
        first, last = value.split(' ')
        self.first_name = first
        self.last_name = last


a = EmployeeBad('john', 'doe')
a.fullname = 'ray santiago'
print(a.first_name)
print(a.last_name)
print(a.email)
print(a.fullname, '\n')
# didn't update the first name, last name, or email! bad design for usage

b = EmployeeGood('jane', 'doe')
b.fullname = 'ray santiago'
print(b.first_name)
print(b.last_name)
print(b.email)
print(b.fullname)
# does update the attributes!

"""
output:
john
doe
john.doe@gmail.com
ray santiago 

ray
santiago
ray.santiago@gmail.com
ray santiago
"""