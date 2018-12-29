


n,s,t = map(int, raw_input().split())

G = [map(int,raw_input().split()) for _ in xrange(n)]


def sp(n,s,t,G):
	if s==t:
		return 0
	dist = [float('inf')]*n
	vis = {s}
	unvis = set(xrange(n))-vis
	
	dist[s] = 0

	while unvis:
		for u in unvis:
			for v in vis:
				if dist[u]>dist[v]+G[v][u]:
					dist[u] = dist[v]+G[v][u]
		u = min(unvis, key=lambda u:dist[u])
		vis.add(u)
		unvis.discard(u)
		if u==t:
			return dist[t]



print sp(n,s,t,G)









