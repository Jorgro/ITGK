#4a)

pulsData = [110,118,125,127,127,130,129,131,132,134,134,135,145,157,165,172,173,178,179,178]
def pulsStatistikk(pulsData):
    results = []
    maximum = pulsData[0]
    minimum = pulsData[0]
    average = 0 
    for i in pulsData:
        if i < minimum: 
            minimum = i
        if i > maximum:
            maximum = i
        
        average += i
    average = average/len(pulsData)
    results.append(average), results.append(minimum), results.append(maximum)
    return results
print(pulsStatistikk(pulsData))

#4b)
def pulsSoneGrenser(maksPuls):
    sone1 = 0.6*maksPuls
    sone2 = 0.725*maksPuls
    sone3 = 0.825*maksPuls
    sone4 = 0.875*maksPuls
    sone5 = 0.925*maksPuls
    pulsSoner = [sone1, round(sone2, 1), sone3, sone4, sone5]
    return pulsSoner

print(pulsSoneGrenser(188))

#4c)
def pulsSoner(maksPuls, pulsData):
    points = [0, 0, 0, 0, 0]
    grenser = pulsSoneGrenser(maksPuls)
    
    for i in pulsData:
        if i >= grenser[0] and i < grenser[1]:
            points[0] += 1
        elif i >= grenser[1] and i < grenser[2]:
            points[1] += 1
        elif i >= grenser[2] and i < grenser[3]:
            points[2] += 1
        elif i >= grenser[3] and i < grenser[4]:
            points[3] += 1
        elif i >= grenser[4]:
            points[4] += 1


    print(points)
    percentage = []
    sum_points = sum(points)
    for i in points: 
        percentage.append(i*100/(sum_points))

    return percentage

print(pulsSoner(188, pulsData))

def lengstePultsOkning(pulsData):
    record = (0, 0)
    for i in range(len(pulsData)-1):
        start = i
        k = i
        while pulsData[k+1] >= pulsData[k]:
            k += 1
            
        if k-start > record[0]:
            record = (k-start+1, start+1)

    return [record]

print(lengstePultsOkning(pulsData))