#2a)
def yatzy(t1, t2, t3, t4, t5):
    numbers = [t1, t2, t3, t4, t5]
    numbers.sort()
    if numbers[0] < 1 or numbers[-1] > 6:
        return 'Error'

    return numbers

#2b)
def maxi_yatzy(liste):
    kast = len(liste)

    liste.sort()
    max = 0
    for i in liste:
        if liste.count(i) >= liste.count(max):
            max = i
    
    return f'Du kastet {kast} terninger og fikk flest {liste[max]} ({liste.count(max)} like)'

print(maxi_yatzy([1, 2, 3, 4, 4, 3]))


