class MyException(Exception):
	pass

a = int(input("Type a number"))

if a == 0:
	raise Exception("Can't type 0!")

if a == 1:
	raise Exception

if a == 2:
	raise ValueError("No 2")

if a == 3:
	raise MyException("My Exception with message.")
