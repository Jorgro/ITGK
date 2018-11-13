import random

numbers = []
for number in range(1, 35):
    numbers.append(number)

myguess = [1, 2, 3, 4, 5, 6, 7]
tilleggstall = [11, 12, 13]

def drawnumbers(n, numbers):
    solution = []

    for x in range(n):
        k = random.choice(numbers)
        solution.append(k)


    return solution




def complist(solution, yourguess):
    points = []
    for x in range(0, len(yourguess)):
        if yourguess[x] in solution:
            points.append(1)
    return sum(points)


# moneyearn = [-50, -50, -50, -50, -50, 90, 3380, 2749450]
# extramoney = [40, 102110]
# def winnings(x, y):
#     if y >= 1 and x>=4 and x%2 == 0:
#         winnings = extramoney[x//2 - 2]
#         return winnings
#     else:
#         winnings = moneyearn[x]
#         return winnings

def winnings3(x, y):
    prizes = {
        (7, False or True) : 2749450,
        (6, True ) : 102110,
        (6, False) : 3380,
        (5, False or True) : 90,
        (4, True ) : 40
    }
    return prizes.get((x, y >= 1), -10)




def mainlotto():
    draw1 = drawnumbers(10, numbers)
    draw2 = draw1[7:]

    moneygained = winnings3(complist(draw1, myguess), complist(draw2, tilleggstall))
    return moneygained

# print(mainlotto())

totalsum = []
for x in range(10000):
    totalsum.append(mainlotto())

if sum(totalsum) < 0:
    print(f' Du har totalt tapt {-sum(totalsum)}kr på å spille lotto')
else:
    print(f' Du har totalt vunnet {sum(totalsum)}kr på å spille lotto')
