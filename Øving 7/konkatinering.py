def tekst(s1, s2):
    streng = s1 + ' '+ s2
    return streng

print(tekst('hey', 'bond'))

def tekstlist(list):
    nystreng = ''
    for streng in list:
        nystreng += streng
    return nystreng

print(tekstlist(['hey', 'james', 'bond']))

def bokstav(list):
    for i in range(len(list)):
        print(list[i][0])
bokstav(['Uka','red'])
def func1(liste):
    streng = ""
    for s in liste:
        if len(s)>3:
            streng += s[3]
    return streng

def func2(streng):
    streng += streng
    return streng

print(func2(func1(["Klabert","Oslo","Tur","stubbe"])))
