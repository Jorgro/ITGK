i = -1
g = 0
n = int(input('n = '))
r = float(input('r = '))
tol = float(input('Toleranse: '))


while i < n:
    i += 1
    g = g + r**i
print(f'Summen er {g}')
    

t = 1/(1-r) - (1-r**(i+1))/(1-r)
while tol <= t:
    t = 1/(1-r) - (1-r**(i+1))/(1-r)
    i += 1
    g = g + r**i
print(f'Number of iterations: {i}')
print(f'Differanse mellom virkelig og estimer: {t}')
    