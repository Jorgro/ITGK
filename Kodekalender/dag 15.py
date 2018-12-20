import time
counter = 0
stime = time.time()
with open('input-gullbursdag.txt', 'r') as file:
    for line in file:
        line.strip()
        line = line.split('.')
        birthday = int(line[-1])
        for i in range(round(birthday**(1/2))-1, birthday + 1000):
            if i**2 == birthday+i:
                counter += 1
                break
            if i**2 > birthday + i:
                break
print(counter)
etime = time.time()
dtime = etime-stime
print(dtime*1000)