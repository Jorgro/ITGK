def seperate(numbers, threshold):
    s = len(numbers)
    mindre = []
    større = []
    for i in range(s):
        if numbers[i]< threshold:
            mindre.append(numbers[i])
        else:
            større.append(numbers[i])
    return mindre, større
print(seperate([1, 2, 3, 4, 5, 6,], 4))
def multiplication_table(n):

    multiplication_table = []
    for i in range(1, n+1):
        rowi = []
        for k in range(1, n+1):
            rowi.append(i*k)

        multiplication_table.append(rowi)
    return multiplication_table
def printer(table):
    for i in range(1, len(table)+1):
        print(f'{i} : {table[i-1]}')

printer(multiplication_table(10))
