

def has_cycle(G,a,b):
	G[a][b] = 0
	G[b][a] = 0
	visited = [False]*len(G)
	q=[a]
	visited[a]=True
	while q:
		el =q.pop(0)
		for i in xrange(len(G)):
			if G[el][i] and not visited[i]:
				if i==b:
					G[a][b]=1
					G[b][a]=1
					return True
				visited[i]=True
				q.append(i)
	G[a][b] = 1
	G[b][a] = 1
	return False


def has_bridge(G):
	n=len(G)
	for i in xrange(n):
		for j in xrange(i+1,n):
			if G[i][j] and not has_cycle(G,i,j):
				return True
	return False



p,c=map(int,raw_input().split())

while p or c:
	G=[[0]*p for _ in xrange(p)]
	for _ in xrange(c):
		a,b= map(int,raw_input().split())
		G[a][b] = 1
		G[b][a] = 1
	print 'Yes' if has_bridge(G) else 'No'
	p,c=map(int,raw_input().split())



