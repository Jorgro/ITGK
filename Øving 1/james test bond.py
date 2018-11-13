a = input('Jeg heter: ')
b = a.split()
print(b[1])
c = len(b)
prepfor={'Von', 'Di', 'De', ' Van'}
preplast={'Sr', 'Jr', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'}

if b[c-3] in prepfor and b[c-1] in preplast:
    print(f'The name is {b[c-3]} {b[c-2]}, {a}')

elif b[c-2] in prepfor and c > 2:
    print(f'The name is {b[c-2]} {b[c-1]}, {a}')

elif b[c-1] in preplast:
    print(f'The name is {b[c-2]}, {a}')


else:
    print(f'The name is {b[c-1]}, {a}')
