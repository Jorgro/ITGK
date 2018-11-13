

def hundre():
    tall = []
    for i in range(0, 100):
        tall.append(i)
    return tall


def delelig(tall):
    deleligliste = []
    for i in range(100):
        if tall[i]%3 == 0:
            deleligliste.append(tall[i])
        elif tall[i]%10 ==0:
            deleligliste.append(tall[i])
    summendelelig = sum(deleligliste)
    return summendelelig

def plassbytter(tall):

    for i in range(100):
        if tall[i]%2 == 0:
            tall[i]=tall[i+1]
        elif tall[i]%2 !=0:
            tall[i]=tall[i]-1

    return tall

def reverserer(listemtall):
    length = len(listemtall)
    L = length

    ny_liste = [None]*length

    for tall in listemtall:
        L = L - 1
        ny_liste[s] = tall
    return ny_liste
print(reverseerer(plassbytter(hundre())))
