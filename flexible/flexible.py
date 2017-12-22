

w,p=map(int,raw_input().split())


l=[0]+map(int,raw_input().split())+[w]

l.sort()

size=set()

for i in xrange(p+2):
	for j in xrange(i+1,p+2):
		size.add(l[j]-l[i])


print ' '.join(map(str,sorted(size)))


