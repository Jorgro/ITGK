def file_to_table(txtfile):
    f = open(txtfile, 'r')
    innhold = f.readlines()
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
def time_diff(start, stop):
    differanse =(stop[3]*3600 +stop[4]*60 + stop[5]) - (start[3]*3600 +start[4]*60 + start[5])
    return differanse


def list_speeders(filename_a, filename_b, speed_limit, distance):
    box_a = file_to_table(filename_a)
    box_b = file_to_table(filename_b)
    for i in range(len(box_a)):
