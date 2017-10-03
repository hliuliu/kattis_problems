




def solve(src,dest,n):
	G={}
	for _ in xrange(n):
		names = raw_input().split()
		for name in names:
			G[name] = G.get(name, {})
		for a in names:
			for b in names:
				if a!=b:
					G[a][b] = min(len(names), G[a].get(b,float('inf')))

	path = search(src,dest,n,G)
	if not path:
		return ['impossible']
	path[1].insert(0, str(path[0]))
	return path[1]


def search(src,dest,n,G):
	if not {src,dest}.issubset(set(G)):
		return
	parent = {v: None for v in G}
	dist = {v: float('inf') for v in G}
	parent[src]=src
	dist[src] = -1
	q= [src]
	while q:
		u= q.pop(0)
		k=dist[u]
		for x in G[u]:
			d = k+G[u][x]-1
			if d<dist[x]:
				dist[x]=d
				parent[x] =u
				q.append(x)
	if parent[dest] is not None:
		path = [dest]
		curr = dest
		while parent[curr]!=curr:
			path.insert(0,parent[curr])
			curr=parent[curr]
		return dist[dest], path





while 1:
	try:
		src,dest = raw_input().split()
	except EOFError:
		break
	else:
		n= int(raw_input())
		print ' '.join(solve(src,dest,n))


