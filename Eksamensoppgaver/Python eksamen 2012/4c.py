#4c)
import random
N = input('Antall unike tall: ')
minvalue = int(input('Min value: '))
maxvalue = int(input('Max value: '))
def generate_testdata(N, minvalue, maxvalue):
    result = []
    while len(result)<int(N):
        g = random.randint(minvalue, maxvalue)
        if g not in result:
            result.append(g)

    return result
print(generate_testdata(N, minvalue, maxvalue))
