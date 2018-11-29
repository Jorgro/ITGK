
D = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
80: 'eighty', 90: 'ninety'}

L = [ 1000000, ' million', 1000, ' thousand', 1, '']

#4a)
def i2_text(number):
    if number == 0:
        return ''
    if number%10 == 0:
        first = D.get((number//10) *10)
        return f'{first}'
    elif (number//10) == 0:
        last = D.get(number%10)
        return f'{last}'
    else:
        first = D.get((number//10) *10)
        last = D.get(number%10)
        return f'{first}-{last}'


#4b)
def i3_text(number):
    if number < 100 and number >= 0:
        return i2_text(number)

    hundredel = number//100
    rest = number%100
    hundreplass = D.get(hundredel)
    if rest == 0:
        return f'{hundreplass} hundred'
    return f'{hundreplass} hundred {i2_text(rest)}'
#4c)
def i9_text(number):
    if number < 100:
        return i2_text(number)
    elif number < 1000:
        return i3_text(number)

    if number < 1000000:
        tusendel = number//1000
        rest = number%1000
        return f'{i3_text(tusendel)} thousand {i3_text(rest)}'

    milliondel = number//1000000
    rest = number%1000000
    tusendel = rest//1000
    rest2 = rest%1000
    if tusendel != 0:
        return f'{i3_text(milliondel)} million {i3_text(tusendel)} thousand {i3_text(rest2)}'
    else:
        return f'{i3_text(milliondel)} million {i3_text(rest2)}'.strip()
#4d)
def add_words(streng):
    strenglist = streng.split()
    for i in range(len(strenglist)):
        if strenglist[i].isdigit():
            numberstring = i9_text(int(strenglist[i]))
            numberstring_2 = '- '+numberstring+' -'
            strenglist.insert(i+1, numberstring_2)

    
    newstreng = ' '.join(strenglist)

    return newstreng.strip()
print(add_words('Mr. X shall pay 9005100 dollars'))
