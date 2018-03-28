def func(a = 6, b = 3):
	"This function adds 2 numbers."
	return a + b

print (func(1))

def func2(*tuple):
	for a in tuple:
		print (a)

func2(1, 2, 3, 4)

def func3(**dict):
	for a, b in dict.items():
		print (a, b)

func3(a = 1, b = 2, c = 3, d = 4)

add = lambda x, y: x + y
print (add(1,2))
