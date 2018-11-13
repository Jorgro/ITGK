import numpy as np
a =[1, 2, 3, 4, 5, 6, [8, 9, 10]]
b = [7, 8, 9, 10, 11, 12]
def areOrthogonal(a, b):
    a = np.array(a)
    b = np.array(b)
    if np.dot(a, b) == 0:
        print('Orthogonal')
    else:
        print(' No u')
areOrthogonal(a, b)
