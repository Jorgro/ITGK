
import time
from turtle import *
# importerer funksjoner fra turtle
print("Hei, jeg kan tegne en trekant")
g = input('Ønsker du spissen på trekanten opp eller ned (O / N)? ')
if g == 'N':
    n = -120
elif g == 'O':
    n = 120  

T = '#5cbec9'
R = '#ad208e'
L = '#552988'
B = '#00509e'

k = input('Velg pennefarge, rosa (R) eller turkis (T): ')
if k == 'T':
    pencolor(T)
elif k== 'R':
    pencolor(R)
else:
    print('error')
pensize(7)          # sett pennen 7 piksler tykk
a = input('Velg bakgrunnsfarge, blå (B) eller lilla (L): ')    
if a == 'B':
    bgcolor(B)
elif a == 'L':
    pencolor(L)
else:
    print('error')

b = input('Velg fyllfarge, blå (B) eller rosa (R): ')    
if b == 'B':
    fillcolor(B)
elif b == 'R':
    fillcolor(R)
else:
    print('error')
 
# Tegner en fylt trekant
begin_fill()
forward(200)        # gå 100 piksler framover
left(int(n))         # drei 120 grader venstre
forward(200)  
left(int(n))
forward(200)
end_fill()
  
# Holder vinduet med tegningen åpent i 10 sekunder. Ha dette som siste linje i koden din
time.sleep(10)
