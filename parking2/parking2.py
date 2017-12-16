

n=int(raw_input())

for i in xrange(n):
    raw_input()
    stores=map(int,raw_input().split())
    print 2*(max(stores)-min(stores))


