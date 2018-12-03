def read_file(filename):
    try:
        with open(filename, 'r') as file:
            innhold = file.read()
        return innhold

    except IOError:
        #Å huske navnet på alle errors er vanskelig, så mulig at den er feil, men koden ville kjørt akkurat like fint med bare except
        print(f'Kan ikke finne filen {filename}')
        return None

streng= read_file('flerkamp.txt')
print(streng)
def list_from_string(txt):
    txt = txt.split(',')
    for i in range(len(txt)):
        txt[i] = txt[i].strip('\n') #tror ikke denne trengs, men vil være på den sikre siden
        txt[i] = txt[i].strip()

    return txt
print(list_from_string("Lisa,  12,   1.30,   12,    13,  1:13.02\n"))

def make_result_list(string_from_file):
    tabell = []

    list_from_file = string_from_file.split('\n')

    for line in list_from_file:
        newList = list_from_string(line)
        tabell.append(newList)
    return tabell
k = make_result_list(streng)

def time_to_seconds(time):
    time = time.replace('.', ':')
    time = time.split(':')
    float_time = float(time[0])*60+float(time[1]) + float(time[2])/100

    return float_time

def str_to_numbers(results):

    for i in results:
        for j in range(len(i)):
            try:
                if float(i[j]) == round(float(i[j])):
                    #tester for om den avrundede verdien er lik verdien selv -> dersom sant må tallet være et heltall
                    i[j] = int(i[j])
                else:
                    i[j] = float(i[j])

            except:
                    #dersom vi får en error i try-blokken over så kan elementet ikke være på et vanlig tallformat
                try:
                    i[j] = time_to_seconds(i[j])
                    #tester for om strengen kan gjøres om ved hjelp av funksjonen fra 3d)
                    #grunnen til at dette fungerer er at dersom elementet i[j] bare er en vanlig streng vil vi få en error når vi splitter og tester for time[2] som ikke eksisterer i den listen.
                except:
                    continue #dersom vanlig streng (som navnet)



    return results

print(str_to_numbers(k))
def find_data(event, name, results):

    event_index = results[0].index(event)

    for i in results:
        if i[0] == name:
            return i[event_index]
def event_results(event, results):

    event_index = results[0].index(event)

    results_table = []

    for i in range(1, len(results)):
        results_table.append([results[i][0], results[i][event_index]])

    sorted_results = sorted(results_table, key = lambda elem: elem[1], reverse = True)
    #sorted_results = sort_list(results_table, 1):sorted_results.reverse() også mulig, men lambda funksjonen skal gjøre akkurat det samme

    return sorted_results
print(event_results('Poker', k))
