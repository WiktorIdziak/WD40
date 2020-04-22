class Robaczek:

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idzWGore(self, ileKrokow):
        self.y = self.y + (self.krok*ileKrokow)

    def idzWDol(self, ileKrokow):
        self.y = self.y - (self.krok * ileKrokow)

    def idzWPrawo(self, ileKrokow):
        self.x = self.x + (self.krok * ileKrokow)

    def idzWLewo(self, ileKrokow):
        self.x = self.x - (self.krok * ileKrokow)

    def pokazGdzieJestes(self):
        print "x:" + self.x + " " + "y:" + self.y

    def __del__ (self):
        print "R.I.P Robaczek"
