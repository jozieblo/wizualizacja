
import sys
plik = open("test.txt", "r")
znaki = plik.read(10)
linia = plik.readline()
wiersze = plik.readlines()
print(znaki)
print(linia)
print(wiersze)
plik.close()

print("podaj imie, nazwisko i grupe: ")
dane=sys.stdin.readline()
plik=open("zapis.txt","w+")
plik.write(dane)
plik.close()

import sys
#zad1
print("zad1")
pliczek=[]
for x in range(1,50):
    if(x%4==0):
        pliczek+=[x]
plik=open("zapis.txt","a+")
plik.writelines(str(pliczek))
plik.close()
#zad2
print("zad2")
plik2=open("zapis.txt","r")
linia = plik2.readline()
wiersze2=plik2.readlines()
print(linia)
print(wiersze2)
#zad3
print("zad3")
with open("zapis.txt","a+") as plik3:
    print("\n")
    print("podaj imie, nazwisko i grupe: ")
    dane2 = sys.stdin.readline()
    print(dane2)
    plik3.write(dane2)
#zad4
print("zad4")
class kons:
    def __init__(self, nazwa_produktu, ilosc, jednostka, cena):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka= jednostka
        self.cena=cena
    def wyswietl_produkt(self):
        return self.nazwa_produktu,self.ilosc,self.jednostka,self.cena
    def ile_produktu(self):
        return self.ilosc , self.jednostka
    def ile_kosztuje(self):
        return self.ilosc * self.cena
p=kons("groszek",4, "sztuki",5)
print(p.wyswietl_produkt())
print(p.ile_produktu())
print(p.ile_kosztuje())

#zad5
print("zad5")
class ciagi:
    def __init__(self,a1,r,an,suma,i,n,lista1):
        self.a1=a1
        self.r=r
        self.an = an
        self.suma = suma
        self.i= i
        self.n = n
        self.lista1 = lista1
    def wyswietl_dane(self):
        return self.a1,self.suma,self.r
    def pobierz_elementy(self):
        self.a1 = int(input("Podaj pierwszy wyraz ciagu"))
        self.an = int(input("Podaj n wyraz ciagu"))
        self.r = int(input("Podaj roznice ciagu"))
    def pobierz_parametry(self):
        self.a1 = int(input("Podaj pierwszy wyraz ciagu"))
        self.r = int(input("Podaj roznice"))
        self.an =int(input("Podaj ile elementow trzeba wygenerowac"))
        i=0
        for i in range(self.a1,self.an):
          i=i+self.r
          print(i)

    def policz_sume(self):
         self.a1 = int(input("Podaj pierwszy wyraz ciagu"))
         self.r = int(input("Podaj roznice"))
         self.n = int(input("Podaj n wyraz"))
         self.suma=(2*self.a1+(self.n-1)*self.r*self.n)/2
         return self.suma

    def policz_elementy(self):
        self.a1 = int(input("Podaj pierwszy wyraz ciagu"))
        self.r = int(input("Podaj roznice"))
        self.an = int(input("Podaj ile elementow trzeba wygenerowac"))
        i=0
        for i in range(self.a1,self.an):
         i = i + self.r
         print(i)


liczby5=ciagi(1,2,50,300,1,27,0)
print(liczby5.wyswietl_dane())
print(liczby5.pobierz_elementy())
print(liczby5.pobierz_parametry())
print(liczby5.policz_sume())
print(liczby5.policz_elementy())

#zad6
print("zad6")
class robaczek:
    def __init__(self,x,y,krok):
        self.x = x
        self.y = y
        self.krok = krok
    def gora(self,ile_krokow):

        self.y+=ile_krokow*self.krok

    def dol(self, ile_krokow):
        self.y -= ile_krokow * self.krok

    def lewo(self, ile_krokow):
        self.x -= ile_krokow * self.krok
    def prawo(self, ile_krokow):
        self.x += ile_krokow * self.krok
    def gdzie(self):
        return (self.x,self.y)
rob=robaczek(0,0,1)
rob.dol(20)
rob.gora(4)
rob.lewo(7)
rob.prawo(11)
print(rob.gdzie())
