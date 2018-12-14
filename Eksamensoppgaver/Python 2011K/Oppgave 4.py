#4a)
import random
def random_picture(size):
    pict = []
    for i in range(size):
        temp = []
        for j in range(size):
            temp.append(random.randint(0, 255))
        pict.append(temp)

    return pict

print(random_picture(5))
#4b)
def test_picture(table):
    
    for i in table:
        if len(i) != len(table):
            return False

        for j in range(len(i)):
            if i[j] > 255 or i[j] < 0:
                return False

    return True

#4c)
def filter_black_and_white(table, treshold):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] < treshold:
                table[i][j] = 0
            else:
                table[i][j] = 255

    return table

#4d)
def filter_inverse(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            temp = table[i][j]
            table[i][j] = 255-temp
    return table

#4e)
def histogram(table):
    values = [0 for e in range(255)]
    
    for i in range(len(table)):
        for j in range(len(table[i])):
            values[table[i][j]+1] += 1
    dict_values = {}
    for i in range(len(values)):
        if values[i] != 0:
            dict_values[i] = values[i]
    return dict_values

table = random_picture(2)
print(table)
print(histogram(table))

#4f)
def main():
    table = random_picture(10)

    if not test_picture(table):
        return

    table = filter_inverse(table)
    histo = histogram(table)

    for key, value in histo.items():
        print(f'{key}: {value}')
    
    table = filter_black_and_white(table, 100)

    for i in table:
        for j in i:
            print(j, end=' ')
        print()

main()





            