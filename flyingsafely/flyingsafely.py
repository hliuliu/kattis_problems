

t = int(raw_input())

for _ in xrange(t):
	n, m = map(int, raw_input().split())

	G = {i: set() for i in xrange(1,n+1)}

	for _ in xrange(m):
		a,b = map(int,raw_input().split())
		G[a].add(b)
		G[b].add(a)

	print n-1


