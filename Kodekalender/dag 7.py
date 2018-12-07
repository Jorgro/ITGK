def sorter(liste):
    remover = []

    for i in range(len(liste)-1):
        #print(i)
        #print(liste[i+1])
        if liste[i+1] < liste[i]:
            remover.append(liste[i])
    #print(len(remover))
    #print(len(liste))
    return len(liste)-len(remover)



    return len(liste)
#print(sorter([1, 1, 2, 3, 4, 5, 7, 6, 6, 7, 8]))
#print(len([1, 1, 2, 3, 4, 5, 7, 6, 6, 7, 8]))

with open('input-vekksort.txt', 'r') as file:
    inp = file.readlines()
    for i in range(len(inp)):
        inp[i] = inp[i].strip()
        inp[i] = int(inp[i])

    #print(sorter(inp))
# lis() returns the length
# of the longest increasing
# subsequence in arr[] of size n
def lis(arr, n):

    result = 0
    lis = [0 for i in range(n)]

    # Initialize LIS values
    # for all indexes
    for i in range(n):
        lis[i] = 1

    # Compute optimized LIS values
    # in bottom up manner
    for i in range(1, n):
        for j in range(i):
            if ( arr[i] > arr[j] and
                lis[i] < lis[j] + 1):
                lis[i] = lis[j] + 1

    # Pick resultimum
    # of all LIS values
    for i in range(n):
        if (result < lis[i]):
            result = lis[i]

    return result

# Function to calculate minimum
# number of deletions
def minimumNumberOfDeletions(arr, n):

    # Find longest increasing
    # subsequence
    len = lis(arr, n)

    # After removing elements
    # other than the lis, we
    # get sorted sequence.
    return (n - len)


# Driver Code
arr = inp
n = len(arr)
print("Minimum number of deletions = ",
      minimumNumberOfDeletions(arr, n))
