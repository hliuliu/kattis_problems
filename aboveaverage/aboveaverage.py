



c= int(raw_input())

for _ in xrange(c):
    l = map(int, raw_input().split())
    n = l.pop(0)
    s = sum(l)
    ct =0
    for el in l:
        if el*n>s:
            ct += 1
    print '%.3f'%(ct*100./n)+'%'
