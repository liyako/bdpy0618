import math
import random

print math.pi, math.log10(10), math.log10(2)
#計算pi log10 log2
print math.sqrt(5)
for k in range(0, 100):
    print random.randint(10, 50),
#取亂數1-50
print "\n"
stores = ['7-11', 'Fami', "OK", "Hi-Life"]
for k in range(0, 10):
    print random.choice(stores),
#亂數字串選擇
pokers = ['A', 'K', 'Q', 'J', '10', '9']
for l in range(0, 10):
    random.shuffle(pokers)
    #亂數洗牌
    print pokers