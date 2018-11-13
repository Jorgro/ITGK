import random

print('Welcome to my blackjack game! The stakes are 1 cookie :)')
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 'ess']


def trueblackjack(x):
    if 11 in x and 10 in x:
        return True
    elif 1 in x and 10 in x:
        return True
    elif 11 in x and 10 in x and sum(summation(x)) <= 21:
        return True




def wongame(x, y):
    if sum(summation(x))>21:
        print('Give me my cookie.')

    elif sum(summation(x)) > sum(summation(y)) and sum(summation(y)) < 21:
        print('You won! I owe you one!')
    elif sum(summation(y)) > 21 and sum(summation(x)) < 21:
        print('You won! I owe you one!')
    elif sum(summation(y)) > sum(summation(x)):
        print('Gimme my cookie!')
    elif sum(summation(x)) == sum(summation(y)) and sum(summation(x)) < 21:
        print('Guess we got the same score ¯\_(ツ)_/¯')



def summation(x):

    if 'ess' in x and x.count('ess') == 1:
        x.remove('ess')
        if 21 >= sum(x)+11:
            x.append(11)
        elif sum(x)+11 > 21:
            x.append(1)
    if 'ess' in x and x.count('ess') == 2:
        x.remove('ess')
        x.remove('ess')
        x.append(11)
        x.append(1)
    if 'ess' in x and x.count('ess') == 3:
        x.remove('ess')
        x.remove('ess')
        x.remove('ess')
        x.append(11)
        x.append(1)
        x.append(1)

    return x

def blackjack():

    cards_dealer = []
    card_dealer1 = random.choice(cards)
    card_dealer2 = random.choice(cards)
    # print(card_dealer1)
    # print(card_dealer2)

    cards_dealer.append(card_dealer1)
    cards_dealer.append(card_dealer2)
    dealersum = sum(summation(cards_dealer))

    cards_player = []
    card_player1 = random.choice(cards)
    card_player2 = random.choice(cards)
    cards_player.append(card_player1)
    cards_player.append(card_player2)

    sum(summation(cards_player))
    print(f'Dealers cards are {card_dealer1} and ?')
    print(f'Your score is {sum(summation(cards_player))}')
    # print(card_player1)
    # print(card_player2) #bare sjekket om alt funket riktig
    # print(summation(cards_player))
    anothercard = input('Do you want a new card? Y/N ')
    if anothercard == 'Y':
        card_player3 = random.choice(cards)
        cards_player.append(card_player3)
    if anothercard == 'N':
        if trueblackjack(cards_dealer) == True:
            print('I got blackjack! You owe me!')
        elif trueblackjack(cards_player) == True:
            print('You got blackjack! I owe you!')
        else:
             wongame(cards_player, cards_dealer)
        exit()


    if sum(summation(cards_player)) > 21:
        print('Give me my cookie.')
        exit()

    sum(summation(cards_player))
    print(f'Dealers cards are {card_dealer1} and ?')
    print(f'Your score is {sum(summation(cards_player))}')
    anothercard = input('Do you want a new card? Y/N ')
    if anothercard == 'Y':
        card_player4 = random.choice(cards)
        cards_player.append(card_player4)
        if trueblackjack(cards_dealer) == True:
            print('I got blackjack! You owe me!')
        elif trueblackjack(cards_player) == True and sum(summation(cards_player))<22:
            print('You got blackjack! I owe you!')
        else:
             wongame(cards_player, cards_dealer)
        exit()

    if anothercard == 'N':
        if trueblackjack(cards_dealer) == True:
            print('I got blackjack! You owe me!')
        elif trueblackjack(cards_player) == True:
            print('You got blackjack! I owe you!')
        else:
             wongame(cards_player, cards_dealer)
        exit()
def playagain():
    while True:
        spilligjen = input('Do you wanna play again? Y/N ')
        if spilligjen.lower() == 'Y':
            blackjack()
        if spilligjen.lower() == 'N':
            break
        else:
            print('Fuck you')
            break
# playagain()
blackjack()
