#3a)
def throw(n):
    import random

    throws = []

    for i in range(n):
        throws.append(random.randint(1,6))
    return throws

#3b)
def chance(dice):
    sum = 0

    for i in dice:
        sum+=i
    return sum
#3c)
def house(dice):
    set_dice = list(set(dice))

    if dice.count(set_dice[0]) == 2 and dice.count(set_dice[1]) == 3:
        return chance(dice)
    
    if dice.count(set_dice[0]) == 3 and dice.count(set_dice[1]) == 2:
        return chance(dice)

    if len(set_dice) != 2:
        return 0

    return 0

#3d)
def straight(dice):
    truth = True
    for i in dice:
        if dice.count(i) > 1:
            truth = False

    if not truth:
        return 0
    else:
        dice.sort()
        if chance(dice) == 20:
            return 20
        if chance(dice) == 15:
            return(15)
    return 0

import os
import random
print(random.__file__)
