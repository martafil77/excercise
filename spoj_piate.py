from sys import stdout

x = 3
a = 3
b = 4

for pattern in range(x):
    for wiersz in range(a):
        for kolumna in range(b):
            if wiersz != 0 and kolumna != 0 and kolumna != b - 1:
                stdout.write(".")
            else:
                stdout.write("*")
        stdout.write("\n")
print ("*" * b)
print
c = 4
d = 3
e = 13

for pattern in range(c):
    for wiersz in range(d):
        for kolumna in range(e):
            if wiersz != 0 and kolumna != 0 and kolumna != e - 1 and kolumna != 3 and kolumna != 6 and kolumna != 9:
                stdout.write(".")
            else:
                stdout.write("*")
        stdout.write("\n")
print ("*" * e)
print

f = 2
g = 3
h = 16

for pattern in range(f):
    for wiersz in range(g):
        for kolumna in range(h):
            if wiersz != 0 and kolumna != 0 and kolumna != h - 1 and kolumna != 3 and kolumna != 6 and kolumna != 9 and kolumna != 12:
                stdout.write(".")
            else:
                stdout.write("*")
        stdout.write("\n")
print ("*" * h)
print
