#4a)
NTNU_scores = (89, 77, 65, 53, 41, 0)
NTNU_letters = ('A', 'B', 'C', 'D', 'E', 'F')
TASKS = ('1', '2a', '2b', '2c', '3a', '3b', '3c', '3d', '4a', '4b', '4c', '4d', '4e',
'4f', '4g', '4h')
WEIGHTS = (25, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)

#4b)
def makeArray(Numbers, Text):
    table = [[] for i in range(len(Text))]
    for i in range(len(table)):
        table[i].append(Numbers[i])
        table[i].append(Text[i])
    return table
limitLetters = makeArray(NTNU_scores, NTNU_letters)
#4c)
def computeScore(Points, WEIGHTS):
    total = 0
    for i in range(len(Points)):
        total += Points[i]*WEIGHTS[i]/10

    return total

#4d)
def score2Letter(scoreSum, limitLetters):
    for i in range(len(limitLetters)):
        if scoreSum >= limitLetters[i][0]:
            return limitLetters[i][1]
        else:
            continue

#4e)
def addCandidate(candidateNumber, Scores, WEIGHTS):
    score = computeScore(Scores, WEIGHTS)
    file_string = str(candidateNumber)

    for i in Scores:
        file_string += '\t'+str(i).strip()
    file_string += '\t'+str(round(score, 1))
    try:
        with open('eksamen.txt', 'a+') as file:
            file.write(file_string+'\n')
    except Exception as error:
        print(error)
addCandidate(12492,[0,10,10,10,0,0,0,0,0,10,10,10,10,10,10,10],WEIGHTS)

#4f)
def readResultFile(filename):
    table = []
    with open(filename, 'r') as file:

        for line in file:
            line = line.rstrip()
            table.append(line.split('\t'))

    return table[1:]


#4g)
def checkResultOK(filename, WEIGHTS):
    table = readResultFile(filename)
    truth = True
    count = {}
    for i in range(len(table)):
        if table[i][0] not in count:
            count[table[i][0]] = 1
        else:
            count[table[i][0]] = count.get(table[i][0]) +1
    print(count)
    for key, value in count.items():
        if value > 1:
            print(f'ERROR: Candidate {key} appears more than once!')
            truth = False
    for i in table:
        for j in i[1:len(i)-1]:
            if int(j) < 0 or int(j) > 10:
                print(f'ERROR: Candidate {i[0]} scores are not between 0-10!')
                truth = False

    for i in table:
        points = i[1:len(i)-1]
        points_2 = [int(i) for i in points]
        score = computeScore(points_2, WEIGHTS)
        if str(score) != str(i[-1]):
            print(f'ERROR: Candidate {i[0]} has wrong total score!')
            truth = False

    return truth

#4g)
def listAll(filename, limitLetters):
    table = readResultFile(filename)
    grades = [[] for i in range(len(table))]
    print(grades)
    for i in range(len(table)):
        grades[i].append(table[i][0])
        grades[i].append(float(table[i][-1]))

    print(grades)
    for i in grades:
        i.append(score2Letter(i[1], limitLetters))

    for i in grades:
        print(f'{i[0]} {str(i[1]).rjust(7)} {i[2]}')
    print(len(table))
listAll('eksamen.txt',limitLetters)
