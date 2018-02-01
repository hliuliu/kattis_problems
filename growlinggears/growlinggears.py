


m= int(raw_input())

for _ in xrange(m):
	n=int(raw_input())
	gear=0
	ctmax=0
	for i in xrange(1,n+1):
		a,b,c=map(int,raw_input().split())
		tmax=c+(b**2)/4/a
		#print tmax
		if tmax>ctmax:
			gear=i
			ctmax=tmax
	print gear



