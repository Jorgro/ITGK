
symbols = ''

with open('input.spp', 'r') as file:
    for line in file:
        line = line.strip('\n')
        
        symbols += line

print(symbols)

def parser(streng):
    import random
    import math
    stack = []
    for i in streng:
        print(stack)
        if i == ' ':
            stack.append(31)
        elif i == '|':
            stack.append(3)
        elif i == ':':
            k = sum(stack)
            stack = [k]
        elif i == "'":
            k = stack.pop(-1) + stack.pop(-1)
            stack.append(k)
        elif i == '.':
            k = stack.pop(-1) + stack.pop(-1)
            stack.append(k), stack.append(-k)
        elif i == '_':
            a = stack.pop(-1)
            k = a*stack.pop(-1)
            stack.append(k), stack.append(a)
        elif i == '/':
            stack.pop(-1)
        elif i == 'i':
            stack.append(stack[-1])
        elif i == '*':
            k = stack.pop(-1) // stack.pop(-1)
            stack.append(k)
        elif i == ']':
            k = stack.pop(-1)
            if k%2 == 0:
                stack.append(1)
        elif i == ']':
            k = stack.pop(-1)
            if k%2 == 1:
                stack.append(k)
        elif i == '~':
            k, a, b = stack.pop(-1), stack.pop(-1), stack.pop(-1)
            stack.append(max([k, a, b]))
        elif i == '\\':
            stack[-1] += 1



        
        

    print(stack)
    return max(stack)
print(parser(symbols))