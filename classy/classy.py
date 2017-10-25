
rank = {'upper':-1,'middle':0,'lower':1}


t = int(raw_input())

for _ in xrange(t):
	n= int(raw_input())
	names = {}
	nlist=[]

	for __ in xrange(n):
		name, cl, _ = raw_input().split()
		names[name] = list(reversed(
			map(lambda x: rank[x],cl.split('-'))
			))
		nlist.append(name)

	l = max(map(len, names.values()))

	for n,c in names.iteritems():
		names[n].extend([0]*(l-len(c)))

	nlist.sort(key= lambda x: (names[x],x))

	for n in nlist:
		print n[:-1]
	print '='*30



