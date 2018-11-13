pos = input('Posisjon: ')
bokstav = pos[0]
Svart = ['a', 'c', 'e', 'g', 'A', 'C', 'E', 'G']
Hvit = ['b', 'd', 'f', 'h', 'B', 'D', 'F', 'H']
SvartT =[1, 3, 5, 7]
HvitT = [2, 4, 6, 8]
c = len(pos)

if int(c) != 2:
    print('Feil input. Du må skrive akkurat to tegn')
else:
    tall = int(pos[1])
    if bokstav in Svart and tall in SvartT:
        print('Svart')
    elif bokstav in Hvit and tall in HvitT:
        print('Svart')
    elif bokstav not in Svart and bokstav not in Hvit:
        print('Første tegn må være en bokstav A-H eller a-h')
    elif tall not in SvartT and tall not in HvitT:
        print('Andre tegn må være et tall 1-8')
    else:
        print('Hvit')





    
