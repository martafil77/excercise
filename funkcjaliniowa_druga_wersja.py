
def funkcjaliniowa(y, a, b ):
    if a:
         "%d = %dx + %d" % (y, a, b )
         "%dx = %d - %d" % (a, y, b )
         wynik1 = float(y - b)
         "%dx = %d" % (a, wynik1)
         x = float(y - b) / a
         "x = %d/%d" % (wynik1, a )
         wynik2 = float(wynik1 / a)
         print "x = %.11f" % (wynik2 )
    else:
         print "Nie ma rozwiazania"


funkcjaliniowa(20, 0, 12 )
