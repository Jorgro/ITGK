lastyear = int(input('Last year: '))
firstyear = int(input('First year: '))
def summerOlympics(firstyear, lastyear):
    years = []
    for i in range(firstyear, lastyear+1):
        if (i-1948)%4 == 0:
            years.append(i)
    return years
years = summerOlympics(firstyear, lastyear)
print(years)
