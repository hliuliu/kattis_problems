
# TLE?


inf=float('inf')
import copy#,time

#start=time.time()

def run_query(s,qs,G):
	n=len(G)
	wt=dict()
	wt[s]=0
	incl=set()
	exl=dict()
	exl[s]=0
	#print exl
	while exl:
		u,du=min(exl.iteritems(),key=lambda x:x[1])
		incl.add(u)
		del exl[u]
		for v in dict(G[u]):
			if wt.get(v,inf)>du+G[u][v]:
				wt[v]=du+G[u][v]
				exl[v]=wt[v]
			del G[u][v]
	for q in qs:
		if q in wt:
			print wt[q]
		else:
			print 'Impossible'








line =raw_input()

n,m,q,s=map(int,line.split())

graph={i:{} for i in xrange(n)}



while any([n,m,q,s]):
	for i in xrange(m):
		u,v,w=map(int,raw_input().split())
		graph[u][v]=w
	queries=[]
	for i in xrange(q):
		queries.append(int(raw_input()))
	run_query(s,queries,graph)
	line =raw_input()
	#print queries
	n,m,q,s=map(int,line.split())
	for i in graph:
		graph[i]={}
	print

#end=time.time()

#print "time", end-start


