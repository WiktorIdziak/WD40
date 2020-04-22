class Ciag:
    a = 0
    b = 0
    c = 0

    def wyswietlDane(self):
        return self

    def pobierzElementy(self):
        self.a = int(raw_input("Podaj a:"))
        self.b = int(raw_input("Podaj b:"))
        self.c = int(raw_input("Podaj c:"))

    def policzSume(self):
        return self.a + self.b + self.c
