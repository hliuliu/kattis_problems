

p,t=map(int,raw_input().strip().split())

graph=[{} for i in xrange(p)]

for i in xrange(t):
	p1,p2,t=map(int,raw_input().strip().split())
	if p1==p2:
		continue
	for j,k in [(p1,p2),(p2,p1)]:
		if k not in graph[j]:
			graph[j][k]=[]
		graph[j][k].append(t)


for j in xrange(p):
	for k in graph[j]:
		m= min(graph[j][k])
		graph[j][k]=(m,graph[j][k].count(m))

# for j in xrange(p):
# 	print j, graph[j]



class node(object):
	def __init__(self,label):
		self.label=label
		self.prevs=[]
		self.dist=float('inf')

points=[node(i) for i in xrange(p)]

points[0].dist=0

expand={0}


def update(pt,k):
	w=graph[pt][k][0]+pt.dist
	if w<=points[k].dist:
		if w<points[k].dist:
			points[k].prevs=[]
		points[k].prevs.append(pt)
		points[k].dist=w



while len(expand)<p:
	for pt in expand:
		for k in graph[pt]:
			update(pt,k)





