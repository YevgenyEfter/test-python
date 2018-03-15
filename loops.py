print("while:")

i = 0
while i < 5:
	print(i)
	i += 1

print("for:")

numbers = [1,2,3]
for number in numbers:
	print(number)

print("for with range:")

for i in range(5):
	print(i)

print("break:")

for i in range(10):
	if i == 7:
		break
	print(i)

print("continue:")

for i in range(10):
	if i == 7:
		continue
	print(i)

print("else:")

for i in range(5):
	if i == 2:
		continue
	print(i)
else:
	print("Finished for else loop.")

print("else with break:")

for i in range(5):
	if i == 2:
		break
	print(i)
else:
	print("Finished for else loop.")
