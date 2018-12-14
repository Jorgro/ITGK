
import itertools

comb = itertools.product(['+', '-', ''], repeat=14)
i = 0
#comb = list(comb)
output = 0



def joining(liste):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]
    

    sum_numb = str(numbers[0])

    for i in range(len(liste)):
        sum_numb += str(liste[i]) + str(numbers[i+1])

    return eval(sum_numb)

for x in comb:
    if joining(x) == 42:
        output += 1

print(output)
        


        