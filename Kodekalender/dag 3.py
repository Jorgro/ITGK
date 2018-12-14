


def test_prime(number):
    for i in range(2, round(number**1/2)+1):
        if number%i==0:
            return False
    return True 

def primes(number):
    primes = []
    for i in range(2, number):
        if test_prime(i) and i not in primes:
            primes.append(i)
    return primes
   
def num_primes():
    import itertools
    prime = primes(338)
    hey = itertools.combinations(prime, 14)
    for x in hey:
        print(x)
#num_primes()
prime = primes(510)
for i in prime:
    if 2**18 * 3**5 * i <= 4294967296:
        continue

from functools import reduce
def find_configurations(number):
    import itertools
    global juletall
    counter = 0
    prime = primes(510)
    hey = combinations_with_replacement(prime, number)
    for x in hey:
        three_list = [3 for e in range(number)]
        if reduce(lambda x, y: x * y, list(x), 1) <= 3**(number):
            counter += 1
            print(x)
            if x not in juletall:
                juletall.append(x)
        else:
            k = False
        #elif reduce(lambda x, y: x * y, list(x), 1) > 3**(number) and x.count(2) + x.count(3) = ?
        
        if set(list(x)) == set(three_list):
            break
        else:
            continue
counter = 0
juletall = []
def combinations_with_replacement(iterable, r, grense=4294967296):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    global counter
    global juletall
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)

        #print(pool)
        elem = tuple(pool[i] for i in indices) 
        if reduce(lambda x, y: x * y, list(elem), 1) > grense:
            if i > n-1:
                indices[i:] = [indices[i] + 1] * (r - i)
            
            
        else:
            juletall.append(tuple(pool[i] for i in indices))
            yield tuple(pool[i] for i in indices)


grense = 4294967296
d = combinations_with_replacement(primes(510), 24)
#dd = 1
for x in d:
    print(x)
    continue
    #dd += 1
    #print(x)
#print(dd)
"""while i <= 13:
    d = combinations_with_replacement(primes(509), 24-i)
    for x in d:
        print(x)
    i += 1
    siste_elem = list(juletall[-1])
    grense = 4294967296/reduce(lambda x, y: x * y, siste_elem[23:22-i:-1], 1)
"""
#print(len(juletall))






    




#for x in hey:
    #print(x)
from functools import reduce
#reduce(lambda x, y: x * y, [1, 2, 4], 1)






#521 er det høyeste primtallet som er med i en 24 lang primtallsfaktoriseringkonfigurasjon