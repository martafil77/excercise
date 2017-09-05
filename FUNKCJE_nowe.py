def lista_korzysci():
    return tablica
tablica = ["Lepiej zorganizowany kod", "Wieksza czytelnosc kodu", "Latwiejsze wielokrotne uzycie kodu", "Mozliwosc dzielenia sie kodem i laczenia go w calosc przez rozne osoby"]

def buduj_zdanie(korzysc):
    return korzysc + " jest zaleta funkcji!"

def nazwij_korzysci_z_funkcji():
    tabela = lista_korzysci()
    for korzysc in tabela:
        print buduj_zdanie(korzysc)

nazwij_korzysci_z_funkcji()
