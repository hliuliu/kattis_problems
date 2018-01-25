




def bfs(G,n,numitems):
	start=1
	#visited=[False]*(n+1)
	#used=[False]*(n+1)
	#visited[start]=True
	track=[(float('inf'),1)]*(n+1)
	track[start]=(0,-numitems[start])
	q=[start]
	while q:
		ci=q.pop(0)
		sp,ni=track[ci]
		#used[ci]=True
		for nbr in xrange(1,n+1):
			if G[ci][nbr]:
				newpair=(sp+G[ci][nbr],ni-numitems[nbr])
				if track[nbr]>newpair:
					track[nbr]=newpair
					q.append(nbr)
					#visited[nbr]=True
	s,i=track[n]
	#debug_print(track)
	return s,-i



def debug_print(track):
	for i,j in enumerate(track):
		print i,j






n= int(raw_input())

numitems=[0]+map(int,raw_input().split())

G=[[0]*(n+1) for _ in xrange(n+1)]

m=int(raw_input())

for _ in xrange(m):
	a,b,d=map(int,raw_input().split())
	G[a][b]=d
	G[b][a]=d

p,q=bfs(G,n,numitems)

if q<0:
	print 'impossible'
else:
	print p,q






