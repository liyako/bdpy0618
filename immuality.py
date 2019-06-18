x = 5
print x, hex(id(x))
x = 6
print x, hex(id(x))

l = [5]
print l, hex(id(l))
l[0] = 6
print l,hex(id(l))