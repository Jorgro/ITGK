def winnings3(x, y):
    prizes = {
        (7, False or True) : 2749450,
        (6, True ) : 102110,
        (6, False) : 3380,
        (5, False or True) : 90,
        (4, True ) : 40
    }
    return prizes.get((x, y >= 1), -5)
print(winnings3(7, 1))
