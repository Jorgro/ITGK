

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

from functools import reduce



def increase_pos(indexes, pos):
    indexes[pos] += 1
    new_val = indexes[pos]
    for i in range(0, pos):
        indexes[i] = new_val
        
indexes = [0]*3
        


counter = 0
indice = 0
def incrementer(indexes):
    val1 = 0
    global indice
    global counter
    prefig = [e for e in indexes]
    increase_pos(indexes, indice)
    prime_numbers = primes(510)
    
    for i in range(96):
        print(indexes)
        increase_pos(indexes, indice)
        size = 1
        breaking = False
        for n in indexes:
            if n > len(prime_numbers)-1:
                breaking = True
                break
            else:
                size *= prime_numbers[n]

        if size > 2**21 or breaking:
            indice += 1
            break 
        
        counter += 1
    print(counter)
    increase_pos(prefig, indice)
    #print(prefig)
    incrementer(prefig)      


#incrementer(indexes)

def testing():
    ind = [0, 0, 0]
    val1 = 0
    while val1 < 3:
        prefig = [e for e in ind]

        for i in range(2):
            print(ind)
            increase_pos(ind, val1) #kan ikke bruke val1 siden da skifter den feil indeks
        ind = prefig
        
        val1 += 1
        increase_pos(ind, val1+1)
        #print(ind)

testing()






        
