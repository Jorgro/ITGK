#4a)
def les_inn_bilinfo():
    merke = input('Hvilket bilmerke var det? ')
    modell = input('Hvilken modell? ')
    farge = input('Hvilken farge? ')
    bil = []
    bil.append(merke), bil.append(modell), bil.append(farge)

    return bil

#4b)
def sjekk_bil(vitne, faktisk):

    if '?' in vitne:
        for i in range(vitne.count('?')):
            vitne.remove('?')
    vitne_set = set(vitne)
    faktisk_set = set(faktisk)

    return vitne_set.issubset(faktisk_set)

SKILTBOKSTAV = ('A','B','C','D','E','F','G','H','J','K','L',
                'N','P','R','S','T','U','V','X','Y','Z','?')
#4c)
def les_gyldig_vitneskilt():
    switch = True
    SKILTBOKSTAV = ('A','B','C','D','E','F','G','H','J','K','L',
                    'N','P','R','S','T','U','V','X','Y','Z','?')

    while switch:
        car = input('Skriv inn skilt, 2 bokst + 5 tall (?=usikker) ')
        switch = False
        if car[0] not in SKILTBOKSTAV or car[1] not in SKILTBOKSTAV:
            switch = True
            print('To første tegn må være lovlig skiltbokstav eller ?')

        if len(car) != 7:
            switch = True
            print('Skiltnummer må være 7 tegn langt')

        digit = False
        for i in range(2, len(car)):
            if not car[i].isdigit() and not car[i] == '?':
                digit = True

        if digit:
            switch = True
            print('Fem siste tegn må være tall eller ?')
    return car
#4d)
def match(bil1, bil2):
    truth = []
    for i in range(len(bil1)):
        if bil1[i] != bil2[i] and bil1[i] != '?' and bil2[i] != '?':
            truth.append(False)
    return not False in truth


#4e)
def match_liste(skilt, skiltliste):
    # skilt = skilt.replace('?', '')
    possible = []
    print(skilt)
    for j in range(len(skiltliste)):
        truth = []
        for i in range(len(skilt)):

            if skilt[i] != skiltliste[j][i] and skilt[i] != '?' and skiltliste[j][i] != '?':
                truth.append(False)


        if False not in truth:
            possible.append(skiltliste[j])

    return possible

#4f)
def get_cars(car_dic, skilt, bilinfo):
    keys = []
    for key, value in car_dic.items():
        truth = True
        if match(key, skilt):
            for i in range(len(value)-1):
                if value[i] != bilinfo[i] and bilinfo[i] != '?':
                    truth = False
        else:
            truth = False


        if truth:
            keys.append(key)

    return keys


def main():
    bil_dic = {}

    try:
        with open('biler.txt', 'r') as file:
            for line in file:
                line = line.split()
                bil_dic[line[0]] = line[1:]
    except:
        print('biler.txt does not exist.')
        exit()

    fortsett = True
    while fortsett:
        bilinfo = les_inn_bilinfo()
        skilt = les_gyldig_vitneskilt()
        biler = get_cars(bil_dic, skilt, bilinfo)
        if not biler:
            print('No cars found.')
        else:
            for i in biler:
                print(f'{i} Eier: {bil_dic[i][-1]} ')

        bruker = input('Vil du fortsette? J/N ')
        if bruker == 'N':
            fortsett = False
main()
