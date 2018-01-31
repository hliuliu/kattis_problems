

n=int(raw_input())

parent = [0]*(n+1)

value = [-1]*(n+1)


for i in xrange(1,n+1):
	value[i],parent[i]=map(int,raw_input.split())

maxsize=[1]*(n+1)
maxval = [-1]*(n+1)

for i in xrange(n+1):
	maxval[i]=value[i]

for i in xrange(n,0,-1):
	pari = parent[i]
	size = maxsize[i]
	if value[pari]>value[i]:
		size+=1 # can add this root to the subtree of pari
		maxval[pari] = value[pari]
	if size> maxsize[pari]:
		maxsize[pari]= size
		maxval[pari]= max(maxval[pari],maxval[i])
	

