numbers = [7096, 3, 3924, 2404, 4502, 4800, 74, 91, 9, 7, 9, 6790, 5, 59, 9, 48, 6345,
88, 73, 88, 956, 94, 665, 7, 797, 3978, 1, 3922, 511, 344, 6, 10, 743, 36,
9289, 7117, 1446, 10, 7466, 9, 223, 2, 6, 528, 37, 33, 1616, 619, 494, 48, 9,
5106, 144, 12, 12, 2, 759, 813, 5156, 9779, 969, 3, 257, 3, 4910, 65, 1, 907,
4464, 15, 8685, 54, 48, 762, 7952, 639, 3, 4, 8239, 4, 21, 306, 667, 1, 2, 90,
42, 6, 1, 3337, 6, 803, 3912, 85, 31, 30, 502, 876, 8686, 813, 880, 5309, 20,
27, 2523, 266, 101, 8, 3058, 7, 56, 6961, 46, 199, 866, 4, 184, 4, 9675, 92]

string_numbers = [str(e) for e in numbers]
#lage rekursiv sorterings funksjon: sorterer først på 1. indeks, så andre, så tredje... 
# Sorterer basert på verdien til indeksen (ser bare på den relevante indeksen)



def recursive_sort(liste):
    concatenate = [[] for e in range(9)]
    for i in liste:
        #print(i)
        truth = True
        for index, value in enumerate(concatenate[9-int(i[0])]):
            truth, number = recursive(value, i)
            if number == i:
                concatenate[9-int(i[0])].insert(index, i)
            if not truth:
                break
        if truth: 
            concatenate[9-int(i[0])].append(i)
        #print(concatenate)
    
    return concatenate

def recursive(number1, number2):
    j = number1[0]

    orig1 = number1
    orig2 = number2

    while len(number1) < 4:
        number1 += j
    while len(number2) < 4:
        number2 += j
    
    if int(number2) >= int(number1):
        return False, orig2
    return True, orig1

helo = recursive_sort(string_numbers)
string = ''
for liste in helo:
    for i in liste:
        string += i

print(string)




        
