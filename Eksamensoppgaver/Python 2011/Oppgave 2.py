#2a)
def edgeLength(x1, y1, x2, y2):
    length = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    return length

#2b)
def circumference(coordinates):
    if len(coordinates)%2 == 1 or not coordinates:
        return -1
    
    if len(coordinates) == 2:
        return 0
    
    if len(coordinates) == 4:
        return 2*edgeLength(coordinates[0],coordinates[1],coordinates[2],coordinates[3])
    circumference = 0
    for i in range(0, len(coordinates), 2):
        if i == len(coordinates)-2:
            circumference += edgeLength(coordinates[i], coordinates[i+1], coordinates[0], coordinates[1])
        else:
            circumference += edgeLength(coordinates[i], 
                            coordinates[i+1], coordinates[i+2], coordinates[i+3])
    
    return circumference

print(circumference([3, 1, 5, 4, 4, 5, 2, 4, 1, 2]))

#2c)
def enclosingRectangle(pList):
    max_x = pList[0]
    min_x = pList[0]

    max_y = pList[1]
    min_y = pList[1]
    for i in range(0, len(pList), 2):
        if pList[i] > max_x:
            max_x = pList[i]
        elif pList[i] < min_x:
            min_x = pList[i]
    
    for i in range(1, len(pList), 2):
        if pList[i] > max_y:
            max_y = pList[i]
        elif pList[i] < min_y:
            min_y = pList[i]
    
    return [min_x, min_y, max_x, max_y]

print(enclosingRectangle([3, 1, 5, 4, 4, 5, 2, 4, 1, 2]))

#2d)
def readPolygonFile(filename):
    polygon = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.split()
            
            for i in line:
                i = i.rstrip('\n')
                i = i.strip()
                polygon.append(int(i))
    return polygon

