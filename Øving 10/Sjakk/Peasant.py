class Peasant:
    def __init__(self, x, y, Team):
        self.x = x
        self.y = y
        self.Team = Team

        self.original_y = y #ikke sikkert jeg trenger dersom brettet skal gjøre all bevegelse, da trenger jeg bare
        # å initialisere riktig for å få farge, deretter gjør brettet resten av spillet

    def __repr__(self):
        #nice printer
        colors = {'Black': 'p', 'White': 'P'} #1 er svart, 6 er hvit
        return colors.get(self.Team)

    def Team(self):
        #sjekke hvilket lag brikken er på så brettet slipper det ettersom brikkene vet best
        return self.Team == 'Black'


    def Movement(self, x, y, Brett): #tar inn koordinatene til seg selv
        self.LegalMovesList_Piece = []

        if self.Team == 'Black':
            try:
                if Brett[y+1][x] == '.':
                    self.LegalMovesList_Piece.append((x, y+1))
                    if Brett[y+2][x] == '.' and y == self.original_y:
                        self.LegalMovesList_Piece.append((x, y+2))
            except:
                pass
            try:
                if ord(repr(Brett[y+1][x+1])) < 96 and Brett[y+1][x+1] != '.':
                    self.LegalMovesList_Piece.append((x+1, y+1))
            except:
                pass
            try:
                if ord(repr(Brett[y+1][x-1])) < 96 and Brett[y+1][x-1] != '.':
                    self.LegalMovesList_Piece.append((x-1, y+1))
            except:
                pass

        if self.Team == 'White':
            try:
                if Brett[y-1][x] == '.':
                    self.LegalMovesList_Piece.append((x, y-1))
                    if Brett[y-2][x] == '.' and y == self.original_y:
                        self.LegalMovesList_Piece.append((x, y-2))
            except:
                pass
            try:
                if ord(repr(Brett[y-1][x+1])) > 96 and Brett[y-1][x+1] != '.':
                    self.LegalMovesList_Piece.append((x+1, y-1))
            except:
                pass
            try:
                if ord(repr(Brett[y-1][x-1])) > 96 and Brett[y-1][x-1] != '.':
                    self.LegalMovesList_Piece.append((x-1, y-1))
            except:
                pass
        return self.LegalMovesList_Piece


    def Upgrade(self):
        #når den kommer over brettet, avhengig av team
        pass

class Rook:
    def __init__(self, x, y, Team):
        self.x = x
        self.y = y
        self.Team =  Team
        self.original_y = y #ikke sikkert jeg trenger dersom brettet skal gjøre all bevegelse, da trenger jeg bare
        # å initialisere riktig for å få farge, deretter gjør brettet resten av spillet

    def __repr__(self):
        #nice printer
        colors = {'Black': 'r', 'White': 'R'} #1 er svart, 6 er hvit
        return colors.get(self.Team)

    def Team(self):
        #sjekke hvilket lag brikken er på så brettet slipper det ettersom brikkene vet best
        return self.Team == 'Black'

    def Movement(self, x, y, Brett): #tar inn koordinatene til seg selv
        self.LegalMovesList_Piece = []
        #x+ retning:

        for i in range(1, 9):
            try:
                if Brett[y][x+i] == '.':
                    self.LegalMovesList_Piece.append((x+i, y))
                elif Brett[y][x+i].Team != self.Team:
                    self.LegalMovesList_Piece.append((x+i, y))
                    break
                elif Brett[y][x+i].Team == self.Team:
                    break
            except:
                break
        #x- retning
        for i in range(1, 9):
            try:
                if Brett[y][x-i] == '.':
                    self.LegalMovesList_Piece.append((x-i, y))
                elif Brett[y][x-i].Team != self.Team:
                    self.LegalMovesList_Piece.append((x-i, y))
                    break
                elif Brett[y][x-i].Team == self.Team:
                    break
            except:
                break
        #y+ retning:
        for i in range(1, 9):
            try:
                if Brett[y+i][x] == '.':
                    self.LegalMovesList_Piece.append((x, y+i))
                elif Brett[y+i][x].Team != self.Team:
                    self.LegalMovesList_Piece.append((x, y+i))
                    break
                elif Brett[y+i][x].Team == self.Team:
                    break
            except:
                break
        #y- retning:
        for i in range(1, 9):
            try:
                if Brett[y-i][x] == '.':
                    self.LegalMovesList_Piece.append((x, y-i))
                elif Brett[y-i][x].Team != self.Team:
                    self.LegalMovesList_Piece.append((x, y-i))
                    break
                elif Brett[y-i][x].Team == self.Team:
                    break
            except:
                break
        # for i in range(1, 3):
        #     if Brett[y+i][x] == '.':
        #         self.LegalMovesList_Piece.append((x, y+i))

        return self.LegalMovesList_Piece

class Knight:
    def __init__(self, x, y, Team):
        self.x = x
        self.y = y
        self.Team = Team

        self.original_y = y #ikke sikkert jeg trenger dersom brettet skal gjøre all bevegelse, da trenger jeg bare
        # å initialisere riktig for å få farge, deretter gjør brettet resten av spillet

    def __repr__(self):
        #nice printer
        colors = {'Black': 'h', 'White': 'H'} #0 er svart, 7 er hvit
        return colors.get(self.Team)

    def Team(self):
        #sjekke hvilket lag brikken er på så brettet slipper det ettersom brikkene vet best
        return self.Team == 'Black'


    def Movement(self, x, y, Brett):
        self.LegalMovesList_Piece = []

        for i in [-2, 2]:
            for j in [-1, 1]:

                try:
                    if Brett[y+j][x+i] == '.':
                        self.LegalMovesList_Piece.append((x+i, y+j))
                    elif Brett[y+j][x+i].Team != self.Team:
                        self.LegalMovesList_Piece.append((x+i, y+j))
                except:
                    pass

                try:
                    if Brett[y+i][x+j] == '.':
                        self.LegalMovesList_Piece.append((x+j, y+i))
                    elif Brett[y+i][x+j].Team != self.Team:
                        self.LegalMovesList_Piece.append((x+j, y+i))
                except:
                    pass


        return self.LegalMovesList_Piece


