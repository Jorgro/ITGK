#4a)
def importResults(file):
    innhold = []
    try:
        with open(file, 'r') as filename: 
            for line in filename:
                innhold.append(line)
        return innhold

    except IOError:
        user = input(f'{file} could not be found. File name ("q"-quits): ')
        if user == 'q':
            return
        return importResults(user)

results = importResults('Matches.txt')

#4b)
def analyzeResults(results):
    newRes = []

    for line in results:
        line = line.replace('-', ',')
        line = line.split(',')
        temp = []
        for i in line:
            try: 
                temp.append(int(i))
            except ValueError:
                temp.append(i)
        newRes.append(temp)
    return newRes

analyzed= analyzeResults(results)

#4c)
def calculateScores(homeGoals, awayGoals):

    if homeGoals == awayGoals:
        return 1, 1
    if homeGoals > awayGoals:
        return 3, 0
    else:
        return 0, 3

#4d)
def sumTeamValues(analyzed):

    teams = {}
    for  i in analyzed: #oppretter dict med alle scores
        if i[0] not in teams:
            teams[i[0]] = [0, 0]

        if i[1] not in teams:
            teams[i[1]] = [0, 0]
            
    for i in analyzed:

        score1, score2 = calculateScores(i[2], i[3])
        teams[i[0]][0] += score1
        teams[i[1]][0] += score2

        teams[i[0]][1] += 1
        teams[i[1]][1] += 1
    return teams

anal = sumTeamValues(analyzed)

#4e)
def showResults(analyzed):
    print('#'*45)

    for i in analyzed:
        if i[2] > i[3]:
            k = ' (H)'
        elif i[2] < i[3]:
            k = ' (B)'
        else: 
            k = ' (U)'

        print('# ' + i[0].ljust(15) + i[1].ljust(15) + str(i[2]).rjust(2) + ' - ' + str(i[3]).rjust(2) + k +' #')

    print('#'*45)

showResults(analyzed)

#4f)
def savePoints(team_data):
    sorted_data = sorted(team_data.items(), key =lambda elem: elem[1][0], reverse = True)
    with open('Points.txt', 'a+') as file:
        file.write('#'*35 + '\n')
         
        file.write('# Navn'.ljust(19) + 'Poeng'.ljust(8) + 'Kamper #\n')
        
        for i in sorted_data: 
            streng = '# '+ i[0].ljust(19) + str(i[1][0]).rjust(2) +' '.ljust(6) + str(i[1][1]) + '#'.rjust(5) + '\n'
            file.write(streng)
        file.write('#'*35)
    
        
savePoints(anal)

def getkey(item):
    return item[1][0]

hey = [(1, 2), (4, 5), (7, 8), (1, -1)]

hey = sorted(hey, key = getkey, reverse = True)
print(hey)

getk = lambda elem: elem[1] 
hey = sorted(hey, key=getk)
print(hey)
summation = lambda x, y: x+y

print(summation(1, 3))

