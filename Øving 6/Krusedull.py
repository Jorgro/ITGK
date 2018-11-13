oddetall = []
import random
import turtle
for i in range(1, 20, 2):
    oddetall.append(i)
print(oddetall)
farger = input('What colours do you want? (10) ')
fargeliste = farger.split(', ')

for i in oddetall:
    farge = random.choice(fargeliste)
    turtle.setposition(0, 0)
    for x in range(41):
        turtle.pencolor(farge)
        turtle.forward(i*len(oddetall))
        turtle.left(123)
