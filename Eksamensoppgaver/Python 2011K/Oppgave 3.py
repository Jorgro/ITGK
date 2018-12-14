#3a)
def rente(laanBelop, renteFot):
    return laanBelop*renteFot/100

#3b)
def termBelop(laanBelop, renteFot, antallTerminer):
    i = renteFot/100
    over = laanBelop*(1+i)*(1-(1/(1+i)))
    under = 1-(1/(1+i)**antallTerminer)
    return over/under

print(termBelop(1000, 5, 3))

#3c)
def restLaan(laanBelop, renteFot, antallTerminer, termin):
    if antallTerminer <= termin: 
        return 0
    rest = laanBelop
    for i in range(termin):
        rest += rente(rest, renteFot)
        rest -= termBelop(laanBelop, renteFot, antallTerminer)
        
    
    return rest

print(restLaan(1000, 5, 3, 2))
