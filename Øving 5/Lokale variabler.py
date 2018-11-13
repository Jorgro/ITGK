# a) må være kodesnutt 3 siden da brukes ikke funksjonen med error.

x = int(input('x = '))
y = int(input('y = '))
def heltallsdivisjon(x, y):
    num= x//y
    print(f'Heltalls divisjon av {x} over {y} gir {num}')
def kvadrat(x):
    num = x**2
    print(f'Kvadratet av {x} er {num}')
heltallsdivisjon(x, y)
kvadrat(x)
