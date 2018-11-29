
#2a) 
def readOneNumber():
    x = int(input('Rad(1-9): '))
    y = int(input('Kolonne(1-9): '))
    number = int(input('Tallet(1-9): '))
    print(f'Posisjon ({x},{y}) innholder nå {number}')


#2b) 
def readPositionDigit(rowNr, colNr, board):
    number = int(input(f'Verdi for posisjon ({rowNr}, {colNr}): '))
    board[rowNr-1][colNr-1] = number
    return board

#print(readPositionDigit(2,3,[[1,0,0],[2,0,0],[3,0,0]]))


#2c) 
def readValidPositionDigit(rowNr, colNr, board):
    while True: 
        try: 
            number = int(input(f'Verdi for posisjon ({rowNr}, {colNr}): '))
            board[rowNr-1][colNr-1] = number
            if number >= 0 and number <= 9:
                return board
            print('Feil! Oppgi et siffer mellom 0 og 9...')

        except ValueError:
            print('Feil! Oppgi et siffer mellom 0 og 9...')

print(readValidPositionDigit(2,3,[[1,0,0],[2,0,0],[3,0,0]]))

#2d) 
def readSudokuBoard():
    board = [[0 for e in range(9)] for e in range(9)]

    for i in range(1, 10):
        for j in range(1, 10):
            readValidPositionDigit(i, j, board)
    return board
print(readSudokuBoard())


