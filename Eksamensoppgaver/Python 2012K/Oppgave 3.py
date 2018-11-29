#3a)
def mshd2s(minutter, sekunder, hundredeler):
    time = minutter*60 + sekunder + hundredeler/100 
    return time

print(mshd2s(2, 10, 20))

#3b)
def rundeTid(startTid, sluttTid):
    start = mshd2s(startTid[0], startTid[1], startTid[2])
    slutt = mshd2s(sluttTid[0], sluttTid[1], sluttTid[2])

    return slutt-start

print(rundeTid([0,45,20], [1,14,55]))

#3c)
def alleRundeTider(passeringsTider):
    tider = []
    for i in range(len(passeringsTider)-1):
        tid = rundeTid(passeringsTider[i], passeringsTider[i+1])
        tider.append(tid)

    return tider

print(alleRundeTider([[0,20,0],[0,50,10],[1,21,21],[1,53,33]]))
        