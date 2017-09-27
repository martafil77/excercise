from sys import stdout


def zadanie(x, a, b):
  for pattern in range(x):
    for wiersz in range(a):
        for kolumna in range(b):
            if wiersz != 0 and kolumna % 3 != 0 and kolumna != b - 1:
                stdout.write(".")
            else:
                stdout.write("*")
        stdout.write("\n")
  print ("*" * b)
  print

zadanie(3, 3, 4)
zadanie(4, 3, 13)
zadanie(2, 3, 16)

#rozwiązanie Skiby
#for i in range(int(raw_input())):
    #a, b = map(int, raw_input().strip().split(' '))
    #w = 1 + 3 * b
    #patt = '*' + '..*' * b
    #line = '*' * w
    #print line
    #for _ in range(a):
        #print patt
        #print patt
        #print line
    #print 
