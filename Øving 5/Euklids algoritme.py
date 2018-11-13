a = int(input('a = '))
b = int(input('b = '))
def gcd(a, b):
    while b != 0:
        gammel_b = b
        b = a % b
        a = gammel_b
        return a
print(gcd(a, b))

# print(f'gcd({a}, {b}) = {a}')


def reduce_fraction(gammel_b, gammel_a):
    x = gammel_a/gcd(a, b)
    y = gammel_b/gcd(a, b)
    print(f'{x}/{y}')
reduce_fraction(a, b)
