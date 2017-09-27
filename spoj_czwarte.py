def polowa(slowo):
    ilosc_znakow = len(slowo)
    polowa = slowo[0:ilosc_znakow/2]
    return polowa


def co_drugie(slowo):
    index = 0
    wynik = ''
    for znak in slowo:
        if index % 2 == 0:
            wynik = wynik + znak
        index = index + 1
    return wynik

def zadanie(slowo):
    return co_drugie(polowa(slowo))

ile_testow = int(raw_input())
for test in range(ile_testow):
    slowo = raw_input()
    litery = zadanie(slowo)
    print litery


# to samo inaczej:

#line = raw_input()
#print line[:len(line)/2:2]
