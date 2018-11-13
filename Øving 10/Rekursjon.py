def rekursiv(tall):
    if tall == 1:
        return 1
    else:
        tall = tall+rekursiv(tall-1)
        return tall
print(rekursiv(53))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
def smallest_number(numbers):
    if numbers[0] < numbers[1]:
        smallest = numbers[0]
        smallest_number(numbers)
        return smallest

def findMinimum(l):
    if len(l) == 0:
       raise ValueError('Cannot find the minimum of an empty list.')
    elif len(l) == 1:
       return l[0]
    else:
       minNumber = findMinimum(l[1:])
       min = l[0]
       if minNumber < min:
            min = minNumber
       return min
print(findMinimum([5,3,2,6]))
import math
def binary_search(A, T):
    L = 0
    R = len(A)-1
    while L <= R:
        m = math.floor((L+R)/2)
        if A[m] < T:
            L = m+1
        elif A[m] > T:
            R = m-1
        else:
            return m
    return -float('inf')
print(binary_search([1,4,6,9,13,34,45,53,65,78],53))
#In the worst case, binary search makes log _{2}(n)+1 iterations of the comparison loop
