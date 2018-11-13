import binascii

def toHex(word):
    return int(str(binascii.hexlify(word), 'ascii'), 16)

def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')

def stringtobinary(string):
    string = bytes(string, encoding = 'ascii')
    return string

def encrypt(message, key):
    if len(message)!=len(key):
        print('Mission failed, we will get him next time.')
        exit()
    message = stringtobinary(message)
    message = toHex(message)
    key = stringtobinary(key)
    key = toHex(key)
    code = message ^ key
    return code
    # print(f'Krypto: {code}')
def decrypt(code, key):
    key = stringtobinary(key)
    key = toHex(key)
    message = code ^ key
    message = toString(message)
    print(f'The message was {message}')

import string
import random
g = input('\nHva vil du kryptere? ')
alphabet = list(string.ascii_lowercase)
key = list(random.choice(alphabet) for i in range(len(g)))
key = ''.join(key)
print(key)
code = encrypt(g, key)
print(code)
f = input('do you wanna decrypt? Y/N ')
if f == 'Y':
    decrypt(code, key)
else:
    print('Ok')
