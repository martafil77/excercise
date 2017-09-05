

y = 20
a = 0
b = 12

if a == 0 :
    print "Nie mozna dzielic przez zero. Koniec programu."


if a != 0:
    print "y = ax + b"
    print "%d = %dx + %d" % (y, a, b )
    print "%dx = %d - %d" % (a, y, b )
    wynik1 = float(y - b)
    print "%dx = %d" % (a, wynik1)
    x = float(y - b) / a
    print "x = %d/%d" % (wynik1, a )
    wynik2 = float(wynik1 / a)
    print "x = %.11f" % (wynik2 )

    y, a, b = 20, 0, 12
    x = float(y - b) / a
    print('x = ' + str(x))
