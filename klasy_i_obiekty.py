#gotowa klasa Pojazd

class Pojazd:
    nazwa = ""
    rodzaj = "auto"
    kolor = ""
    wartosc = 100.00
    def opis(self):
        napis_opisu = "%s to %s %s warty %.2f zl." % (self.nazwa, self.kolor, self.rodzaj, self.wartosc)
        return napis_opisu

# Ponizej umiesc swoj kod

Auto1 = Pojazd()
Auto1.nazwa = "Ferrari"
Auto1.rodzaj = "kabriolet"
Auto1.kolor = "czerwony"
Auto1.wartosc = 60000

Auto2 = Pojazd()
Auto2.nazwa = "Ikarus"
Auto2.rodzaj = "autobus"
Auto2.kolor = "niebieski"
Auto2.wartosc = 10000


# sprawdzenie kodu
print Auto1.opis()
print Auto2.opis()
