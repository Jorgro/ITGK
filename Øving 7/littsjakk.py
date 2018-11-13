board_string_1 = 'rknPrPp.....P..PP.PPB.K..'
def make_board(string):
    board = []
    board_list = list(string)

    for i in range(1, 6):
        board.append(board_list[5*i-5:5*i:])

    for j in range(5):
        for i in range(5):
            if not board[j][i].isalpha():
                board[j][i] = None
    return board

def get_piece(board, x, y):
    if y <= 5 and y >= 1:
        element = board[-y][x-1]
        return element
    else:
        return '!'

board = make_board(board_string_1)


def get_legal_moves_peasant(board, x, y):
    if get_piece(board, x, y).lower() == 'p':
        piece = get_piece(board, x, y)
        movelist = []
        #for svart
        if ord(piece) < 100:
            if get_piece(board, x, y+1) == None:
                move = (x, y+1)
                movelist.append(move)
                if get_piece(board, x, y+2) == None:
                    move = (x, y+2)
                    movelist.append(move)
            if get_piece(board, x+1, y+1) != None:
                if ord(get_piece(board, x+1, y+1))>100:
                    move = (x+1, y+1)
                    movelist.append(move)
            if get_piece(board, x-1, y+1) != None:
                if ord(get_piece(board, x-1, y+1))>100:
                    move = (x-1, y+1)
                    movelist.append(move)
        #for hvit
        elif ord(piece) > 100:

            if get_piece(board, x, y-1) == None:
                move = (x, y-1)
                movelist.append(move)
                if get_piece(board, x, y-2) == None:
                    move = (x, y-2)
                    movelist.append(move)
            if get_piece(board, x+1, y-1) != None:
                if ord(get_piece(board, x+1, y-1))<100:
                    move = (x+1 , y-1)
                    movelist.append(move)
            if get_piece(board, x-1, y-1) != None:
                if ord(get_piece(board, x-1, y-1))<100:
                    move = (x-1, y-1)
                    movelist.append(move)

        return movelist
    else:
        emptylist = []
        return emptylist

print(board)
print(get_piece(board, 1, 5))
print(get_legal_moves_peasant(board, 1, 4))
print(get_legal_moves_peasant(board, 4, 2))
