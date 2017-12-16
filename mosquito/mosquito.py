

while 1:
	try:
		m,p,l,e,r,s,n=map(int,raw_input().split())
		for i in xrange(n):
			m,p,l=p/s,l/r,e*m
		print m
	except EOFError:
		break


