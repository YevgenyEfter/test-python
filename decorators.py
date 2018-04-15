def decorator(func):
	def wrapper(arg):
		print("Before func.")
		func(arg)
		print("After func.")

	return wrapper

@decorator
def show(line):
	print(line)

show("Decorator function")

#dec = decorator(show)

#dec("Decorator function")
