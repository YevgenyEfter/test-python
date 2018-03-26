#a = {"a", "b", "c", "a", "d"}
#a = {i ** 2 for i in range(10)}
"""a = set("Hello")
a.add(1)
b = frozenset("Hello")
print(type(a))
print(a)

print(type(b))
print(b)

a1 = ["H", "e", "l", "l", "o"]
a2 = set(a1)
print(a1)
print(a2)"""

a = {1, 2, 3, 4}
#x = 2
x = {1, 6, 7}
#print (x in a)
#print(a.isdisjoint(x))
#print(a == x)
#a.update(x)
#a.intersection_update(x)
a.symmetric_difference_update(x)
print(a)

#a.remove(3)
#print(a)

#a.discard(6)
#print(a)

#a.discard(8)
#print(a)

b = a.pop()
print(a)
print(b)

a.clear()
print(a)
