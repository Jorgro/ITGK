#4a)
def bidOk(streng, number):
    return int(streng.split()[0])+6 >= number


#4b)
def game(bid, trick): 
    bidlist = bid.split()

    if bidlist[1] == 'grand':
        required = 3
    elif bidlist[1] in ('hjerter', 'spar'):
        required = 4
    elif bidlist[1] in ('kløver', 'ruter'):
        required = 5

    return int(bidlist[0]) > required and trick >= int(bidlist[0])+6

#4c)
#fuck this bridge shit