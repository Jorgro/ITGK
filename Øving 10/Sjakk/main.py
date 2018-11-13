from Board import Board
import time
brett = Board()
coordinates = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
          'e': 4, 'f': 5, 'g': 6, 'h': 7}
def main():
    try:
        players = ['White', 'Black']
        print('Welcome to my chessgame. In order to stop the game hit Ctrl-C after blacks turn.')
        time.sleep(3)
        for player in players:
                brett.printBoard()
                print(f"Player {player}'s turn.")
                if brett.Check(player):
                    trekk = brett.CheckLegalMove(player, brett)
                    if not trekk:
                        print(f'{players[players.index(player)-1]} won! Better "luck" next time {player}.')
                        exit()
                    else:
                        print(f'{player} king in check!\nThink carefully about which'
                            ' piece to move.')
                        check_input = False
                        while not check_input:
                            try:
                                user_input = input('Choose coordinate to move: ')
                                x, y = user_input[0], int(user_input[1])
                                if len(x) > 1 or len(x) < 0 or x.isnumeric():
                                    print('Write in real coordinates')
                                else:
                                    Move_x = coordinates.get(x)
                                    Move_y = y - 1
                                    if brett._Brett[Move_y][Move_x] == '.' or brett._Brett[Move_y][Move_x].Team != player:
                                        print('This is not a piece you can move.')
                                    elif (Move_x, Move_y) not in trekk:
                                        print('This is an illegal move.')
                                    else:
                                        user_input_2 = input('Move to letter-coordinate: ')
                                        x_2, y_2 = user_input_2[0], int(user_input_2[1])

                                        Move_x_2 = coordinates.get(x_2)
                                        Move_y_2 = y_2 - 1
                                        if (Move_x_2, Move_y_2) not in trekk[(Move_x, Move_y)]:
                                            print('This is an illegal move.')
                                        else:
                                            brett.x = Move_x
                                            brett.y = Move_y
                                            brett.LegalMovesList = trekk[(Move_x, Move_y)]
                                            brett.movePiece(brett.LegalMovesList.index((Move_x_2, Move_y_2)))
                                            break
                            except:
                                print('Write in real coordinates')



                else:
                    print(f'{player} king is not in check')
                    check_input = False
                    while not check_input:
                        try:
                            user_input = input('Choose coordinate to move: ')
                            x, y = user_input[0], int(user_input[1])

                            Move_x = coordinates.get(x)
                            Move_y = y - 1
                            if brett._Brett[Move_y][Move_x] == '.' or brett._Brett[Move_y][Move_x].Team != player:
                                print('This is not a piece you can move.')
                            else:
                                trekk = brett.LegalMoves(x, y, player)
                                if not trekk:
                                    print("This piece can't move anywhere.")
                                else:
                                    user_input_2 = input('Move to letter-coordinate: ')
                                    Move_x, Move_y = user_input_2[0], int(user_input_2[1])

                                    Move_x_2 = coordinates.get(Move_x)
                                    Move_y_2 = Move_y - 1
                                    if (Move_x_2, Move_y_2) not in trekk:
                                        print('This move is not allowed.')
                                    else:
                                        brett.movePiece(trekk.index((Move_x_2, Move_y_2)))
                                        brett.Upgrade_Peasant(Move_x_2, Move_y_2)
                                        check_input = True

                        except:
                            print('Write in real coordinates.')
        main()

    except KeyboardInterrupt:
        print('You ended the game before a winner was decided.')


if __name__ == "__main__":
    main()
