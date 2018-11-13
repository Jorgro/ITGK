def stringcounter(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    liste = []
    for i in range(len(str2)):
        if "".join(str2[i:i+len(str1)]) == str1:
            liste.append(i)
    return liste

print(stringcounter("oo", "Never let you go let me go. Never let me go ooo" ))
def stringtroll(str1, str2, str3):
    liste = stringcounter(str1, str2)
    print(stringcounter(str1, str2))
    list2 = list(str2)
    for i in liste:
        list2[i] = str3

    return "".join(list2)
print(stringtroll('is', "Is this the real life? Is this just fantasy?", 'cool'))
