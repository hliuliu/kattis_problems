

p=int(raw_input())

for _ in xrange(p):
	k,n=map(int,raw_input().split())
	print k,n*(n+1)/2,n**2,n*(n+1)

