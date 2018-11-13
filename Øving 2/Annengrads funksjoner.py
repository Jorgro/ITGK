a = float(input('Tall for x^2: '))
b = float(input('Tall foran x: '))
c = float(input('Konstant: '))
d = b**2 - 4*a*c
if d < 0: 
    print(f'Andregradslikningen {str(a)}x^2 + {str(b)}x+{str(c)} har to imaginæreløsninger')
elif d > 0: 
    x_1 = (-b+(d)**0.5)/(2*a)
    x_2 = (-b-(d)**0.5)/(2*a)
    print(f'Andregradslikningen {str(a)}x^2 + {str(b)}x+{str(c)} har to reelle løsninger {x_1} og {x_2}')
elif d == 0: 
    x = (-b)/(2*a)
    print(f'Andregradslikningen {str(a)}x^2 + {str(b)}x+{str(c)} har den reelle løsningen {x}')


