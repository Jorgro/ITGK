#2a)

def chess_match():
    total_score1 = 0
    total_score2 = 0

    num_games = int(input('Hvor mange partier? '))

    if num_games < 1:
        print('Så kjedelig.')   
    else:
        i = 0
        while num_games > 0: 
            print(f'Parti {i+1}')
            score1 = int(input('Score player 1: '))
            score2 = int(input('Score player 2: '))

            total_score1 += score1
            total_score2 += score2

            i += 1
            num_games -= 1
    
    print('Kampen er slutt.')
    print(f'Spiller 1 fikk {total_score1} poeng\nSpiller 2 fikk {total_score2} poeng.')

    
#2b)
def end_of_match(num_games, game, total_score1, total_score2):
    for i in (total_score1, total_score2):
        x = 1
        if i >= num_games/2 +0.5:
            print(f'Player {x} won the game. ')
            return x
        
        x += 1
    if total_score1 == total_score2 and num_games == game:
        return 3

    if game < num_games: 
        return 0

#2c)
def chess_scorer():
    try:
        points = float(input('Points for one player: '))
    except ValueError:
        print('Umulig resultat')
        return chess_scorer()

    if points == 1: 
        return 0
    elif points == 0.5:
        return 0.5
    elif points == 0:
        return 1
    else:
        print('Umulig resultat')
        return chess_scorer()

print(chess_scorer())

#2d)
def player_score(results):
    return sum([i for i in results if isinstance(i, int) or isinstance(i, float)])

print(player_score([1, 0.5, 0, None]))