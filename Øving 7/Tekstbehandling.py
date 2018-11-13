
def capital(string):
    s = string
    return s.upper().rstrip().lstrip()

print(capital(" \n  The Sky's Awake So I'm Awake   \t "))

def slicer(string, karakter):
        print(string.split(karakter))

slicer("Hakuna Matata", 'a')

def Z():
    for x in range(1, 8):
        print('Z'*x)
    for y in range(6, 0, -1):
        print('Z'*y)
Z()
