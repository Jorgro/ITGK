# sum = 0
# for x in range(1, 100, 1):
#     sum = sum +x
#     print(sum)
# mul = 1
# while mul < 1000: 
#     for x in range(1, 100, 1):
#      mul = mul * x 
#     print(mul)

    
g = float(input('Hva er 4*3? '))
while g != 12: 
    print('Det var feil, prøv igjen.')
    g = float(input('Hva er 4*3? '))
else: 
    print('Korrekt')
