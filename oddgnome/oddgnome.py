
n = int(raw_input())

while n:
	n-=1
	g = map(int,raw_input().split())
	for i in xrange(2,len(g)-1):
		if g[i-1]<g[i+1] and not g[i-1]<g[i]<g[i+1]:
			print i
			break



