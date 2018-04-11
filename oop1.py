class Person:
	name = "Eugene"
	age = 32

	def getDetails(self):
		return self.name + " " + str(self.age)

p = Person()
p.name = "Eugene Efter"
print (p.name)
p.lastName = "Efter"
print (p.lastName)

print(p.getDetails())
