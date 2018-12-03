def vekksort(filename):
    summer = 0
    liste = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            liste.append(int(line))
    test = [0]
    for i in range(0, len(liste)):
        if test[-1] <= liste[i]:
            test.append(liste[i])
    return sum(test)

print(vekksort('input-vekksort.txt'))
