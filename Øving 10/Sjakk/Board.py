from Peasant import Peasant, Rook, Queen, King, Knight, Springer
import copy

class Board:

    def __init__(self):
        self._Brett = [['.']*8 for _ in range(8)]
        self.fillPieces()

    def __repr__(self):
        return f'{self._Brett}'
        #for developers

    def printBoard(self):
        #printer ut en fin versjon av brettet til skjermen og refresher skjermen
        print('\n'*100)
        self.k = 1
        print('\na b c d e f g h')
        for i in self._Brett:
            for j in i:
                if j != '.':
                    print(repr(j), end=' ')
                else:
                    print(j, end=' ')
            print(self.k)
            self.k+=1


    def fillPieces(self):

        #peasant
        for i in range(len(self._Brett[1])):
            self._Brett[1][i] = Peasant(i, 1, 'Black')

        for i in range(len(self._Brett[6])):
            self._Brett[6][i] = Peasant(i, 6, 'White')
        #bør nok gi brikkene et team parameter
        #rook
        self._Brett[0][0], self._Brett[0][7] = Rook(0, 0, 'Black'), Rook(7, 0, 'Black')
        self._Brett[7][0], self._Brett[7][7] = Rook(0, 7, 'White'), Rook(7, 7, 'White')

        #knight
        self._Brett[0][1], self._Brett[0][6] = Knight(1, 0, 'Black'), Knight(6, 0, 'Black')
        self._Brett[7][1], self._Brett[7][6] = Knight(1, 7, 'White'), Knight(6, 7, 'White')

        #springer
        self._Brett[0][2], self._Brett[0][5] = Springer(2, 0, 'Black'), Springer(5, 0, 'Black')
        self._Brett[7][2], self._Brett[7][5] = Springer(2, 7, 'White'), Springer(5, 7, 'White')

        #queen
        self._Brett[0][4], self._Brett[7][4] = Queen(4, 0, 'Black'), Queen(4, 7, 'White')

        #king
        self._Brett[0][3], self._Brett[7][3] = King(3, 0, 'Black'), King(3, 7, 'White')

    def movePiece(self, user_input):

        try:
            #henter ut tuple
            self.to_x = self.LegalMovesList[user_input][0]
            self.to_y = self.LegalMovesList[user_input][1]
            #bytter plass
            self._Brett[self.to_y][self.to_x] = self._Brett[self.y][self.x]
            self._Brett[self.y][self.x] = '.'



        except IndexError:
            pass
        #beveger brikke fra getPosition til (x, y)
        # her skal bare selve bevegelsen være, utregningene gjøres i LegalMove


    def Check(self, Team):
        #finner kongen til laget:
        for i in range(8):
            for j in range(8):
                if isinstance(self._Brett[i][j], King) and self._Brett[i][j].Team == Team:
                    self.King = (j, i)

        #hente ut alle mulige angrep fra motstanderen og sammenligne:
        self.allLegalMoves = []
        for i in range(8):
            for j in range(8):
                if self._Brett[i][j] != '.':
                    if self._Brett[i][j].Team != Team:
                        self.LegalMoveCheck = self._Brett[i][j].Movement(j, i, self._Brett)
                        for tuple in self.LegalMoveCheck:
                            self.allLegalMoves.append(tuple)

        if self.King in self.allLegalMoves:
            return True
        return False

    def LegalMoves(self, from_x, from_y, Team):
        coordinates = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                      'e': 4, 'f': 5, 'g': 6, 'h': 7}
        #henter ut koordinatene på riktig form for listen self._Brett, kanskje gi dette til en annen funksjon for interface
        self.x = coordinates.get(from_x)
        self.y = from_y - 1

        #sjekker om veien er blokkert av fiendebrikker/egne brikker? for tårn/dronning/løper kan dette bli mange moves, noen løsning?
        #kanskje brikken har en funksjon med alle moves som returneres hit, og getPosition gir objektet koordinatene?
        self.LegalMovesList = []
        self.LegalMovesList = self._Brett[self.y][self.x].Movement(self.x, self.y, self._Brett)
        if self.LegalMovesList:
            self.LegalMovesList = [e for e in self.LegalMovesList if (e[1]>-1 and e[0]>-1)]
        #finner kongen til motstanderen
        for i in range(8):
            for j in range(8):
                if isinstance(self._Brett[i][j], King) and self._Brett[i][j].Team != self._Brett[self.y][self.x].Team:
                    self.King_2 = (j, i)
        #fjerner kongen fra angrepslisten siden kongen er immun
        if self.King_2 in self.LegalMovesList:
            self.LegalMovesList.remove(self.King_2)

        self.illegalMoves = []

        for tuple in self.LegalMovesList:
            copied_board_2 = Board()
            copied_board_2._Brett = copy.deepcopy(self._Brett)
            copied_board_2.x = self.x
            copied_board_2.y = self.y
            copied_board_2.LegalMovesList = self.LegalMovesList
            copied_board_2.movePiece(copied_board_2.LegalMovesList.index(tuple))

            if copied_board_2.Check(Team):
                self.illegalMoves.append(tuple)

        self.LegalMovesList = [e for e in self.LegalMovesList if e not in self.illegalMoves]


        return self.LegalMovesList

    def CheckLegalMove(self, Team, board):
        coordinates = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                      'e': 4, 'f': 5, 'g': 6, 'h': 7}



        self.LegalMovementsCheck = {}
        for i in range(8):
            for j in range(8):
                copied_board = Board()
                copied_board._Brett = copy.deepcopy(board._Brett)
                # print(repr(copied_board))
                copied_board.x = j
                copied_board.y = i
                if copied_board._Brett[i][j] != '.':
                    if copied_board._Brett[i][j].Team == Team:

                        self.Piece = copied_board._Brett[i][j].Movement(j, i, copied_board._Brett)

                        if self.Piece:
                            self.Piece = [e for e in self.Piece if (e[1]>-1 and e[0]>-1)]

                        for k in range(8):
                            for m in range(8):
                                if (isinstance(copied_board._Brett[k][m], King) and
                                copied_board._Brett[k][m].Team != copied_board._Brett[i][j].Team):
                                    self.King_2 = (m, k)

                        if self.King_2 in self.Piece:
                            self.Piece.remove(self.King_2)

                        #genial løsning
                        if len(self.Piece)>0:
                            self.tuple_list = []
                            for tuple in self.Piece:
                                copied_board_2 = Board()
                                copied_board_2._Brett = copy.deepcopy(board._Brett)
                                copied_board_2.x = j
                                copied_board_2.y = i
                                copied_board_2.LegalMovesList = self.Piece
                                copied_board_2.movePiece(self.Piece.index(tuple))

                                if not copied_board_2.Check(Team):
                                    self.tuple_list.append(tuple)
                                    # self.LegalMovementsCheck[(j, i)] = self.Piece[self.Piece.index(tuple)]
                                    self.LegalMovementsCheck[(j, i)] = self.tuple_list

        return self.LegalMovementsCheck

    def Upgrade_Peasant(self, x, y):

        if (y == 7 and self._Brett[y][x].Team == 'Black'
            and isinstance(self._Brett[y][x], Peasant)):
            choose_upgrade = input('Choose between Queen (Q) and Horse(H): ')
            if choose_upgrade == 'Q':
                self._Brett[y][x] = Queen(x, y, 'Black')
            if choose_upgrade == 'H':
                self._Brett[y][x] = Knight(x, y, 'Black')

        if (y == 0 and self._Brett[y][x].Team == 'White'
            and isinstance(self._Brett[y][x], Peasant)):
            choose_upgrade = input('Choose between Queen (Q) and Horse(H): ')
            if choose_upgrade == 'Q':
                self._Brett[y][x] = Queen(x, y, 'White')
            if choose_upgrade == 'H':
                self._Brett[y][x] = Knight(x, y, 'White')
