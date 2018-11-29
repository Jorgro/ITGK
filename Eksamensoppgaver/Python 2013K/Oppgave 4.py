#4a) 
def enterWords():
    user_input = 'no'
    wordList = []
    while user_input:
        user_input = input('Enter word (press Enter to quit): ')
        if user_input:
            wordList.append(user_input)
    return wordList

#4b) 

def noVowels(inList):
    vowels = 'aeyuioåøæ'
    outList = []
    for i in inList:
        newStreng = ''
        for j in range(len(i)):
            if i[j] not in vowels:
                newStreng += i[j]

        outList.append(newStreng)

    return outList

#4c)
import random
def randomSequence(listOne, listTwo):
    k = max((len(listOne), len(listTwo)))
    newListOne = []
    newListTwo = []

    while k > 0:
        number = random.randint(0, k-1)

        one = listOne.pop(number)
        two = listTwo.pop(number)
        newListOne.append(one)
        newListTwo.append(two)

        k -= 1


    return newListOne, newListTwo

new, lol = randomSequence([1,2,3,4,5], [5, 3,6 ,8,8])

print(new, lol)

#4d)
def printNewLines(number):
    while number > 0: 
        print('\n')
        number -= 1

#4e)
def playGame(answers, puzzles):
    points = 0
    for i in range(len(puzzles)):
        print('Puzzle word:', puzzles[i])
        answer = input('Guess word? ')
        if answers[i] == answer:
            print('You answered correctly!')
            points += 1
        else: 
            print('You answered incorrectly! The answer should be', answers[i])

    return points

print(playGame(['university'], ['nvrst']))

#4f)
def game():
    print('The NoVowels game')
    print1 = 'Player 2: Look away from screen'
    print('='*len(print1))
    print(print1)
    print('Player 1: Write in a list of English words in lower-case.')

    wordList = enterWords()
    noVowelsList = noVowels(wordList)

    answers, quizzes = randomSequence(wordList, noVowelsList)

    printNewLines(50)

    print('Player 2: Guess words that lack vowels:')

    points = playGame(answers, quizzes)

    print(f'You got {points} of {len(answers)} points.')

game()
