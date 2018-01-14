
def bfs(G,src,dest):
	n= len(G)
	if src==dest:
		return True
	q =[src]
	vis = [False]*n
	vis[src]=True
	while q:
		u = q.pop(0)
		for v in xrange(n):
			if G[u][v] and not vis[v]:
				if v==dest:
					return True
				vis[v] = True
				q.append(v)
	return False


def dist(p1,p2):
	return sum([abs(s-t) for s,t in zip(p1,p2)])


t = int(raw_input())

while t:
	t-=1
	n = int(raw_input())+2
	pts = [map(int, raw_input().split()) for _ in xrange(n)]
	G = [[i!=j and dist(pts[i],pts[j])<=1000 for j in xrange(n)] for i in xrange(n)]
	print 'happy' if bfs(G,0,n-1) else 'sad'






