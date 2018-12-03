def vectors(filename):
    dict_vectors = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            line = line.split(';')
            for i in range(len(line)):
                line[i] = line[i].split(',')
                line[i][0] = line[i][0].replace('(', '')
                line[i][1] = line[i][1].replace(')', '')

            slope = (int(line[1][1])-int(line[0][1])) / (int(line[1][0])-int(line[0][0]))

            if abs(slope) in dict_vectors:
                dict_vectors[abs(slope)] += 1
            else:
                dict_vectors[abs(slope)] = 1

    return max(zip(dict_vectors.values(), dict_vectors.keys()))
print(vectors('input-rain.txt'))
