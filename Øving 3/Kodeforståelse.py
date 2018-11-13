a=345
b=''
while a or b=='':
    b=str(a%16)+b
    a=a//16
print(b)
