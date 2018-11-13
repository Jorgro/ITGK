a= int(input('a = '))
b= int(input('b = '))


def delelig(a, b):
    return a % b == 0

print(delelig(a, b))

p = int(input('Sjekk om det er et primtall: '))

def isPrime(p):
    f = []
    for x in range(2, p-1):
        if p % x == 0:
            f.append('False')

        elif p % x != 0:
            f.append('True')
    if 'False' in f:
        print('False')
    else:
        print('True')



def isPrime2(p):
    f = []
    for i in range (3, round(p**0.5 + 0.5), 2):
        if p % i == 0:
            f.append('False')
        elif p % i != 0:
            f.append('True')
    if p % 2 ==0 and p !=2:
        f.append('False')
    return 'False' in f
print(isPrime2(29))
