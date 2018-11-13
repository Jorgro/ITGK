import os
board = []
clear = lambda: os.system('cls')
clear()
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(None)
    board.append(row)


def draw(board):
    print(f'  {1}      {2}     {3} \n--------------------------')
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                print(''.rjust(5), end='| ')
            else:
                print(str(board[i][j]).rjust(5), end='| ')
        print(i+1,'\n--------------------------')

Wintuples = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8],
            [3, 6, 9], [1, 5, 9], [3, 5, 7]]

def wongame(windict, player):
        wincondition = []
        for i in range(len(Wintuples)):
            if set(Wintuples[i]).issubset(windict[player]):
                wincondition.append(True)
        return wincondition
        if True in wincondition:
            print(f'Player {player} won!')


def playerturn(board, players):
    while True:

        for player in ''.join(players):
            clear()
            draw(board)
            possiblecoordinates = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            print(f'Your turn player {player}')
            try:
                x = int(input('x-coordinate: '))
                y = int(input('y-coordinate: '))
                windict[player].append(int(possiblecoordinates[y-1][x-1]))

                if board[y-1][x-1] == None:
                    board[y-1][x-1] = player
                else:
                    print('That slot is already taken.')
                    playerturn(board, players)
                clear()
                draw(board)
                gamedecider = wongame(windict, player)
                if True in gamedecider:
                    print(f'Player {player} won!')
                    exit()

                nonempty = []
                for j in range(len(board)):
                    for i in range(len(board[j])):
                        if board[i][j] == None:
                            nonempty.append(False)

                if False not in nonempty:
                    print(f'No one wins ¯\_(ツ)_/¯')
                    exit()

            except IndexError:
                print('Write cartesian coordinates.')
                playerturn(board, players)
            except ValueError:
                print('Write cartesian coordinates.')
                playerturn(board, players)
draw(board)
player1 = input('What is your character player 1? ')
player2 = input('What is your character player 2? ')
players = [player1, player2]
windict = {player1: [], player2: []}
playerturn(board, players)
