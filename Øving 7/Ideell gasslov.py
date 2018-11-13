
def p_ig(t, v, n, rgas=8.31452):
    p = n*rgas*t / v
    return p

nv = 10     # number of volumes (rows)
nt = 3      # number of temperatures (columns)

n = 10      # [mol]
t = [100 + float(j)*200 for j in range(nt)]     # [K]
v = [10**(-float(i)/nv) for i in range(1, nv+1)]

def p_ig_pptable(t, v, n, rgas=8.31452):
    gasstrykk = []
    for k in range(len(v)):
        listtemp = []
        listtemp.append(v[k])
        for h in range(len(t)):
            listtemp.append(p_ig(t[h], v[k], n))

        gasstrykk.append(listtemp)

    return gasstrykk

table = p_ig_pptable(t,v,n)

def printer(table):
    for i in range(len(table)):
        for k in range(len(table[i])):
            # print(table[i][k]) 40-len(str(table[i][k]))
            print(('|' + str(table[i][k])).ljust(21), end='')
        print()
print('For n = 10 mol, så har vi at det ideelle gasstrykket er: ')

print("\n| Volum (m^3)".ljust(21),"|",("Temp. = "+str(t[0])+"K").ljust(19),"|",("Temp. = "+str(t[1])+"K").ljust(19),"|",("Temp. = "+str(t[2])+"K").ljust(19),"|")
print("-"*89)
printer(table)
