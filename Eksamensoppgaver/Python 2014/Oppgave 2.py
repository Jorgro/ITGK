#2a)
def inputPerson():
    name = input('Name: ')
    ID = input('ID: ')
    weight = int(input('KG: '))
    size = int(input('Size: '))
    numbers = []
    numbers.append(name), numbers.append(ID)
    numbers.append(weight), numbers.append(size)
    return numbers

#2b)
def readDbFile(filename):
    table = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            list_line = line.split(';')
            table.append(list_line)

    return table

#2c)
# def printMemberList(db):
#     print('NAME ' + 'ID-NR '.rjust(14) + 'VEKT kg. '.rjust(12) + 'SKJERMSTORLEIK'.rjust(4))
#     for i in db:
#         print(f'{i[0]} {i[1].rjust(19-len(i[0]))} {i[2].rjust(5)} kg {i[3].rjust(4)} kvadratfot')
db = readDbFile('members.txt')
print('\n')

def printMemberList(db):
    print('NAVN             ID-NR   VEKT kg. SKJERMSTØRRELSE')
    for line in db:
        s=line[0].ljust(15)
        s+=line[1].rjust(9)
        s+=str(line[2]).rjust(5)+' kg '
        s+=str(line[3]).rjust(4)+' kvadratfot'
        print(s)

#2d)
def addPerson(filename):
    person = inputPerson()
    str_person = ''
    for i in person:
        str_person += str(i)+';'
    with open('members.txt', 'a') as file:
        file.write(str_person[:len(str_person)-1])

#2e)
def feet2seconds(height):
    if height < 3000:
        return 0
    elif height <= 4000:
        return (height-3000)/100
    else:
        return 10 + (height-4000)/200
