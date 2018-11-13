import random


def random_matrise(n, m):
    matrise = []
    for i in range(n):
        rad = []
        for k in range(m):
            a = random.randint(0, 9)
            rad.append(a)
        matrise.append(rad)

    return matrise
    # matrise = []
    # a = [[random.randint(0, 9)] * m for i in range(n)]
    # return a

# print(random_matrise(3, 4))
a = random_matrise(3,4)
b = random_matrise(3, 4)
print(a)
print(b)
def matrix_addition(a, b):
    newmatrix = []
    for i in range(len(a)):
        newrow = []
        for j in range(len(a[i])):
            number = a[i][j]+b[i][j]
            newrow.append(number)
        newmatrix.append(newrow)
    return newmatrix
print(matrix_addition(a, b))
print('[')
for i in a: print(f'{i},')
print(']')
