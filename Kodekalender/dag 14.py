with open('input-bounding-crisscross.txt', 'r') as file:
    data = file.read()
board = [['x']]
x, y = 0, 0
dict_mov = {'F': 0,'B': 0, 'V': 0, 'H': 0}
for i in range(0, len(data)-1, 2):
    dict_mov[data[i+1]] += int(data[i])
print(dict_mov)

#board = [['' for e in range(20)] for j in range(20)]
x, y  = 0, 0
min_x = 0
max_x = 0
min_y = 0
max_y = 0

for i in range(0, len(data)-1, 2):
    if data[i+1] == 'F':
        y += int(data[i])
        if y > max_y:
            max_y = y
    elif data[i+1] == 'B':
        y -= int(data[i])
        if y < min_y:
            min_y = y
    elif data[i+1] == 'V':
        x -= int(data[i])
        if x < min_x:
            min_x = x
    elif data[i+1] == 'H':
        x += int(data[i])
        if x > max_x:
            max_x = x
    #print(x, y)
print(max_x, min_x)
print(max_y, min_y)

board = [[' ' for e in range(113)] for j in range(144)]

x, y = 45, 23


for i in range(0, len(data)-1, 2):
    #print('hey')
    #print(board)
    if data[i+1] == 'F':
        for j in range(int(data[i])):
            y += 1
            board[y][x] = 'x'
            #print(board[y][x])
    elif data[i+1] == 'B':
        for j in range(int(data[i])):
            y -= 1
            board[y][x] = 'x'
    elif data[i+1] == 'V':
        for j in range(int(data[i])):
            x -= 1
            board[y][x] = 'x'
    elif data[i+1] == 'H':
        for j in range(int(data[i])):
            x += 1
            board[y][x] = 'x'
counter = 0
empty = 0
for j in board:
    for i in j:
        if i == 'x':
            counter+= 1
        else: 
            empty += 1
        #print(i, end='')

    #print()

print(counter/empty)



#finne max, min av x,y til slutt så vi kan finne selve boksen


    