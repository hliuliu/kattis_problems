

t=int(raw_input())



for _ in xrange(t):
	raw_input()
	n=int(raw_input())
	print 'YES' if sum([int(raw_input()) for _ in xrange(n)])%n==0 else 'NO'


	



