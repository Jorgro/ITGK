def fu1(a):
    r = 0
    while(a>0):
        s = a%10
        r = r + s
        a = (a-s)/10

    return r
print(fu1(1234))
print(1234%10)
