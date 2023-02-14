class Koszyk:
    def __init__(self):
        self.zakupy = {}

    def dodajProdukt(self, produkt, ilosc):

        if (produkt in self.zakupy):
            ile = self.zakupy[produkt]
            self.zakupy[produkt] = ile + ilosc
        else:
            self.zakupy[produkt] = ilosc

    def odejmijProdukt(self, produkt, ilosc):
        ile = self.zakupy[produkt]
        if (ile < ilosc):
            print("Niedozwolona ilosc")
        elif (ile == ilosc):
            del self.zakupy[produkt]
        else:
            self.zakupy[produkt] = ile-ilosc


magazyn = {"chleb":2.50, "sok":1.80, "woda":3.0, "piwo":5.50}
obj = Koszyk()


while(True):
    dec = input("Co robimy ? D - dodaj, U - usun, P - podglad, K - koniec ").upper()

    if(dec == "D"):
        print(magazyn)
        produkt = input("Podaj nazwę produktu: ")

        if(produkt in magazyn):

            ilosc = int(input("Podaj ilosc produktu: "))
            obj.dodajProdukt(produkt, ilosc)
        else:
            print("Brak produktu na magazynie")

    elif(dec == "P"):
        print(obj.zakupy)
    elif(dec == "U"):
        print(obj.zakupy)
        produkt = input("Podaj nazwę produktu do usuniecia: ")
        ilosc = int(input("Podaj ilosc produktu: "))
        obj.odejmijProdukt(produkt, ilosc)
    elif(dec == "K"):
        break



print("Podsumowanie koszyka klienta")
suma = 0.0
for produkt in obj.zakupy:

    suma += magazyn[produkt] * obj.zakupy[produkt]


print("Klient ma do zapłacenia "+str(suma))




