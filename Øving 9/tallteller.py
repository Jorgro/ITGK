
def number_of_lines(filename):
    f = open(filename, 'r')
    num_lines = sum(1 for line in f)
    print(num_lines)
number_of_lines('numbers.txt')

def number_frequence(filename):
    f = open(filename, 'r')
    innhold = f.read()
    number_frequence = {}
    keyset = set(innhold)
    values = innhold.split()
    for i in keyset:
        if i.isdigit():
            number_frequence[i] = values.count(i)
    return number_frequence

def printer(dictionary):
    for key in dictionary:
        print(f'{key} : {dictionary[key]}')
printer(number_frequence('numbers.txt'))
