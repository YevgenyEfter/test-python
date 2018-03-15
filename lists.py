lst1 = []
lst1.append(1)
lst1.append(2)
lst1.append(3)

print(lst1[0])
print(lst1[1])
print(lst1[2])

for x in lst1:
	print(x)

l = [1, 2, "x", 2.34, ["a", "b"], "e"]
print(l)

l2 = [x for x in "abcd"]
print(l2)

l2.extend(l)
print(l2)

l2.insert(1, "e")
print(l2)

l2.remove("e")
print(l2)

x = l2.pop()
print(l2)
print(x)

x = l2.pop(1)
print(l2)
print(x)

y = l2.index(1)
print(y)

cnt = l2.count("a")
print(cnt)

lst3 = ["d", "a", "b", "i", "c"]
lst3.sort()
print(lst3)

lst3.reverse()
print(lst3)

lst3.clear()
print(lst3)
