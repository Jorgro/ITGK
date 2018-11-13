x = 'Hei på deg Bob Bernt'
def overordnet():
    visnavn()
    navn()
    siste()
def visnavn():
    print(x)
def siste():
    print(f'Hyggelig å møte deg {x}.')

def navn():
    global x
    x = input('Vent, du heter kanskje ikke Benedicte. Hva er ditt egentlige navn? ')
overordnet()
