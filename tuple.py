a = (1, (1, 2, 3, 4))
print(a.__sizeof__())

b = [2, [1, 2, 3, 4]]
print(b.__sizeof__())

a2 = ()
a2 = tuple("Hello world!")
print(a2)

b2 = 1, 2, 3, 4
print(b2)

b3 = b2[2]
print(b3)

print(a.count(1))
