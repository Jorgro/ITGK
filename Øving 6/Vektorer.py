import random


def vector_print(liste, name):
    print(f'{name} = {liste}')

def vektorliste():
    liste = []
    for i in range(0, 3):
        integer = random.randint(0, 10)
        liste.append(integer)

    return liste



def skalarmultiplisering(liste, skalar):
    for i in range(len(liste)):
        liste[i] = liste[i]*skalar
    return liste

def vektorprodukt(vektor1, vektor2):
    prikkprodukt = vektorlengde(vektor1)* vektorlengde(vektor2)
    return prikkprodukt

def vektorlengde(vektor):
    vektorsum = []
    for i in range(len(vektor)):
        vektorsum.append(vektor[i]**2)
    lengde = sum(vektorsum)**0.5
    return lengde

def main():
    vektor = vektorliste()
    vector_print(vektor, 'vec')
    skalar = int(input('Skriv inn en skalar: '))
    print(skalarmultiplisering(vektor, skalar))
    nyvektor = skalarmultiplisering(vektor, skalar)
    vektorlengde1 = vektorlengde(vektor)
    vektorlengde2 = vektorlengde(skalarmultiplisering(vektor, skalar))

    print(f'Lengde før skalering = {vektorlengde1} \nLengde etter skalering = {vektorlengde2} \nForhold mellom lengde = {vektorlengde2/vektorlengde1}')



main()
