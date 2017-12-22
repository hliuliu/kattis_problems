





import sys,math

for line in sys.stdin:
	line= line.strip()
	if line:
		r,x,y=map(float,line.split())
		if x*x+y*y>r*r:
			print 'miss'
		else:
			distsqr = x*x+y*y
			dist = math.sqrt(distsqr)
			theta= math.acos(dist/r)*2
			sector = theta*r*r/2
			triangle= dist*math.sqrt(r*r-dist*dist)
			big=triangle+(math.pi*r*r-sector)
			small = math.pi*r*r-big
			print big,small










