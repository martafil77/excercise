

def imie(imie):
    if (imie.endwith ("a")):
        return "t"
    else:
        return "n"


x=raw_input("Jak masz na imie ? " )
if imie(x)=="t":
    print "Jestes kobieta"
else:
    print "Jestes mezczyzna"


imie()
