a= int(input('a = '))
b= int(input('b = '))
def gcd(a, b):
    while b!=0:
        gammel_b = b
        b = a % b
        a = gammel_b

    return a
print(gcd(a, b))
def reduce_fraction(a, b):
    x = a // gcd(a, b)
    y = b // gcd(a, b)
    print(f'{a}/{b} = {x}/{y}')
reduce_fraction(a, b)
