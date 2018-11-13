car_table = [[2017, 11, 17, 6, 21, 12, 'HB69082'], [2017, 11, 17, 6, 21, 53, 'CV86023'],
[2017, 11, 17, 6, 23, 0, 'HD27560'], [2017, 11, 17, 6, 23, 2, 'UT29891'], [2017,
11, 17, 6, 24, 25, 'IS11293'], [2017, 11, 17, 6, 24, 40, 'EL73840'], [2017, 11,
17, 6, 24, 41, 'UT55227'], [2017, 11, 17, 6, 26, 55, 'NB59108'], [2017, 11, 17,
6, 27, 29, 'UT46408'], [2017, 11, 17, 6, 28, 19, 'LE68228']]

import datetime

def date_diff(start,end):
 d0 = datetime.date(start[0],start[1],start[2])
 d1 = datetime.date(end[0],end[1],end[2])
 delta = d1-d0
 return delta.days

def time_diff(start, stop):
    date = date_diff(start, stop)
    
    differanse =(stop[3]*3600 +stop[4]*60 + stop[5]+date*3600*24) - (start[3]*3600 +start[4]*60 + start[5])
    return differanse

diff = time_diff([2017,11,17,23,59,59],[2017,11,18,0,9,12])
print(diff)


def check_min_distance(car_table, diff):
    tidsliste = []
    for liste in car_table:
        tider = liste[:6]
        tidsliste.append(tider)
    crazy_drivers = []
    for i in range(len(car_table)-1):
        if time_diff(car_table[i], car_table[i+1]) < diff:
            crazy_drivers.append(car_table[i+1][-1])
    return crazy_drivers
print(check_min_distance(car_table, 3))

def list_el_cars(car_table):
    elcars = []
    for liste in car_table:
        car = liste[-1]
        if car[0:2] == 'EK' or car[0:2] == 'EL' or car[0:2] == 'EV':
            elcars.append(liste)
    return len(elcars)
print(list_el_cars(car_table))
import random
bokstaver = ['BS', 'CV', 'EL', 'FY', 'KU', 'LE', 'NB', 'PC', 'SY', 'WC']

def generate_license_numbers(amount):
    license_numbers = []
    while len(license_numbers) < amount:
        license = random.choice(bokstaver) + str(random.randint(10000, 99999))
        if license not in license_numbers:
            license_numbers.append(license)
    return license_numbers
print(generate_license_numbers(10))
