class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def getDetails(self):
		return self.name + " " + str(self.age)
	
	def setDetails(self, name, age):
		self.name = name
		self.age = age

class Student(Person):
	course = 1

	def __init__(self, name, age, course):
		super(Student, self).__init__(name, age)
		self.course = course

	def setDetails(self, name, age, course):
		super(Student, self).setDetails(name, age)
		self.course = course

	def getDetails(self):
		return self.name + " " + str(self.age) + " " + str(self.course)

st1 = Student("Eugene", "32", 5)
print (st1.getDetails())
st1.setDetails("Yevgeny", 18, 2)
print (st1.getDetails())
