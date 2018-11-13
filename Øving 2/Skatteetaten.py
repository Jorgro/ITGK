g = input('Oppgi hvor mye av boligen som ble utleid: ')
h = input('Skriv inn hva du har hatt i leieinntekt: ')
if float(g) > 100:
    print('Error')
elif float(g)< 50:
    print('Skattepliktig beløp er 0')
elif float(g)>50 and float(h)< 20000:
    print('Skattepliktig beløp er 0')
else:
    print(f'Skattepliktig beløp for bolig er {h}')


a = input('Skriv inn type annen bolig: ')



print(f'Du har valgt {a}.')
if a == 'Fritidsbolig' or a == 'fritidsbolig':
    c = input(f'Formålet: ')
    f_1 = input(f'Hvor mange fritidsbolig(er) leier du ut: ')
    d_1 = input(f'Utleieinntekt pr fritidsbolig: ')
    if c == 'fritid' and float(d_1)>10000:
        print('Inntekten er skattepliktig')
        d_2 = (float(d_1)-10000)
        print(f'Overkytende beløp pr. fritidsbolig er {d_2}')
        skattepliktig = float(d_2)*0.85
        print(f'Skattepliktig inntekt pr. fritidsbolig er {skattepliktig}')
        totalt = float(skattepliktig)*float(f_1)
        print(f'Totalt skattepliktig beløp er {totalt} kr')
    elif c == 'Utleie':
        print('Inntekten er skattepliktig')
        skattepliktig = float(d_1)
        print(f'Skattepliktig inntekt pr. fritidsbolig er {skattepliktig} kr')
        totalt = float(skattepliktig)*float(f_1)
        print(f'Totalt skattepliktig beløp for fritidsbolig(er) er {totalt} kr')
    else:
        print('Skattepliktig beløp er 0')
    
    
    
elif a == 'Sekundærbolig' or a == 'sekundærbolig':
    f_2 = input(f'Hvor mange sekundærbolig(er) leier du ut: ')
    d_2 = input(f'Utleieinntekt pr sekundærbolig: ')
    skatt_2 = float(f_2)*float(d_2)
    print(f'Totalt skattepliktig inntekt for sekundærbolig(er) er {skatt_2} kr')



a = input('Skriv inn type annen bolig: ')



print(f'Du har valgt {a}.')
if a == 'Fritidsbolig' or a == 'fritidsbolig':
    c = input(f'Formålet: ')
    f_1 = input(f'Hvor mange fritidsbolig(er) leier du ut: ')
    d_1 = input(f'Utleieinntekt pr fritidsbolig: ')
    if c == 'fritid' and float(d_1)>10000:
        print('Inntekten er skattepliktig')
        d_2 = (float(d_1)-10000)
        print(f'Overkytende beløp pr. fritidsbolig er {d_2}')
        skattepliktig = float(d_2)*0.85
        print(f'Skattepliktig inntekt pr. fritidsbolig er {skattepliktig}')
        totalt = float(skattepliktig)*float(f_1)
        print(f'Totalt skattepliktig for fritidsbolig(er) beløp er {totalt} kr')
    elif c == 'Utleie':
        print('Inntekten er skattepliktig')
        skattepliktig = float(d_1)
        print(f'Skattepliktig inntekt pr. fritidsbolig er {skattepliktig} kr')
        totalt = float(skattepliktig)*float(f_1)
        print(f'Totalt skattepliktig beløp for fritidsbolig(er) er {totalt} kr')
    else:
        print('Skattepliktig for fritidsbolig(er) beløp er 0')
    
    
    
elif a == 'Sekundærbolig' or a == 'sekundærbolig':
    f_2 = input(f'Hvor mange sekundærbolig(er) leier du ut: ')
    d_2 = input(f'Utleieinntekt pr sekundærbolig: ')
    skatt_2 = float(f_2)*float(d_2)
    print(f'Totalt skattepliktig for sekundærbolig(er) er {skatt_2} kr')

alttotalt = float(skatt_2)+float(totalt)+float(h)
print(f'Totalt skattepliktig beløp for alle boliger er {alttotalt}')
