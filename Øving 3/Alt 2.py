k = int(input('k = '))
n=0
h=0
f=[]
while h <= k:
    n += 1 
    if n % 2 == 0: 
        u = -n**2
        f.append(u) 
    else:
        v = n**2
        f.append(v)
    
    h = sum(f)


print('Iterasjoner: ', len(f)-1)
if f[-1] > 0:
    print('Sum før over k: ', sum(f)-f[-1])
elif f[-1] < 0:
    print('Sum før over k: ', sum(f)+f[-1])