
endring = 1.25
tol = float(input('Toleranse:'))
def multiplikasjon(tol, endring):

    prod = 2
    i = 2
    while endring > tol:

        ledd = 1 + 1/i**2
        gammel_prod = prod
        prod = prod*ledd
        endring = prod - gammel_prod
        i = i +1
    return i-1, prod

print(multiplikasjon(tol, endring))
f = []
n  = 1
while (1+1/n**2) >= (1 + tol):
    n += 1
    f.append(n)
n = f[-1]
print(f'Antall iterasjoner er {n-1}')
def rekursjon(n):
    if n < 1:
        return 1
    else:
        return (1 + 1/n**2) * (rekursjon(n-1))
print(f'Summen er {rekursjon(n)}')


# def rekursjon(n):
#     # n = symbol('n')
#     # solve((1+1/n**2) < (1 + tol),)
#
#
#     if (1+1/n**2) < (1 + tol):
#         res = (1 + 1/n**2) * float(rekursjon(n-1))
#         n += 1
#     elif n == 0:
#
#     else:
#         print(n-1)
#         print(res)
#
#
# rekursjon(n)
# print('hu')
