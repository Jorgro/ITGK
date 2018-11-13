a = input('How many cookies? ')
b = input('How many cookies? ')
c = input('How many cookies? ')

abc = [a, b, c]
print( 'Antall'.rjust(11) + 'sukker(g)'.rjust(12)+'sjokolade(g)'.rjust(13))
for x in abc:
    sukker = 200*int(x)/24
    sjokolade = 250*int(x)/24
    print(x.rjust(10) + str(sukker).rjust(10)+str(sjokolade).rjust(10))
