import datetime
def weekday_newyear(year):
    date = datetime.datetime(year, 1, 1)
    sentence = '{:%A}'.format(date)
    print(sentence)
weekday_newyear(1900)
