from turtle import *
import time
 
# setter opp tegnevinduet
colormode(255)
setup(330, 330, 0, 0)
screensize(315, 315)
goto(-60, 150)
g = input('Angi et tall ')
f = input('Angi et tall ')

Rb = int(g)//256**2


Gb = (int(g)% (256**2))//256



Bb = Gb % 256



Rf = int(f)//256**2


Gf = (int(f)% (256**2))//256



Bf = Gf % 256

# velger farger
bgcolor(Rb, Gb, Bb)
color(Rf, Gf, Bf)
 
#tegner den indre firkanten
begin_fill()
right(10) # tilter den 10 grader nedover
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
end_fill()
  
time.sleep(10)      # Gjør at vinduet med tegningen ikke lukkes med én gang, men er oppe i 10 sekunder
