fasit = ['A', 'C', 'B', 'D', 'A', 'A', 'B', 'A', 'C', 'A', 'D', 'A', 'C', 'C', 'B', 'A', 'B', 'A', 'C', 'D']
def fasitsjekker(svarliste):
    poengregner = []
    for i in range(0, 20):
        if svarliste[i]!=fasit[i]:
            poengregner.append(1)

    prosentregner = 20 - sum(poengregner)
    print(f'{prosentregner*100/20}%')
fasitsjekker(['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'])
