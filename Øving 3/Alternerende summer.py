
n = int(input('n = '))
f = []
for x in range(1, n+1):
    if x % 2 == 0: 
        u = -x**2
        f.append(u) 
    else:
        v = x**2
        f.append(v) 
     
print(sum(f))
print(f)
