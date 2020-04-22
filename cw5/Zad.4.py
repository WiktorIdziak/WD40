class NaZakupy:
    def __init__(self , nazwaProduktu, ilosc, jednostkaMiary, cenaJed):
        self.nazwaProduktu=nazwaProduktu
        self.ilosc=ilosc
        self.jednostkaMiary=jednostkaMiary
        self.cenaJed=cenaJed
    def wyswietlProdukt(self):
        return self.nazwaProduktu
    def ileProduktu(self):
        return self.ilosc, self.jednostkaMiary
    def ileKosztuje(self):
        return self.ilosc*self.cenaJed

Zakupy=NaZakupy("Ziemniaki", 3, "Kilogram", 2)

print(Zakupy.wyswietlProdukt())
print(Zakupy.ileProduktu())
print(Zakupy.ileKosztuje())
