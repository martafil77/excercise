from sys import stdout
a = int(raw_input())

for rozdziel_dane in range(a):
    b = input(raw_input().count())
    for slowo in range(b):
        for litery in range(c):
            if (slowo) % 2 == 0 :
                stdout.write(b)
        stdout.write("\n")
    print
