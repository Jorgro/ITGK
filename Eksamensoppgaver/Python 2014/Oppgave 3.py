#3a)
weatherData = [[12.0, 2.4, 8.2],
[6.1, 0.6, 11.9],
[8.3, -3.5, 0.0],
[11.6, -5.2, 0.0],
[15.3, 2.8, 14.3]
]
def weatherStats(weatherData):
    max = 0
    min = 0
    total = 0
    for i in range(1, len(weatherData)):
        if weatherData[i][0] > weatherData[max][0]:
            max = i
        if weatherData[i][1] < weatherData[min][1]:
            min = i
        total += weatherData[i][2]
    total += weatherData[0][2]

    print(f'There are {len(weatherData)} days in the period.')
    print(f'The highest temperature was {weatherData[max][0]} C on day number {max+1}')
    print(f'The lowers temperature was {weatherData[min][1]} C on day number {min+1}')
    print(f'There was a total of {round(total,1)} mm rain in the period')

#3b)
def coldestThreeDays(weatherData):

    min = 0
    for i in range(1, len(weatherData)-2):
        minimum_temp = (weatherData[min][1] + weatherData[min+1][1] + weatherData[min+2][1])/3
        if (weatherData[i][1] + weatherData[i+1][1] + weatherData[i+2][1])/3 <= minimum_temp:
            min = i
    return min+1
print(coldestThreeDays(weatherData))

#3c)
def addNewDay(extraData, weatherData):
    extra = extraData.split()
    data = []
    for i in extra:
        i = i.strip()
        i = i.replace('max=', '')
        i = i.replace('min=','')
        i = i.replace('mm','')
        i = i.replace(',', '')
        data.append(float(i))
    weatherData.append(data)
    return weatherData
print(addNewDay('max=23.5, min=9.3, 5.1mm', weatherData))
