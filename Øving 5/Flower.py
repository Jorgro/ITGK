import time
from turtle import *

pensize(2)              #setter pennen 2 piksler tykk
pencolor("yellow")      #setter pennefargen til lilla
bgcolor("red")       #setter bakgrunnsfargen til gul
hideturtle()            #skjuler pila

def halfPetal():      #lager et halvt blomsterblad
    forward(50)
    left(30)
    forward(75)
    left(30)
    forward(50)
    left(120)

def petal():
    left(60)         #går 60 grader mot venstre hver gang et nytt blad er laget
    for i in range(2): #lager et helt blomsterblad
        halfPetal()

def simpleflower(): #lager en hel blomst
    for y in range(4):
        petal()

def advancedflower():
    for y in range(4):
        left(45)
        simpleflower()

advancedflower()
# Holder vinduet med tegningen åpent i 10 sekunder. Ha dette som siste linje i koden din
time.sleep(5)
