
coordinates = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
              'e': 4, 'f': 5, 'g': 6, 'h': 7}
LegalMovementsCheck = {(0, 5): [(0,6), (4,1)], (4,1):[(0,6)]}
printLegalMovementsCheck = {}

for key in LegalMovementsCheck:
    x_key = [k for k, v in coordinates.items() if v == key[0]]
    print_tuple = (x_key[0], key[1]+1)
    values = []
    for value in LegalMovementsCheck[key]:
        x_value = [k for k, v in coordinates.items() if v == value[0]]
        print_tuple_v = (x_value[0], value[1]+1)
        values.append(print_tuple_v)
    printLegalMovementsCheck[print_tuple] = values


print(printLegalMovementsCheck)
