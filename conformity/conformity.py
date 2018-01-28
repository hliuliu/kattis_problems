
n=int(raw_input())

popl={}

for _ in xrange(n):
	comb=map(int,raw_input().split())
	comb.sort()
	comb=tuple(comb)
	popl[comb]=popl.get(comb,0)+1


m=max(popl.itervalues())
count=0
for v in popl.itervalues():
	if v==m:
		count+=m

print count

