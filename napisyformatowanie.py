imie = "Marta"
print "Witaj %s!" % imie

imie = "Marcin"
print "Witaj %s!" %imie

wiek = 100
print "%s ma %d lat!" % (imie, wiek)

dane = ("Marta", 22, 38)
print "%s ma %d lata i nosi rozmiar buta rowny %d" % dane

dane = ("Jacek", "Darek", 44.4)
formatowany_napis = "Czesc %s i %s. Temperatura na zewnatrz wynosi %.1f stopnie Celsjusza."

print formatowany_napis % dane
