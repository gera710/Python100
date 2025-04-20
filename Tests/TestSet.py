x = {}
s = {1,32,1,4}
print(type(x), type(s))
print(s)
print(4 in s)
print(4 not in s)

x = {"key":4,
     2:4}
x[5] = "hello"
x["hello"] = [1,3]
x[(1,2)] = 4
#x[[3,4]] = 5
print(x)

print(x.keys())
print(x.values())
print(x.items())

del x["key"]

for key, value in x.items():
    print(key, value)