i = 0
while True:
    print(i, end = '')
    print('\b' * len(str(i)), end='', flush=True)


    i += 1