for i in range(int(raw_input())):
    a, b = map(int, raw_input().strip().split(' '))
    w = 1 + 3 * b
    patt = '*' + '..*' * b
    line = '*' * w
    print line
    for _ in range(a):
        print patt
        print patt
        print line
    print 
