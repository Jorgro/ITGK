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