
def is_six_edge(liste):
    if liste[-1] == 6 or liste [0] == 6:
        return True
    else:
        return False
print(is_six_edge([1, 2, 3, 4, 5, 7]))

def average(liste):
    a = sum(liste)/len(liste)
    return a
print(average([1, 2, 3, 4, 5, 6]))
def median(liste):
    liste.sort()
    a = liste[round(len(liste)/2)-1]
    return a
print(median([1, 1, 1, 2, 3, 3, 3,]))
