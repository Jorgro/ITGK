def exponentiation(b, n, m):
    x = 1
    power = int(b) % int(m)
    for i in range(1, len(n)+1):
        if n[-i] == '1':
            x = (x*power) % m
        power = power**2 % m
    return x

def binary(a):
    b=''
    while a or b=='':
        b=str(a%2)+b
        a=a//2
    return b
