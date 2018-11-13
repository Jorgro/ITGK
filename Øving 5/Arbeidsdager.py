
def dagfinnern(dag):
    if dag == 0:
        dag = 'mon'
        return dag
    if dag == 1:
        dag = 'tir'
        return dag
    if dag == 2:
        dag = 'ons'
        return dag
    if dag == 3:
        dag = 'tor'
        return dag
    if dag == 4:
        dag = 'fre'
        return dag
    if dag == 5:
        dag = 'lør'
        return dag
    if dag == 6:
        dag = 'søn'
        return dag

def is_leap_year ( year ):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def modulo7(year):
    restvedmodulo = int(year) % 4
    return restvedmodulo


def weekday_newyear(year):
    modulo7(year)
    ekstra_år_liste = []
    for x in range(1,5):
        ekstra_år = ((year-modulo7(year)*x)-1900)/4
        ekstra_år_liste.append(ekstra_år)

    ekstra = max(ekstra_år_liste)
    if year % 4 != 0 and year > 1904:
        dag = int(((year-3) % 7))+int(ekstra)
        gammel_dag = dag

        if dag > 6:
            dag = abs(7 - gammel_dag)
            dagfinnern(dag)
            print(f'{year} {dagfinnern(dag)}')
        else:
            dagfinnern(dag)
            print(f'{year} {dagfinnern(dag)}')

    if year % 4 == 0 and year > 1900:
        dag = int(((year-3) % 7))+int(ekstra)-1
        gammel_dag = dag

        if dag > 6:
            dag = abs(7 - gammel_dag)
            dagfinnern(dag)
            print(f'{year} {dagfinnern(dag)}')
        else:
            dagfinnern(dag)
            print(f'{year} {dagfinnern(dag)}')

    if year < 1904:
        dag = int(((year-3) % 7))
        gammel_dag = dag

        dagfinnern(dag)
        print(f'{year} {dagfinnern(dag)}')

for year in range(1900, 1921):
    weekday_newyear(year)


def is_workday(day):
    if day >= 0 and day < 5:
        return True
    else:
        return False

def weekday_newyear2(year):
    modulo7(year)
    ekstra_år_liste = []
    for x in range(1,5):
        ekstra_år = ((year-modulo7(year)*x)-1900)/4
        ekstra_år_liste.append(ekstra_år)

    ekstra = max(ekstra_år_liste)
    if year % 4 != 0 and year > 1904:
        dag = int(((year-3) % 7))+int(ekstra)
        gammel_dag = dag

        if dag > 6:
            dag = abs(7 - gammel_dag)
            return(dag)

        else:
            return(dag)

    if year % 4 == 0 and year > 1900:
        dag = int(((year-3) % 7))+int(ekstra)-1
        gammel_dag = dag

        if dag > 6:
            dag = abs(7 - gammel_dag)
            return(dag)
        else:
            return(dag)

    if year < 1904:
        dag = int(((year-3) % 7))
        gammel_dag = dag
        return(dag)

def workdays_in_year(year):


    if is_workday(weekday_newyear2(year)) and not is_leap_year(year):
        print(f'{year} har 261 arbeidsdager')
    elif is_workday(weekday_newyear2(year)) and is_leap_year(year) and weekday_newyear2(year) != 4:
        print(f'{year} har 262 arbeidsdager')
    elif not is_workday(weekday_newyear2(year)) and not is_leap_year(year):
        print(f'{year} har 260 arbeidsdager')
    elif not is_workday(weekday_newyear2(year)):
        print(f'{year} har 260 arbeidsdager')



for year in range(1900, 1920):
    workdays_in_year(year)
