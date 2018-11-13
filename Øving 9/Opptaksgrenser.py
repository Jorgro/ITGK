import re
f = open('poenggrenser_2011.csv', 'r')
innhold = f.readlines()
g = open('poenggrenser_2011.csv', 'r')
innhold2 = g.read()
def counter(tekst):
    print(innhold.count(tekst))


karaktersnitt = []
for line in innhold:
    if line[1:5] == 'NTNU':
        if line[-5:-1] != 'lle"':
            try:
                karaktersnitt.append(float(line[-5:-1]))
            except:
                karaktersnitt.append(float(line[-3:-1]))
print(karaktersnitt)
print(min(karaktersnitt))
print(sum(karaktersnitt)/len(karaktersnitt))


def linesplitter(line):
    newstring = []
    for i in range(len(line)):
        if line[i] == '.':
            newstring.append('.')
        elif line[i] == ',':
            newstring.append(' ')
        elif line[i].isalnum() or line[i] == ' ':
            newstring.append(line[i])

    newstring2 =''.join(newstring)
    return newstring2.split()

opptaksgrenser = []
for line in innhold:
    opptaksgrenser.append(linesplitter(line))

directory = {}
subdirectory = {}

for line in opptaksgrenser:
    subdirectory[line[2]]=line[-1]
    directory[line[0]] = subdirectory
# print(directory)
print(directory['NTNU']['Fysikk'])
