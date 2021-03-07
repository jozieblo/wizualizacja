#zad1
print("zad1")

sporty = ["Piłka siatkowa", "Piłka nożna", "Piłka koszykowa", "Tennis stołowy"]
print(sporty)
sporty.reverse()
print(sporty)
sporty.append("Bieg przełajowy")
sporty.append("Kajakarstwo")
print(sporty)



#zad2
print("zad2")

slownik={"brb":"be right back", "btw":"by the way","cya":"see you","gz":"Gratulations"}
print(slownik["cya"])


#zad3
print("zad3")
slownik2={"LOL":"League of Legends", "G":"Gothic","CSGO":"Counter Strike : Global Offensive","BD":"Battlefield"}
print(slownik2["LOL"])
print(slownik2.values())
print(len(slownik2))


#zad4

print("zad4")

print("Wprowadz zdanie")
zdanie=input()
count=zdanie.count("a")
print("Ilosc a jest rowna", count)



#zad5
print("zad5")
plik=open("jazda.txt", "r")
print(plik.readline())




#zad6

print("zad6")

print("Wprowadz 3 liczby")
x=input("Podaj 1 liczbe: ")
y=input("Podaj 2 liczbe: ")
z=input("Podaj 3 liczbe: ")
if (x>y) & (x>z):
    print("Najwieksza liczba to", x)
elif (y>x) & (y>z):
    print("Najwieksza liczba to", y)
elif (z > x) & (z > y):
    print("Najwieksza liczba to", z)
else:
    print("Liczby rowne")



#zad7

print("Zad7")

lista=[int(4), int(2), int(12), int(3)]
for x in range(len(lista)):
    lista[x]=lista[x]**lista[x]
    print(lista)




#zad8

#print("zad8")
#liczby=(0,1,2,3,4,5,6,7,8,9)
#i=0
#while i<10:
     #if liczby[i]%2=0:
# print(lista[i])
#i += 1



#zad9

print("zad9")
lista_kolejna=[1,2,3,4,5]
for x in lista_kolejna:
    print("E")

#zad10

print("zad10")

print("Wprowadz nieujemna liczbe")
try:
    liczba=int(input())
    if liczba%2==1:
        import math
        pierw=math.sqrt(liczba)
        print(pierw)
    else:
        print("Niezgosnosc")
except ValueError:
    raise ValueError("Liczba jest ujemna!.")



