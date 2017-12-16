


symbols='+-*/'


def gen(n):
	L=[]
	if not n:
		yield L
	else:
		for s in symbols:
			for L in gen(n-1):
				yield [s]+L


m= int(raw_input())

for i in xrange(m):
	n=int(raw_input())
	for L in gen(3):
		sol='4'.join(L)
		sol='4'+sol+'4'
		sol=' '.join(sol)
		if eval(sol)==n:
			print sol,'= %d'%n
			break
	else:
		print 'no solution'







