import datetime


class Employee:
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.raise_amount = 1.30

        Employee.num_of_employees += 1

    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print ("Delete name")
        self.first = None
        self.last = None

    def __repr__(self):
        return "Employee('{}', '{}, '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string):
        first, last, pay = string.split("-")
        return cls(first, last, pay)

    @classmethod
    def print_something(cls):
        print("From class Employee")

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False

        return True

    def print_something(self):
        print("From class Employee self")

    @staticmethod
    def print_static():
        print("Static from Employee")
        return "a"

    # def print_static(self):
    #     print("Static from Employee self")
    #     return "b"


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        #self.raise_amount = 1.20
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(first, last)

    def fullname(self):
        return super().fullname()

    @classmethod
    def print_something(cls):
        print("From class Developer")

    def print_something(self):
        print("From class Developer self")

    # @staticmethod
    # def print_static():
    #     print("Static from Developer")
    #     return "a"

    # def print_static(self):
    #     print("Static from Developer self")
    #     return "b"


emp_1 = Employee("A", "B", 50000)
emp_2 = Employee("C", "D", 60000)

# print(emp_1.fullname())
# print(Employee.fullname(emp_2))

# emp_1.apply_raise()

# print(emp_1.pay)
# print(emp_2.pay)

# emp_1.raise_amount += 1

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)
#
# Employee.set_raise_amount(1.05)
#
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)
#
# print(Employee.num_of_employees)
#
# emp_3 = Employee.from_string("E-N-90000")
# print(emp_3.first)
# print(emp_3.last)
# print(emp_3.pay)
#
# date_1 = datetime.date(2018, 5, 8)
# date_2 = datetime.date(2018, 5, 12)
# print(Employee.is_workday(date_1))
# print(Employee.is_workday(date_2))

# dev_1 = Developer("Aaa", "Bbb", "1111", "java")
# print(dev_1.raise_amount)
#
# dev_1.print_something()
# dev_1.print_static()
#
# print(isinstance(dev_1, Developer))
# print(issubclass(Developer, Employee))
#
# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))

print(emp_1.email)
emp_1.fullname = "A1 B1"
del emp_1.fullname
print(emp_1.email)
