

l1,l2=[map(int,raw_input().split()) for i in [0,1]]

d=sum(l1)-sum(l2)

if d<0:
    print 'Emma'
elif d>0:
    print 'Gunnar'
else:
    print 'Tie'
