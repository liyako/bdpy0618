set1 = {'A','P','P','L','E'}
print set1
set2 = set(list('BANANA'))
print set2
set3 = set1 | set2
#聯集
print set3
set4 = set1 & set2
#交集
print set4
set5 = set1 ^ set2
print set5
set3 = {'A', 'B', 'N', 'P'}
print set2 < set3, set3 < set2
set4 = {'P', 'Q'}
print set2 < set4, set2 > set4
set5 = {'A', 'B', 'N'}
print set2 < set5, set2 > set5
print len(set3)

set5.add('!')
print set5
#set3.add(set4) # <-- this will have exception