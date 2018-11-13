import random
class Card:
    Cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 'ess']
    def __init__(self):
        self._card = random.choice(Card.Cards)
class Dealer:
    def __init__(self):
        self._dealer = [Card()._card for i in range(2)]
        if self._dealer.count('ess') == 2:
            self._dealer = [11, 1]
        else:
            for i in range(2):
                if self._dealer[i] == 'ess':
                    self._dealer[i] = 11
        print(self._dealer)
class Player:
    def __init__(self):
        self.player = [Card()._card for i in range(2)]
        if self.player.count('ess') == 2:
            self.player = [11, 1]
        else:
            for i in range(2):
                if self.player[i] == 'ess':
                    self.player[i] = 11
        print(self.player)
    def trekk_Player(self):
        self._sum = sum(self.player)
        self.player.append(Card()._card)
        if 'ess' in self.player:
            if self._sum + 11 <= 21 and self.player[-1] == 'ess':
                self.player[-1] = 11
            else:
                self.player[-1] = 1

class Blackjack(Player, Dealer):
    def __init__(self):
        print('Hei, nå skal vi spille blackjack')
        self.dealer = Dealer()._dealer
        self.player = Player().player
        print(f'Dealers cards are {self.dealer[1]} and ?, your sum is {sum(self.player)}')

    def vinnkondisjoner(self):
        pass

Blackjack = Blackjack()
def main():
    trekk = input('Vil du gjøre et nytt trekk? Isåfall skriv "Ja". ')
    if trekk == 'Ja':
        Blackjack.trekk_Player()
        print(sum(Blackjack.player))

    trekk = input('Vil du gjøre et nytt trekk? Isåfall skriv "Ja". ')
    if trekk == 'Ja':
        Blackjack.trekk_Player()
        print(sum(Blackjack.player))
main()
