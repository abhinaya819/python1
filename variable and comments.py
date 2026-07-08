a , b = 10, 20
print(id(a), id(b))

a, b = 256, 256
print(id(a), id(b))


a, b = 257, 257
print(id(a), id(b))


a, b = 10,20
print(id(a), id(b))

a,b = b,a
print(id(a), id(b))


print(a,b)

