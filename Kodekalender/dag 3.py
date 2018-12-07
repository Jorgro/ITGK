

def primes(number):
    primes_list = []
    for i in range(2, number+1):
        if (number%i) == 0:
            primes_list.append(i)
            break
            primes(int(number/i))

    return len(primes_list)

def juletall():
    jul = 0
    for i in range(16000000, 4294967296):
        if primes(i) == 24:
            jul += 1
        print(jul)
    return jul

print(juletall())
