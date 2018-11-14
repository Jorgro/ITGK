def file_to_table(txtfile):
    f = open(txtfile, 'r')
    innhold = f.readlines()
    f.close()
    fullstendigtabell = []
    for line in innhold:
        tabell = []
        b = line.split(',')
        for i in b:
            try:
                tabell.append(int(b[i]))
            except:
                tabell.append(str(b[i]))
    fullstendigtabell.append(tabell)
    return fullstendigtabell

