#4a) 
highscores = {}
highscores[1] = ['Albus',100]
highscores[2] = ['Fleur',90]
highscores[3] = ['Frank',80]
highscores[4] = ['Harry',70]
highscores[5] = ['Harry',70]
highscores[6] = ['Harry',70]
highscores[7] = ['Harry',70]
highscores[8] = ['Harry',70]
highscores[9] = ['Harry',70]
highscores[10] = ['Harry',70]
def check_highscore(points, scores):

    for key, value in scores.items():
        if points > value[1]:
            return key
    return -1


#4b) 
def print_highscores(scores):
    for key, value in scores.items():
        print(str(key).rjust(2) + ' ' + value[0].ljust(20) + str(value[1]).rjust(5))


#4c)
def add_highscore(points, name, scores):
    place = check_highscore(points, scores)
    if place == -1:
        return scores
    temp = highscores.get(place)
    highscores[place] = [name, points]
    
    for i in range(place+1, 10):
        temp2 = highscores.get(i)
        highscores[i] = temp
        temp = temp2
    
    return scores



#4d)
def most_highscores(scores):
    list_all = list(scores.items())
    newList = []
    for i in list_all:
        newList.append(i[1][0])
    max = 1
    index = 0
    for i in newList:
        if newList.count(i) > max:
            max = newList.count(i)
            index = newList.index(i)
    
    return newList[index]


#4e)
def new_highscorelist():
    import random
    highscore = {}
    
    names = ['Albus', 'Fleur', 'Frank', 'Harry', 'Hermine', 'Minverva', 'Ron', 'Severus', 'Sirius', 'Vernon']
    random.shuffle(names)
    for i in range(100, 0, -10):
        highscore[int(i/10)] = [names[int(i/10)-1], i]
    
    return highscore

print(new_highscorelist())





        

