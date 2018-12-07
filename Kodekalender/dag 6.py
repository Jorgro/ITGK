import time
def find_0s(number):
    return str(number).count('0')>len(str(number))/2
output = 0
stime = time.time()
for i in range(1, 18163106):
    if find_0s(i):
        output += i

print(output)

etime = time.time()
dtime = etime-stime
print(dtime)
