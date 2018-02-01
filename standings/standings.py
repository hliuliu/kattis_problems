



t=int(raw_input())

for _ in xrange(t):
	raw_input()
	n=int(raw_input())
	rks=[int(raw_input().split()[1]) for __ in xrange(n)]
	rks.sort()
	bad=sum([abs(i-j) for i,j in enumerate(rks,1)])
	print bad

