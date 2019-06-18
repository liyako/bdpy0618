a1 = list('abc')
a2 = list('def')
a9 = list('hij')
a1.append(a2)
a1.append(a9)
print 'append==>', a1, a9
a3 = list('abc')
a4 = list('def')
a10 = list('hij')
a3.extend(a4)
a3.extend(a9)
print 'extend==>', a3, a9
a5 = list('abc')
a6 = list('def')
print '+ ==>', a5 + a6
a7 = list('abc')
a8 = list('def')
for x in a8:
    a7.append(x)
print 'append each by each==>', a7