a = input('Høyde? ')

b = 3* int(a)/ 6**0.5

c = 3**0.5 * b**2
print(round(c, 2))

d = 2**0.5 * b**3 /12
print(round(d, 2))

print(f'Et tetraheder med høyde {a} har volum {round(d, 2)} og areal {round(c, 2)}.')

