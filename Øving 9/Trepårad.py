# Lager 3x3 forskjellige tomme lister, og etterhvert som man krysser av ruter så blir det nye brettet printet med den nye verdien som er append() og "".join(blankliste)
# lag en dictionary inne i en dictonary med tallene 1-9 som keys: så bruker vi baordet som verdier til dict.
#Hvis vi har en en viss kombinasjon av keys blir verdien "won game X/O" returnert.

board = []
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(None)
    board.append(row)
print(board)

def draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                print(' ', end=' ')
            else:
                print(board[i][j], end='')
        print('\n------------')

dictionarywins = {

}
for i in range()
# horizontal
for i in range(3):
    if board[i].count('X') == 3:
        print('Player X won')
    elif board[i].count('O') == 3:
        print('Player O won')
# vertical
vertical = []
for i in range(3):
    for j in range(3):
        vertical.append(board[j][i])
# cross
cross = []
for i in range(3):
    cross.append(board[i][i])

all = [cross, vertical]
for character in 'XO':
    for liste in all:
        if liste.count(character) == 3:
            print(f'Player {character} won')



board[0][0] = 'X'
board[1][1] = 'X'
board[2][2] = 'X'
# wingame(board)
