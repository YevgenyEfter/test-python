x = int (input())
y = int (input())

try:
	res = x / y
except ZeroDivisionError:
	res = 0
	print ("Can't divide by 0.")
else:
	print ("All good.")
finally:
	print ("This should always print.")

print (res)
