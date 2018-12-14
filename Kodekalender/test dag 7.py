def GetCeilIndex(arr, T, l, r, key): 
  
    while (r - l > 1): 
      
        m = l + (r - l)//2
        if (arr[T[m]] >= key): 
            r = m 
        else: 
            l = m 
  
    return r 
   
def LongestIncreasingSubsequence(arr,n): 
  
    # Add boundary case, 
    # when array n is zero 
    # Depend on smart pointers 
      
    # Initialized with 0 
    tailIndices=[0 for i in range(n+1)]   
  
    # Initialized with -1 
    prevIndices=[-1 for i in range(n+1)]   
      
    # it will always point 
    # to empty location 
    len = 1 
    for i in range(1, n): 
      
        if (arr[i] < arr[tailIndices[0]]): 
          
            # new smallest value 
            tailIndices[0] = i 
          
        elif (arr[i] >= arr[tailIndices[len-1]]): 
          
            # arr[i] wants to extend 
            # largest subsequence 
            prevIndices[i] = tailIndices[len-1] 
            tailIndices[len] = i 
            len += 1
          
        else: 
          
            # arr[i] wants to be a 
            # potential condidate of 
            # future subsequence 
            # It will replace ceil 
            # value in tailIndices 
            pos = GetCeilIndex(arr, tailIndices, -1, 
                                   len-1, arr[i]) 
   
            prevIndices[i] = tailIndices[pos-1] 
            tailIndices[pos] = i 
          
    print("LIS of given input") 
    i = tailIndices[len-1] 
    while(i >= 0): 
        print(arr[i] , " ",end="") 
        i = prevIndices[i] 
    print() 
   
    return len
# test above function 
with open('input-vekksort.txt', 'r') as file:
    A = file.readlines()

for i in range(len(A)):
    A[i] = int(A[i].strip())

def subsequence(seq):
    if not seq:
        return seq

    M = [None] * len(seq)    # offset by 1 (j -> j-1)
    P = [None] * len(seq)

    # Since we have at least one element in our list, we can start by 
    # knowing that the there's at least an increasing subsequence of length one:
    # the first element.
    L = 1
    M[0] = 0

    # Looping over the sequence starting from the second element
    for i in range(1, len(seq)):
        # Binary search: we want the largest j <= L
        #  such that seq[M[j]] < seq[i] (default j = 0),
        #  hence we want the lower bound at the end of the search process.
        lower = 0
        upper = L

        # Since the binary search will not look at the upper bound value,
        # we'll have to check that manually
        if seq[M[upper-1]] < seq[i]:
            j = upper

        else:
            # actual binary search loop
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[M[mid-1]] <= seq[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower    # this will also set the default value to 0

        P[i] = M[j-1]

        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j+1)

    # Building the result: [seq[M[L-1]], seq[P[M[L-1]]], seq[P[P[M[L-1]]]], ...]
    result = []
    pos = M[L-1]
    for _ in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return len(result[::-1])


n = len(A) 
print(n)
print(subsequence(A))