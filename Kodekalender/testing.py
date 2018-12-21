# An Optimized Solution to check Abundant Number 
# in PYTHON 
import math 
  
# Function to calculate sum_ of divisors 
def getSum(n) : 
    sum_ = 0
      
    # Note that this loop runs till square root 
    # of n 
    i = 1
    while i <= (math.sqrt(n)) : 
        if n%i == 0 : 
              
        # If divisors are equal,take only one 
        # of them  
            if n/i == i : 
                sum_ = sum_ + i 
            else : # Otherwise take both 
                sum_ = sum_ + i 
                sum_ = sum_ + (n / i ) 
        i = i + 1
      
    # calculate sum_ of all proper divisors only 
    sum_ = sum_ - n 
    return sum_ > n
  
          