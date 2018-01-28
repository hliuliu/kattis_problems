
t=int(raw_input())

for i in xrange(1,t+1):
    r,c=map(int,raw_input().split())
    pic=[raw_input() for j in xrange(r)]
    pic.reverse()
    print 'Test',i
    for j in xrange(r):
        print ''.join(reversed(pic[j]))
