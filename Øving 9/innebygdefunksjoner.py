
fruit = {}
fruit['appelsin'] = 0
fruit['banan'] = 5
fruit['eple'] = 2
print(fruit)
del fruit['appelsin']

if 'banan' in fruit:
    del fruit['banan']

print(fruit)

dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }

dict.update(dict2)
print("Value : %s" %  dict)
