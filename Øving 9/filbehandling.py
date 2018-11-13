# 'r' - for lesing av filen (default)
# 'w' - for skriving til filen
# 'a' - for å legge til data (append) til den eksisterende filen
# f = open('minfil.txt', 'w')
# f.write('Dette er innholdet i min fil')
# f.close()
# f = open('minfil.txt', 'r')
# innhold = f.read()
# print(innhold)
# f.close()
def write_to_file(data):
    f = open('my_file.txt', 'a')
    f.write(data)
    f.close()
def read_from_file(filename):
    f = open(filename, 'r')
    innhold = f.read()
    print(innhold)
    f.close()
def main():
    answer = ''
    while answer != 'done':
        answer = input('Read or write? ')
        if answer.lower() == 'read':
            read_from_file('my_file.txt')
        elif answer.lower() == 'write':
            writing = input('What do you want to write? ')
            write_to_file(writing)
        elif answer != 'done':
            print('You must "write" or "read".')
main()
