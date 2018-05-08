import datetime

class Employee:
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(first, last)

        Employee.num_of_employees += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string):
        first, last, pay = string.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False

        return True


emp_1 = Employee("A", "B", 50000)
emp_2 = Employee("C", "D", 60000)

#print(emp_1.fullname())
#print(Employee.fullname(emp_2))

#emp_1.apply_raise()

#print(emp_1.pay)
#print(emp_2.pay)

#emp_1.raise_amount += 1

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

Employee.set_raise_amount(1.05)

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

#print(Employee.num_of_employees)

emp_3 = Employee.from_string("E-N-90000")
print(emp_3.first)
print(emp_3.last)
print(emp_3.pay)

date_1 = datetime.date(2018, 5, 8)
date_2 = datetime.date(2018, 5, 12)
print(Employee.is_workday(date_1))
print(Employee.is_workday(date_2))
