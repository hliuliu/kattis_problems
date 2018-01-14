

n=int(raw_input())

for _ in xrange(n):
	s,d=map(int,raw_input().split())
	if d>s or (s+d)&1:
		print 'impossible'
	else:
		print (s+d)//2,(s-d)//2




