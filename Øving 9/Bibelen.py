def read_from_file(filename):
    f = open(filename, 'r')
    innhold = f.read()
    return innhold
    f.close()


def remove_symbols(text):
    textlist = list(text)
    newtext = []
    for i in range(len(textlist)):
        if textlist[i].isalpha() or textlist[i] ==' ':
            newtext.append(textlist[i])

    newtext = ''.join(newtext)
    finished = newtext.lower()
    return finished

def count_words(filename):
    text = read_from_file(filename)
    text = remove_symbols(text)
    textlist = text.split()
    textset = set(textlist)
    worddictionary = {}
    for i in textset:
        counter = textlist.count(i)
        worddictionary[i] = counter
    return worddictionary
bible_dict = count_words('BIBLE.txt')
for word, value in bible_dict.items():
    print(word, value)
