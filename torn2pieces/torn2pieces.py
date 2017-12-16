
# Accepted :)


graph={}


def dfs(G,u,v,path,visited=set()):
	visited.add(u)
	path.append(u)
	if u==v:
		return True
	if u not in G:
		path.pop()
		visited.discard(u)
		return False
	for w in G[u]:
		if w not in visited:
			if dfs(G,w,v,path,visited):
				return True
	path.pop()
	visited.discard(u)
	return False



n=int(raw_input())

for _ in xrange(n):
	vs=raw_input().split()
	for v in vs:
		if v not in graph:
			graph[v]=set()
	v1=vs[0]
	vs=vs[1:]
	for v in vs:
		graph[v1].add(v)
		graph[v].add(v1)


u,v=raw_input().split()

path=[]
if dfs(graph,u,v,path):
	print ' '.join(path)
else:
	print 'no route found'






