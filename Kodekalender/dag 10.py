
symbols = []
with open('input(1).spp', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.split('')
        for i in line:
            symbols.append(i)

print(symbols)
