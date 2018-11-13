import math


def f(x):
    f = (x-12)*math.exp(5*x) - 8*(x+2)**2
    return f
def g(x):
    g = -x-2*x**2 - 5*x**3 +6*x**4
    return g


def derivate(h, x, function):
    derivert = (function(x+h/2)-function(x-h/2))/h
    return derivert


tol = float(input('Toleranse: '))

def secant_method(h, x, function, tol):
    while abs(float(function(x)/derivate(h, x, function))) > tol:
        gammel_x = x
        x = gammel_x - function(gammel_x)/derivate(h, x, function)

    return x

print(f'Funksjonen nærmer seg et nullpunkt når x = {secant_method(0.00000001,-2,f, tol)}, da er y = {f(secant_method(0.00000001,-2,f, tol))}')
