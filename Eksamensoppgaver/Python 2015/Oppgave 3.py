#3a)
def readTime():
    time = []
    switch = True
    while switch:
        hour = int(input('Enter hour: '))
        if hour >= 0 and hour <= 23:
            switch = False
            time.append(hour)
        else:
            print('Enter a number between 0 and 23.')

    switch = True
    while switch:
        minute = int(input('Enter minute: '))
        if minute >= 0 and minute <= 59:
            switch = False
            time.append(minute)

        else:
            print('Enter a number between 0 and 59.')
    switch = True
    while switch:
        second = int(input('Enter second: '))
        if second >= 0 and second <= 59:
            switch = False
            time.append(second)
        else:
            print('Enter a number between 0 and 59.')
    return time

#3b)
def convertTime(time, mode):
    if mode == 'time':
        list_time = []
        list_time.append(time//3600)
        list_time.append((time%3600)//60)
        list_time.append(time%60)

        return list_time
    if mode == 'sec':
        seconds = 0
        for i in range(len(time)):
            seconds += time[i]*60**(len(time)-i-1)
        return seconds

#3c)
def travelTime():
    print('Give departure time in hour, minute and second:')
    departure = readTime()
    print('Give arrival time in hour, minute and second:')
    switch = True
    while switch:
        arrival = readTime()
        if convertTime(arrival, 'sec') < convertTime(departure, 'sec'):
            print('Error: Arrival time must be later than departure')
        else:
            switch = False

    travel = convertTime(arrival, 'sec') - convertTime(departure, 'sec')
    travel_diff = convertTime(travel, 'time')
    print(f'Traveltime: {travel_diff[0]} hours, {travel_diff[1]} min, {travel_diff[2]} sec')

#3d)
def busTime(BusRoute):
    return convertTime(BusRoute[3:5]+[0],'sec')-convertTime(BusRoute[1:3]+[0],'sec')
def analyzeBusRoutes(BusTables):
    min = 0
    max = 0
    for i in range(1, len(BusTables)):
        start = BusTables[i][1:3]
        stop = BusTables[i][3:]
        time_diff = busTime(BusTables[i])

        time_min = busTime(BusTables[min])
        time_max = busTime(BusTables[max])

        if time_diff < time_min:
            min = i
        elif time_diff > time_max:
            max = i

    time_min = busTime(BusTables[min])
    time_max = busTime(BusTables[max])

    converted_fast = convertTime(time_min, 'time')
    converted_slow = convertTime(time_max, 'time')
    print(f'The slowest bus route is bus nr. {BusTables[max][0]} and it takes {converted_slow[0]} hours, {converted_slow[1]} min.')
    print(f'The slowest bus route is bus nr. {BusTables[min][0]} and it takes {converted_fast[0]} hours, {converted_fast[1]} min.')
Busses = [[1,15,0,15,19],
 [3,15,32,16,45],
 [4,15,45,16,23],
 [5,15,55,16,11]]
analyzeBusRoutes(Busses)