class Springer:
    def __init__(self, x, y, Team):
        self.x = x
        self.y = y
        self.Team = Team

        self.original_y = y #ikke sikkert jeg trenger dersom brettet skal gjøre all bevegelse, da trenger jeg bare
        # å initialisere riktig for å få farge, deretter gjør brettet resten av spillet

    def __repr__(self):
        #nice printer
        colors = {'Black': 'b', 'White': 'B'} #1 er svart, 6 er hvit
        return colors.get(self.Team)

    def Team(self):
        #sjekke hvilket lag brikken er på så brettet slipper det ettersom brikkene vet best
        return self.Team == 'Black'

    def Movement(self, x, y, Brett):
        self.LegalMovesList_Piece = []
        #4 for løkker i hver retning:
        #skrått nedover mot høyre
        for i in range(1, 9):
            try:
                if Brett[y+i][x+i] == '.':
                    self.LegalMovesList_Piece.append((x+i, y+i))
                elif Brett[y+i][x+i].Team != self.Team:
                    self.LegalMovesList_Piece.append((x+i, y+i))
                    break
                elif Brett[y+i][x+i].Team == self.Team:
                    break
            except:
                break
        #skrått nedover mot venstre
        for i in range(1, 9):
            try:
                if Brett[y+i][x-i] == '.':
                    self.LegalMovesList_Piece.append((x-i, y+i))
                elif Brett[y+i][x-i].Team != self.Team:
                    self.LegalMovesList_Piece.append((x-i, y+i))
                    break
                elif Brett[y+i][x-i].Team == self.Team:
                    break
            except:
                break
        #skrått oppover mot høyre
        for i in range(1, 9):
            try:
                if Brett[y-i][x+i] == '.':
                    self.LegalMovesList_Piece.append((x+i, y-i))
                elif Brett[y-i][x+i].Team != self.Team:
                    self.LegalMovesList_Piece.append((x+i, y-i))
                    break
                elif Brett[y-i][x+i].Team == self.Team:
                    break
            except:
                break
        #skrått oppover mot venstre
        for i in range(1, 9):
            try:
                if Brett[y-i][x-i] == '.':
                    self.LegalMovesList_Piece.append((x-i, y-i))
                elif Brett[y-i][x-i].Team != self.Team:
                    self.LegalMovesList_Piece.append((x-i, y-i))
                    break
                elif Brett[y-i][x-i].Team == self.Team:
                    break
            except:
                break
        return self.LegalMovesList_Piece

class Queen:
    def __init__(self, x, y, Team):
        self.x = x
        self.y = y
        self.Team = Team
        self.original_y = y #ikke sikkert jeg trenger dersom brettet skal gjøre all bevegelse, da trenger jeg bare
        # å initialisere riktig for å få farge, deretter gjør brettet resten av spillet

    def __repr__(self):
        #nice printer
        colors = {'Black': 'q', 'White': 'Q'} #1 er svart, 6 er hvit
        return colors.get(self.Team)

    def Team(self): #ubrukelig, lagret i en klassevariabel
        #sjekke hvilket lag brikken er på så brettet slipper det ettersom brikkene vet best
        return self.Team == 'Black'



    def Movement(self, x, y, Brett):

        copy_Board = [e for e in Brett]

        copy_Board[y][x] = Rook(x, y, self.Team)
        self.LegalMovesList_Piece = copy_Board[y][x].Movement(x, y, Brett)

        copy_Board[y][x] = Springer(x, y, self.Team)
        self.Springer = copy_Board[y][x].Movement(x, y, Brett)

        for tuple in self.Springer:
            self.LegalMovesList_Piece.append(tuple)
        Brett[y][x] = Queen(x, y, self.Team)
        #skjer noe feil med initialiseringen, repr kan ikke hente ut en string siden original y endres, static?
        return self.LegalMovesList_Piece
        #trenger vel bare å legge sammen listene til løperen og tårnet som er på dronningens plass?

class King:
    def __init__(self, x, y, Team):
        self.x = x
        self.y = y
        self.Team = Team
        self.original_y = y #ikke sikkert jeg trenger dersom brettet skal gjøre all bevegelse, da trenger jeg bare
        # å initialisere riktig for å få farge, deretter gjør brettet resten av spillet

    def __repr__(self):
        #nice printer
        colors = {'Black': 'k', 'White': 'K'} #1 er svart, 6 er hvit
        return colors.get(self.Team)

    def Team(self):
        #sjekke hvilket lag brikken er på så brettet slipper det ettersom brikkene vet best
        return self.Team == 'Black'

    def Movement(self, x, y, Brett):
        self.LegalMovesList_Piece = []
        #sjekker alle naboer og legger til i listen
        for i in range(-1, 2):
            for j in range(-1, 2):
                Nx = x+i
                Ny = y+j
                try:
                    if not (Nx == x and Ny == y):

                        if Brett[Ny][Nx] == '.':
                            self.LegalMovesList_Piece.append((Nx, Ny))
                        elif Brett[Ny][Nx].Team != self.Team:
                            self.LegalMovesList_Piece.append((Nx, Ny))
                except:
                    pass
        return self.LegalMovesList_Piece
