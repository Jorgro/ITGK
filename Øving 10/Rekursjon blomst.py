import time
from turtle import *

pensize(2)
pencolor("orange")
bgcolor("green")
fillcolor("blue")
hideturtle()

def halfPetal():
    forward(50)
    left(30)
    forward(75)
    left(30)
    forward(50)
    left(120)

def petal():
    for i in range(2):
        halfPetal()

def flower(num, i=1):
    if i==1:
        begin_fill()
    if num == 1:
        petal()
        exit()
    else:
        petal()
        left(30)
    if i==1:
        end_fill()
    flower(num-1, i=1)
flower(12)

time.sleep(10)
