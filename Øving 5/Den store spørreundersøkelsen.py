from sys import exit
antall_kvinner = []
antall_menn = []
antall_fag = []
antall_itgk = []
antall_timer_lekser = []
def statistikk():
    print(f'Antall kvinner: {sum(antall_kvinner)}')
    print(f'Antall menn: {sum(antall_menn)}')
    print(f'Antall som tar et eller flere fag: {sum(antall_fag)}')
    print(f'Antall som tar ITGK: {sum(antall_itgk)}')
    if len(antall_timer_lekser) == 0:
        print('Ikke definert')
    else:
        print(f'Snitt lekser: {(sum(antall_timer_lekser))/(len(antall_timer_lekser))}')
def questions():

    while True:


        print('Velkommen til spørreundersøkelsen! Skriv inn "hade" for å avslutte undersøkelsen. \n ')
        kjønn = input('Hvilket kjønn er du? [f/m] ')

        while kjønn != 'f' and kjønn != 'm' and kjønn != 'hade':
            kjønn = input('Hvilket kjønn er du? [f/m] \n')

        if kjønn == 'hade':

            statistikk()
            exit()

        if kjønn == 'm' or kjønn == 'f':
            if kjønn == 'm':
                antall_menn.append(1)
            if kjønn == 'f':
                antall_kvinner.append(1)
            alder = input('Hvor gammel er du? ')

            while alder.isnumeric() == False and alder != 'hade':
                print('Skriv inn et tall!')
                alder = input('Hvor gammel er du? ')
            if alder == 'hade':

                statistikk()
                exit()

            if int(alder) < 18 or int(alder) > 25:
                print('Du kan ikke ta denne undersøkelsen.\n ')
                questions()
            else:
                fag = input('Tar du et eller flere fag? [ja/nei] ')

                while fag != 'nei' and fag != 'ja' and fag != 'hade':
                    print('Er det så vanskelig å skrive inn ja/nei???')
                    fag = input('Tar du et eller flere fag? [ja/nei] ')
                if fag == 'hade':
                    statistikk()
                    exit()
                if fag == 'ja':
                    antall_fag.append(1)
                    if int(alder) < 22:
                        itgk = input('Tar du ITGK? [ja/nei] ')

                        while itgk != 'ja' and itgk != 'nei' and itgk != 'hade':
                            print('Du har skrivevansker ser jeg...')
                            itgk = input('Tar du ITGK? [ja/nei] ')
                        if itgk == 'hade':
                            exit(questions())
                        if itgk == 'ja':
                            antall_itgk.append(1)
                            lekser = input('Hvor mange timer lekser gjør du? ')
                            if lekser == 'hade':
                                exit(questions())
                            while lekser.isnumeric() == False:
                                print('Er du tilbakestående? ')
                                lekser = input('Hvor mange timer lekser gjør du? ')
                            if lekser.isnumeric() == True:
                                antall_timer_lekser.append(int(lekser))
                                questions()


                    if int(alder) >= 22 and int(alder) < 26:

                        itgk = input('Tar du virkelig ITGK? [ja/nei] ')

                        if itgk == 'hade':
                            statistikk()
                            exit()
                        while itgk != 'ja' and itgk != 'nei':
                            print('Fortsatt problemer med å skrive inn ja/nei ser jeg.')
                            itgk = input('Tar du ITGK? [ja/nei] ')

                        if itgk == 'ja':
                            antall_itgk.append(1)
                            lekser = input('Hvor mye arbeider du med lekser? (antall timer i uka) ')
                            if lekser == 'hade':

                                statistikk()
                                exit()

                            while lekser.isnumeric() == False:
                                print('Er du tilbakestående? ')
                                lekser = input('Hvor mye arbeider du med lekser? (antall timer i uka)  ')
                            if lekser.isnumeric() == True:
                                antall_timer_lekser.append(int(lekser))
                                questions()
                        if itgk == 'nei':

                            lekser = input('Hvor mye arbeider du med lekser? (antall timer i uka) ')
                            if lekser == 'hade':

                                statistikk()
                                exit()

                            while lekser.isnumeric() == False:
                                print('Er du tilbakestående? ')
                                lekser = input('Hvor mye arbeider du med lekser? (antall timer i uka) ')
                            if lekser.isnumeric() == True:
                                antall_timer_lekser.append(int(lekser))
                                questions()







                if fag == 'nei':
                    questions()
questions()
