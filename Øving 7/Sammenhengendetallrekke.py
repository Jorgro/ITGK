import random

def randList(size, lower_bound, upper_bound):
    randomnumbers = []
    while len(randomnumbers) < size:
        randomnumbers.append(random.randint(lower_bound, upper_bound))
def compareLists(list1, list2):
    commonelements = []
    for i in range(len(list1)):
        if list1[i] in list2:
            commonelements.append(list1[i])

    return commonelements

def multiCompList(lists):
    for i in range(len(lists)-1):
        newlist = compareLists(lists[i], lists[i+1])
    return newlist
a = [1,2,3]
b = [4,2,1]
c = [7,2,1]
d = [8,9,2]

def even_seq(list):
    best = (-1, -1)
    start_i = 0
    count = 0
    for i, n in enumerate(list):
        if n % 2 == 0:
            count += 1
            if count > best[1]:
                best = (start_i, count)
        else:
            start_i = i + 1
            count = 0

    return best

print(even_seq([3, 2, 2, 3, 7, 2, 2]))
