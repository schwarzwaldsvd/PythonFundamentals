names = ("John", "Charles", "Mike", "Grigore", "Grigore")
pcs = ("Dell", "IBM", "HP", "Asus", "Asus")

t = tuple(zip(names, pcs))
x = list(zip(names, pcs))
y = set(zip(names, pcs))
z = dict(zip(names, pcs))

print(t)
print(x)
print(y)
print(z)
