#4a)

def formatTime(seconds):

    hour = seconds // 3600
    minute = (seconds%3600)//60
    second = seconds %60

    if hour < 10:
        string_hour = '0' + str(hour)
    else:
        string_hour = str(hour)

    if minute < 10:
        string_minute = '0' + str(minute)
    else:
        string_minute = str(minute)

    if second < 10:
        string_second = '0' + str(second)
    else:
        string_second = str(second)

    return f'{string_hour}:{string_minute}:{string_second}'

#4b)

def valuesDecember():
    first = 3*3600+18*60
    period = 12*3600+25*60+12
    return first, period
#4c)

def genTides():
    first, period = valuesDecember()
    lowtides = []
    lowtide = 0
    i = 0

    while lowtide < 31*24*3600:
        lowtide = first + period*i
        if lowtide < 31*24*3600:
            lowtides.append(lowtide)
        i += 1

    hightides = []
    hightide = 0
    j = 0

    while hightide < 31*24*3600:
        first_high = first + period/2
        hightide = first_high + period*j
        if hightide < 31*24*3600:
            hightides.append(int(hightide))

        j+= 1
    return lowtides, hightides
lowtides, hightides = genTides()
print(lowtides[:8])
print(hightides[:8])
#4d)
def genTidesStr(tideList):
    stringTides = []
    for i in tideList:
        days = 1 + i // 86400
        time = formatTime(i%86400)
        stringTides.append(str(days) + " " + time)
    return stringTides
strLows = genTidesStr(lowtides)
#4e)
def checkTides(dayInMonth):
    lowtides, hightides = genTides()

    seconds1 = dayInMonth*86400 + 9*3600
    seconds2 = dayInMonth*86400 + 13*3600

    for i in lowtides:
        if i >= seconds1 and i <= seconds2:
            time = formatTime(i%86400)
            print(f"low tide at {time}")
            exit()

    for i in hightides:
        if i >= seconds1 and i <= seconds2:
            time = formatTime(i%86400)
            print(f"high tide at {time}")
            exit()

    print("no tides")

#4f)

def listTides():
    lowtides, hightides = genTides()

    list_lowtides = [[] for e in range(31)]

    for item in lowtides:
        day = item // 86400
        list_lowtides[day].append(item)
    print("Day".rjust(3) + "First".rjust(7) + "Second".rjust(10))
    for list in list_lowtides:
        print(str(list[0]//86400 +1).rjust(3), end= ' ')
        for item in list:
            print(f'{formatTime(item%86400).rjust(8)}', end=' ')

        print()
listTides()
