from sys import stdout
a = int(raw_input())

for rozdziel_dane in range(a):
    b, c = map(int, raw_input().split())
    for wiersz in range(b):
        for kolumna in range(c):
            if (wiersz + kolumna) % 2 == 0:
                stdout.write("*")
            else:
                stdout.write(".")
        stdout.write("\n")
    print
    
