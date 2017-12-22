

n= int(raw_input())

parent = [0]+map(int, raw_input().split())

q= int(raw_input())

counts= [1]*(n+1)


for i,j in enumerate(parent):
	while j>0:
		counts[j]+=1
		j= parent[j]



def isparent(p,c):
	while c>0:
		if c==p:
			return True
		c=parent[c]
	return False



for _ in xrange(q):
	toks = map(int, raw_input().split()[1:])
	toks=set(toks)
	childs = {t:set([c for c in toks if c!=t and isparent(t,c)]) for t in toks}

	for t in childs:
		if t in toks:
			for c in childs[t]:
				toks.discard(c)

	print sum([counts[t] for t in toks])

