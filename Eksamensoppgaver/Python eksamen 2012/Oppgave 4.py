#4a)
def cold_days(templist):
    i = 0
    for j in templist:
        if j < 0:
            i+= 1

    return i
days = cold_days([1,-5,3,0,-6,-3,15,0])

#4b)
def cap_data(array, min_value, max_value):
    result = []
    for i in array:
        if i < min_value:
            result.append(min_value)
        elif i > max_value:
            result.append(max_value)
        else:
            result.append(i)
    
    return result
A = [-70,30,0,90,23,-12,95,12]
print(cap_data(A, -50, 50))


#4c)
def generate_testdata(N, min_value, max_value):
    import random
    result = []
    while len(result) < N:
        k = random.randint(min_value, max_value)
        if k not in result:
            result.append(k)
    return result
print(generate_testdata(10,-5,10))

#4d)
def create_db(temp, rain, humidity, wind):

    weather = {}
    for i in range(len(temp)):
        weather[i+1] = [temp[i], rain[i], humidity[i], wind[i]]

    return weather

temp = [1,5,3]
rain = [0,30,120]
humidity = [30,50,65]
wind = [3,5,7]
weather = create_db(temp, rain, humidity, wind)

#4e)
def print_db(weather):

    print('Day | Temp | rain | humidity | wind')
    print('====+======+======+==========+======')
    
    for key, value in weather.items():
        streng = str(key).rjust(4) + str(value[0]).rjust(7) + str(value[1]).rjust(7) + str(value[2]).rjust(11) + str(value[0]).rjust(7)
        print(streng)

print_db(weather)

#4f)
def strange_weather(temp, rain):
    possible = []

    for i in range(len(temp)):
        start = i 
        k = i
        if k < len(temp) - 1:
            while temp[k+1] < temp[k] and rain[k+1] > rain[k]:
                if k < len(temp) - 2: 
                    k += 1

        if start != k: 
            possible.append((start, k))
    best = 0
    if possible:
        for i in range(1, len(possible)):
            if possible[i][1] - possible[i][0] > possible[best][1] - possible[best][0]:
                best = i

        start = possible[best][0] + 1
        stop = possible[best][1] +1
        return (start, stop)
    else:
        return (0, 0)

temp=[1, 3, 4,-5,-6,-7,-8,-9,3,0]
rain=[0,20,30, 0,10,30,50, 0,5,2]

(start, stop) = strange_weather(temp, rain)
print(start, stop)