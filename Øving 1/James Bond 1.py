import math



j = input('Gi inn et desimaltall: ')
k = input('Antall desimaler i avrunding: ')

des = float(j)*10**int(k)-math.floor(float(j)*10**int(k))
if des == 0.5:
    result = math.ceil(float(j) * 10**int(k)) / 10**int(k)
    print(result)

else:
    h= round(float(j), int(k))
    print(h)




# if j[-k]==5
#(j[-int(k)-1])*10**int(len(j)-1)==5
