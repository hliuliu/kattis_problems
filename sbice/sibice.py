

n,w,h=map(int,raw_input().split())

dsq=w**2+h**2

for _ in xrange(n):
	x=int(raw_input())
	if x**2<=dsq:
		print 'DA'
	else:
		print 'NE'

