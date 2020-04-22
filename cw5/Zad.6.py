class Slowa:
    slowo1 = "pierwsze"
    slowo2 = "drugie"

    def sprawdzCzyPalindrom(wyraz):
        for i in range(0, len(wyraz)):
            if wyraz[i] == wyraz[len(wyraz) - i]:
                print wyraz[i] + " ? " + wyraz[len(wyraz - i)] + ("\n")
            else:
                return False
        return True

    def sprawdzCzyAnagram(self):
        for i in range(0, len(self.slowo1)):
            helpdesk = True
            for j in range(0, len(self.slowo2)):
                if self.slowo1[i] == self.slowo2[j]:
                    helpdesk = False
            if helpdesk: return False
        return True

    def sprawdzCzyMetagram(self):
        helpdesk1 = 0
        for i in range(0, len(self.slowo1)):

            for j in range(0, len(self.slowo2)):
                if self.slowo1[i] == self.slowo2[j]:
                    print ""
                else:
                    helpdesk1 += 1
            if helpdesk1 != 1:
                return False
            else:
                return True

    def wyswietlWyrazy(self):
        print self.slowo1 + " " + self.slowo2
