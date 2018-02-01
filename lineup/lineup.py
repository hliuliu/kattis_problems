
n=int(raw_input())


names=[raw_input() for _ in xrange(n)]

alph=sorted(names)

if names==alph:
	print 'INCREASING'
else:
	alph.reverse()
	if names==alph:
		print 'DECREASING'
	else:
		print 'NEITHER'


