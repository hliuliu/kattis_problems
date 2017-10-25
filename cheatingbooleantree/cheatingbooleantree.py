
n=int(raw_input())


def buildtree(tree,gates,parent):
	if parent>=len(gates):
		return
	buildtree(tree,gates,parent*2)
	buildtree(tree,gates,parent*2+1)
	if gates[parent]&2:
		#and gate
		tree[parent]=int(0 not in [tree[parent*2],tree[parent*2+1]])
	else:
		#or gate
		tree[parent]=int(1 in [tree[parent*2],tree[parent*2+1]])

def doall(*args):
	if 'IMPOSSIBLE' in args:
		return 'IMPOSSIBLE'
	return sum(args)
def doany(*args):
	return min(args)


def minchange(tree,gates,pos,v):
	if pos>=len(gates):
		return 0 if tree[pos]==v else 'IMPOSSIBLE'
	if tree[pos]==v:
		return 0
	l0=minchange(tree,gates,pos*2,0)
	l1=minchange(tree,gates,pos*2,1)
	r0=minchange(tree,gates,pos*2+1,0)
	r1=minchange(tree,gates,pos*2+1,1)
	status=gates[pos]&2
	if gates[pos]&1:
		#changable
		if status and v:
			# and gate, 0 to 1
			return doany(
				doall(l1,r1),# keep and gate
				doall(doany(l1,r1),1) # change to or gate
				)
		if status:
			# and gate, 1 to 0
			return doany(l0,r0) # keep and gate
		if v:
			# or gate, 0 to 1
			return doany(l1,r1) # keep or gate
		# or gate, 1 to 0
		return doany(
			doall(l0,r0), # keep or gate
			doall(doany(l0,r0),1) # change to and gate
			)
	if status and v:
		return doall(l1,r1)
	if status:
		return doany(l0,r0)
	if v:
		return doany(l1,r1)
	return doall(l0,r0)





def compute(casenum):
	m,v=map(int,raw_input().split())
	tree=[0]*(m+1)
	gates=[0]*(m/2+1)
	for i in xrange(1,len(gates)):
		g,c=map(int,raw_input().split())
		gates[i]=(g<<1)+c
	for i in xrange(len(gates),len(tree)):
		tree[i]=int(raw_input())
	buildtree(tree,gates,1)
	#print tree
	ans=minchange(tree,gates,1,v)
	print 'Case #%d:'%casenum, ans







for i in xrange(n):
	compute(i+1)




