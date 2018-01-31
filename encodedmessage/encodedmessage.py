
n=int(raw_input())

for i in xrange(n):
	line=raw_input()
	m=int(len(line)**0.5)
	sq=[list(line[j*m:(j+1)*m]) for j in xrange(m)]
	for s in sq:
		s.reverse()
	sq= zip(*sq)
	sq= [''.join(s) for s in sq]
	print ''.join(sq)
