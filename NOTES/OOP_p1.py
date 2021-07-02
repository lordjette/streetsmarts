

class Employee():
    def __init__(self, firstname, lastname, pay):
        self.first = firstname
        self.last = lastname
        self.payload = pay
        self.email = firstname + '.' + lastname + '@company.com'

    def fullname(self):
        return '{} {} {} {}'.format(self.first, self.last, self.payload, self.email)

emp_1 = Employee('Lordjette', 'Lecaros', 50000)
emp_2 = Employee('Sabrina', 'Morningstar', 12000)

print(Employee.fullname(emp_1))
print(emp_1.fullname())