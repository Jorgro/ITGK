
def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1
     # Print all prime numbers 
    numbers = []
    for p in range(2, n): 
        if prime[p]: 
            #print(p)
            numbers.append(p)
    return numbers


def sum_divisors(n):
    """Return a list of the sums of divisors for the numbers below n.

    >>> sum_divisors(10) # https://oeis.org/A000203
    [0, 1, 3, 4, 7, 6, 12, 8, 15, 13]

    """
    result = [1] * n
    result[0] = 0
    for p in range(2, n):
        if result[p] == 1: # p is prime
            p_power, last_m = p, 1
            while p_power < n:
                m = last_m + p_power
                for i in range(p_power, n, p_power):
                    result[i] //= last_m    # (B)
                    result[i] *= m          # (B)
                last_m = m
                p_power *= p
    return result



primes = SieveOfEratosthenes(10000000)
abundants = sum_divisors(10000000)
print(len(primes))
sum_ = 0
for i in primes:
    #print(i)
    if abundants[i+1] > 2*(i+1) and i+2 in primes:
        sum_ += i

print(sum_)


