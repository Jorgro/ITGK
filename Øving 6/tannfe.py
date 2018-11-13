
gyldige = [20, 10, 5, 1]

def oppdeler(tall):
    numberlist = []
    twenty = tall // 20
    ten = (tall%20)//10
    five = ((tall%20)%10)//5
    one = ((tall%20)%10)%5
    numberlist.append(twenty)
    numberlist.append(ten)
    numberlist.append(five)
    numberlist.append(one)
    return numberlist

def tannkalkulator(listemedvekt):
    emptylist = []

    for i in range(0, len(listemedvekt)):
        deltopp = oppdeler(listemedvekt[i])
        emptylist.append(deltopp)
        print(f'20: {oppdeler(listemedvekt[i])[0]}, 10: {oppdeler(listemedvekt[i])[1]}, 5: {oppdeler(listemedvekt[i])[2]}, 1: {oppdeler(listemedvekt[i])[3]}')





tannkalkulator([95,103,71,99,114,64,95,53,97,114,109,11,2,21,45,2,26,81,54,14,118,108,117,27,115,43,70,58,107])
