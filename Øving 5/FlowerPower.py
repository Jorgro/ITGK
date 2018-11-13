
import time
from turtle import *


pensize(2)              #setter pennen 2 piksler tykk
pencolor("purple")      #setter pennefargen til lilla
bgcolor("yellow")       #setter bakgrunnsfargen til gul
hideturtle()            #skjuler pila
x = 1
def halfPetal(x):        #lager et halvt blomsterblad
    forward(50*x)
    left(30)
    forward(75*x)
    left(30)
    forward(50*x)
    left(120)
    x = x +1


def petal(x):            #lager et helt blomsterblad
    for i in range(2):
        halfPetal(x)
def blomsten():
    for y in range(1,7):
        petal(x)


blomsten()


# Holder vinduet med tegningen åpent i 10 sekunder. Ha dette som siste linje i koden din
time.sleep(10)
