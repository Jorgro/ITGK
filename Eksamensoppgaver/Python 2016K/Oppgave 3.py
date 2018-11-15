#3a)
def sek_paa_benken(ant_paa_laget, ant_paa_banen, kamptid):
    time = kamptid*60
    innbytter = ant_paa_laget - ant_paa_banen
    try:
        return round(time/(ant_paa_laget/innbytter))
    except: 
        return 0

print(sek_paa_benken(5, 5, 12))

#3b)
def minutt_sekunder(sekunder):
    minutes = sekunder//60
    seconds = sekunder%60
    if seconds < 10:
        str_seconds = '0' +str(seconds)
        return f'{minutes}:{str_seconds}'
    return f'{minutes}:{seconds}'
print(minutt_sekunder(206))

#3c)
def les_inn_forfall():
    print('Skriv navn, eller kun ENTER (tom tekst) for å avslutte.')
    names = []
    input_names = 'hey'
    while input_names != '':
        input_names = input('Spiller som har meldt forfall: ')
        if input_names != '':
            names.append(input_names)

    return names

#3d)
def finn_tilgjengelige(alle, forfall):
    sett_alle = set(alle)
    sett_forfall = set(forfall)

    return list(sett_alle-sett_forfall)
global barn
barn = ['Ada', 'Bo', 'Emma A.', 'Emma B.', 'Henrik', 'Ine', 'Jo', 'Kim',
'Lucas', 'My', 'Ola', 'Pia']
forfall = ['Henrik', 'Emma B.', 'Lucas']

print(finn_tilgjengelige(barn, forfall))

#3e)
import random
def laginndeling(spillere, sp_per_lag):
    ant_lag = len(spillere)//sp_per_lag
    liste_lag = [[] for i in range(ant_lag)]
    while len(spillere) > 0:
        for i in range(len(liste_lag)):
            player = random.choice(spillere)
            liste_lag[i].append(player)
            spillere.remove(player)

    return liste_lag

print(laginndeling(barn, 5))
        
#3f)
def main():
    forfall = les_inn_forfall()
    sp_per_lag = int(input('Spillere per lag: '))
    Kamptid = int(input('Kamptid (minutter): '))
    barn = ['Ada', 'Bo', 'Emma A.', 'Emma B.', 'Henrik', 'Ine', 'Jo', 'Kim',
            'Lucas', 'My', 'Ola', 'Pia']
    tilgjengelige = finn_tilgjengelige(barn, forfall)
    liste_lag = laginndeling(tilgjengelige, sp_per_lag)
    
    for i in range(len(liste_lag)):
        print(f'Lag {i+1}: ')
        print(liste_lag[i])
        benktid = sek_paa_benken(len(liste_lag[i]), sp_per_lag, Kamptid)
        print(f'Tid på benken pr spiller: {minutt_sekunder(benktid)}')



#3g)
def ny_fil(name, file_in, file_out):
    games = ''

    with open(file_in, 'r') as file:
        for line in file:
            if name in line:
                games += line

    with open(file_out, 'w') as file:
        file.write(games)
ny_fil('Pythonmyra', 'in.txt', 'out2.txt')
    