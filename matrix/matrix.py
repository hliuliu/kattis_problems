

cnum =1
while 1:
	try:
		[[a,b],[c,d]] = [map(int,raw_input().split()) for _ in [0,0] ]
		raw_input()
		det = a*d-b*c
		m = [[d/det,-b/det],[-c/det,a/det]]
		print 'Case {}:'.format(cnum)
		for i,j in m:
			print i,j
		cnum += 1

	except EOFError:
		break


