
from math import sqrt,pi

def distsq(x1,y1,x2,y2):
	return (x2-x1)**2+(y2-y1)**2

c=int(raw_input())

for __ in xrange(c):

	paints=[]

	n=int(raw_input())

	for _ in xrange(n):
		line=raw_input().split()
		x,y,v=map(float,line[:-1])
		col=line[-1]
		#rsq=v/pi
		paints.append((x,y,v,col))

	m=int(raw_input())

	for _ in xrange(m):
		x,y=map(float,raw_input().split())
		col='white'
		for x0,y0,v0,col0 in paints:
			if pi*distsq(x,y,x0,y0)<=v0:
				col=col0
		print col






