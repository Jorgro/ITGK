g = 'python'
j = int(input('Hei. Nå skal vi spille Hangman. Hvor mange forsøk vil du ha? '))
n = set(g)
l = set([])

while True: 
    f = input('Bokstav: \n', )
    if f in n:
        print('Bokstaven er i ordet.' )
        l.add(f)
        # if statements for å 
        if l == n:
            print(f'Du klarte det! Det hemmelige ordet var {g}')
            break
        
        # if f in:
        #     print('p*****')
        # elif f == 'y':
        #     print('*y****')
        # elif f == 't':
        #     print('**t**')
        # elif f == 'h':
        #     print('***h**')
        # elif f == 'o':
        #     print('****o*')
        # elif f == 'n':
        #     print('*****n') går ikke siden den bare tar 1 av de. 
        
    

    elif f not in n and j > 0: 
        j = j-1
        print(f'Bokstaven {f} er ikke i ordet. Du har {j} forsøk igjen.')
        if j == 0:
            print(f'Bokstaven {f} er ikke i ordet. Du er død.')
            break 
    
        
    