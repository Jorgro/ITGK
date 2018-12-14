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

def prime_factors(number):

    prime_num = primes(512)
    
    output = 0
    i = 0
    while i < len(prime_num) and number > 1:
        if int(number%prime_num[i]) == 0:
            number = number/prime_num[i]
            #print(prime_num[i])
            i = 0
            output += 1
        else: 
            i += 1
        if output > 13:
            break
            
        
    
    return output
d = 0
for e in range(8192, 2**21 + 1, 2):
    print(e)
    if prime_factors(e) == 13:
        d += 1

print(d)
