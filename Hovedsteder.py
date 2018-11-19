
def les_fil(filnavn):
    try:
        with open(filnavn, 'r', encoding="UTF-8") as file:
            return file.read()
    except IOError:
        print('You got gnomed')
        return None

hoved = les_fil('hovedsteder.txt')

def streng_til_liste(streng):
    streng = streng.split(',')
    returning = []
    for i in streng:
        i = i.split()
        if len(i) == 2 and i not in returning:
            returning.append(i)
        elif len(i) > 2:
            #i[1] += ' ' + i[2]
            for j in range(2, len(i)):
                i[1] += ' ' + i[j]
        if i not in returning:
            returning.append(i[:2])
        #evt liste.append([liste[0], ' '.join(liste[1:])])
    return returning

hoved2 = streng_til_liste(hoved)

def skriv_ut_liste(liste):
    for i in liste:
        print(f'Hovedstaden i {i[0]} er {i[1]}')
#skriv_ut_liste(hoved2)

def spm(liste):
    import random
    print('Willkommen zu Hitlers anfragspiel! ')
    rand_num = random.randint(0, len(liste)-1)
    if liste[rand_num][0] == 'Tyskland':
        print('DER BESTE CITY UBER ALLES! SIEG')
        return liste
    else:
        answer = input(f'Hva er hovedstaden i {liste[rand_num][0]}? ')

    if answer == liste[rand_num][1]:
        liste.pop(rand_num)
        print('Das ist richtig!!! Sieg')
    else:
        print('Das ist nicht richtig!! Zu den Konzentrationslager!')

    return liste


class Dick:

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculator(self):
        print(self.length*(self.width/2)**2 *3.14)
    
    def __repr__(self):
        str_2 = '-'*self.length
        return f'{str_2}:'

Josteins = Dick(2, 1)
Josteins.calculator()
print(Josteins)
Jørgens = Dick(20, 20)
print(Jørgens)
def liste_til_dic(liste):
    dic = {}
    for i in liste:
        dic[i[0]] = i[1]

    return dic

print(liste_til_dic(hoved2))

def rover(tekst):

    kons = 'bcdfghjklmnpqrstvwxz'
    new = ''
    for i in range(len(tekst)):
        if tekst[i].lower() in kons:
            new += tekst[i] +'o' + tekst[i].lower()
        else:
            new += tekst[i]


    return new

print(rover('ITGK er kult'))

def unrover(tekst): 
    kons = 'bcdfghjklmnpqrstvwxz'
    new = ''
    i = 0
    while (i < len(tekst)):
        if tekst[i].lower() in kons:
            new += tekst[i]
            i += 3
        else:
            new += tekst[i]
            i += 1

    return new

print(unrover('ITotGogKok eror kokuloltot'))

