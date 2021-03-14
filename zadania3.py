#zad1
print("zad1")
a=[1-x for x in range(1,11)]
print(a)

b=[4**y for y in range(8)]
print(b)

c=[z for z in a if z % 2==0]
print(c)
#zad2
print("zad2")
import random

lista1=[random.randint(0, 10) for _ in range(10)]
print(lista1)
lista2=[v for v in lista1 if v % 2==0]
print(lista2)

#zad3
print("zad3")
slownik={"woda":"mililitry", "chleb":"sztuki", "mięso":"kilogramy","sos":"sztuki"}
slownik2={i for i in slownik  if slownik[i]=="sztuki" }
print(slownik2)

#zad4
print("zad4")

def troj(a,b,c):
    pit1=a**2+b**2
    pit2 = b ** 2 + c ** 2
    pit3 = a ** 2 + c ** 2
    if pit1==c**2:
        print("Trojkat jest  prostokatny")
        return 0
    elif pit2 == a ** 2:
        print("Trojkat jest  prostokatny")
        return 0
    elif pit3 == b ** 2:
        print("Trojkat jest  prostokatny")
        return 0
    else:
        print("Trojkat nie jest prostokatny")
        return 0
print(troj(1,2,3))

print(troj(3,4,5))

print(troj(6,8,10))

print(troj(5,3,4))

print(troj(4,3,5))

#zad5
print("zad5")
def trapez(a=1, b=2,h=4):
    pole=((a+b)*h)/2
    return pole
print(trapez())

#zad6
print("zad6")
def ilocz(a=1,b=4,ile=10):
 for j in range(a, ile):
     print(j*b)
     ilocz(1,5,12)

#zad7
print("zad7")
def ilocz2(*nbs):
    if len(nbs) != 3:
        print('Podaj trzy liczby')
        return -1
    for ilosc in range(nbs[0], nbs[2]):
        print(ilosc * nbs[1])
ilocz2(2,4,6)

#zad8
print("zad8")
def funk(**kwargs):
 return len(kwargs.items()), sum(t for t in kwargs.values())
print(funk(bulka=1,banan=2,orzechy=5))

#zad9
print("zad9")
from ciagi_liczbowe import *






