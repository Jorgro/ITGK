# mystring = 'Roser er røde'
# print(mystring[0])
# for i in range(len(mystring)):
#     print(mystring[i])

def stringprinter(string):
    for i in range(len(string)):
        print(string[i])
def bokstavprinter(string):
    if len(string)>=3:
        print(string[2])
    else:
        print('q')

stringprinter('hey')
bokstavprinter('hey')
def sisteindeks(string):
    s = list(string)
    print(len(s)-1)
sisteindeks('The way of kings')
