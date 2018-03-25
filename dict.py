d = {"test": 1, "test2": 2}
print(d)
print(d["test"])
print(d["test2"])

d2 = dict(short="dict", longer="dictionary")
print(d2)

d3 = dict([("key1", "val1"), ("key2", "val2")])
print(d3)

d4 = dict.fromkeys(["a", "b", "c"], 1)
print(d4)

d5 = {a: a ** 2 for a in range(7)}
print(d5)

for key, value in d5.items():
	print(key, value)

d5.clear()
print(d5)

print(d3.items())

a = d.setdefault("test3", 5)
print(d)
print(a)

del d["test2"]
print(d)

b = d.pop("test3")
print(d)
print(b)
