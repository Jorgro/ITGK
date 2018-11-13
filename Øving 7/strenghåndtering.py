


def reverse(stringe):
    liststring = list(stringe)
    nyliste = liststring[::-1]
    nystring = "".join(nyliste)
    return nystring


def check_equal(str1, str2):
    if len(str1) != len(str2):
        return False


    for i in range(len(str1)):
        if str1[i] == str2[i]:
            return True
        else:
            return False

def check_palindrome(str):
    reversed = reverse(str)
    print(check_equal(reversed, str))

def contains_string(str1, str2):
    if str1 in str2:
        print('True')
    else: print('False')
    for i in range(len(str2)):
        if "".join(str2[i:i+len(str1)]) == str1:
            print(i)

contains_string('feee', 'pdasdfdfadfdasdasdsfeeedkdsldls')
