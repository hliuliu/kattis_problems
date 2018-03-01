


n = int(raw_input())

for _ in xrange(n):
	a,b,c = sorted(map(int,raw_input().split()))
	print 'Possible' if c in [a+b,a*b] else 'Impossible'





