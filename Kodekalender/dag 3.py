
primes_list = []
def primes(number):
    global primes_list
    for i in range(2, number+1):
        if (number%i) == 0:
            primes_list.append(i)
            primes(int(number/i))
            break

    return len(primes_list)

def juletall():
    jul = 0
    for i in range(4294967296):
        if len(primes(i)) == 24:
            jul += 1
    return jul

print(primes(25165824))
