def lista_korzysci():
    return tablica
tablica = ["Lepiej zorganizowany kod", "Wieksza czytelnosc kodu", "Latwiejsze wielokrotne uzycie kodu", "Mozliwosc dzielenia sie kodem i laczeia go w calosc przez rozne osoby"]

def buduj_zdanie(info):
    return info + " jest zaleta funkcji!"

tabela = lista_korzysci()

def koniec():
    for info in tabela:
        print buduj_zdanie(info)

koniec()
