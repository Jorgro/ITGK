
import math
N=256*2**24 #4294967296=2^32

p22=[2,3,5,7,11,13,17,19] #primes under 22, 22^2<512
p512=p22+[a for a in range(20,512) if sum([a%b==0 for b in p22])==0] #primes under 512


def factors(number):
	n=number
	output=0
	for i in p512:
		if n<i:
			break
		while n%i==0:
			output+=1
			n=n/i
	return output

print(sum([1 for i in range(2**21) if factors(i)==13]))
