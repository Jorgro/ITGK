#3a)
parties = ['TeaParty','CoffeeParty','MilkParty','HouseParty','BeachParty']
def initElection(parties):
    return [[0]*len(parties) for i in range(92)]
election = initElection(parties)


#3b)
def updateElection(election, number, list_votes):
    for i in range(len(list_votes)):
        election[number][i] += list_votes[i]
    return election

#3c)
def printLeadP(election):
    total_votes = [0]*len(parties)
    for i in range(len(election)):
        for j in range(len(election[i])):
            total_votes[j] += election[i][j]

    max = total_votes[0]
    for i in range(len(total_votes)):
        if total_votes[i] > max:
            max = total_votes[i]
            index = i
    print(f'{parties[index]} is leading with {total_votes[index]} votes')


#3d)
def printResults(election):
    leading_districts = [0]*len(parties)
    tied = 0
    for i in range(len(election)):
        maximum =  max(election[i])
        if election[i].count(maximum) > 1 and maximum != 0:
            tied += election[i].count(maximum)
        elif maximum != 0:
            leading_districts[election[i].index(maximum)] += 1
    for i in range(len(parties)):
        if leading_districts[i] == 1:
            print(parties[i] + ": " + (str(leading_districts[i]) + " delegate").rjust(57-len(parties[i])))
        else:
            print(parties[i] + ": " + (str(leading_districts[i]) + " delegates").rjust(58-len(parties[i])))
    string1 = "Undecided (tied): "
    string2 = "Undecided (no votes): "
    print("Undecided (tied): " + (str(tied) + " delegates").rjust(60-len(string1)))
    print("Undecided (no votes): " + (str((92-sum(leading_districts)-tied)) + " delegates").rjust(60-len(string2)))
election = updateElection( election, 34, [601,2000,3000,50,22])
election = updateElection( election, 34, [601,2000,3000,50,22])
election = updateElection( election, 34, [601,2000,3000,50,22])
printResults(election)
