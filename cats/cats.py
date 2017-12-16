



class uf(object):
	def __init__(self,n):
		self.n=n
		self.parent=range(n)
		self.size=[1]*n
	def find(self,u):
		while u!=self.parent[u]:
			self.parent[u]=self.parent[self.parent[u]]
			u=self.parent[u]
		return u
	def union(self,u,v):
		u,v=map(self.find,[u,v])
		u,v=sorted([u,v],key=lambda x: self.size[x])
		self.parent[u]=v
		self.size[v]+=self.size[u]
	def connected(self,u,v):
		return self.find(u)==self.find(v)



def find_min_cand(Q,G,costs):
	low,li=costs[Q[0]],Q[0]
	for i in Q:
		if costs[i]<low:
			low=costs[i]
			li=i
	Q.remove(li)
	return li




def mwst(G):
	c=len(G)
	# prims with adjacency matrix (O(V^2))
	costs=[float('inf')]*c
	edges=[None]*c
	#F=set()
	Q=range(c)
	while Q:
		v=find_min_cand(Q,G,costs)
		#F.add(v)
		if edges[v]!=None:
			yield (v,edges[v])
			#F.add(edges[v])
		for w in Q:
			if G[v][w]<costs[w]:
				costs[w]=G[v][w]
				edges[w]=v











def wt_graph():
	m,c=map(int,raw_input().split())
	G=[[0]*c for _ in xrange(c)]
	for _ in xrange(c*(c-1)/2):
		i,j,d=map(int,raw_input().split())
		G[i][j]=d
		G[j][i]=d
	return m,G


def possible(m,G):
	tree=mwst(G)
	ans=len(G)
	for u,v in tree:
		ans+=G[u][v]
	#print ans
	return ans<=m





t=int(raw_input())

for _ in xrange(t):
	m,G=wt_graph()
	res=possible(m,G)
	print 'yes' if res else 'no'



