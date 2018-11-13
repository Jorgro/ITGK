
# teller fra 1-5 med tall += 1 for hver gang.
k = 1
for x in range(1,6):
    k = k+1

    for y in range (1, k):

        print(y, end=' ')


    print()

# Printer ut # nedover med økende space:
k = -1
for x in range(1,6):
    k = k+1

    for y in range (1, 2):

        print('#'+k*' '+'#', end=' ')


    print()
g = int(input('Tall: '))

# for i in range(2, g):
#     if g%i == 0:
#         tall.append(i)
#         for j in range(2, g/i):
#             if g%j == 0:
#                 tall.append(j)

def primtall(tall):
    tallene = []
    for i in range(2, tall):
        if tall%i == 0:
            for j in range(2, i):
                if i%j ==0:
                    tallene.append(j)
    return tallene
print(primtall(g))
