set1 = set()
for i in range(20):
    if i%2 != 0:
        set1.add(i)

set2 = set()
for i in range(10):
    if i%2 != 0:
        set2.add(i)

set3 = set1-set2
print(set3)
set4 = set3&set2
print(set4)

def allUnique(liste):
    newlist = list(set(liste))

    if len(liste)==len(newlist):
        return True
    else:
        return False
print(allUnique([1,5,2,3,7]))
