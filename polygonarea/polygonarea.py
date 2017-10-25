

from math import sqrt
'''
def dist(p1,p2):
	x1,y1=p1
	x2,y2=p2
	return sqrt((x1-x2)**2+(y1-y2)**2)

def tri_area(p1,p2,p3):
	a = dist(p1,p2)
	b = dist(p1,p3)
	c = dist(p2,p3)
	s= sum([a,b,c])/2.0
	return sqrt(s*(s-a)*(s-b)*(s-c))

def getdir(p1,p2,p3):
	(x1,y1),(x2,y2),(x3,y3)=p1,p2,p3
	mat=[]
	mat.append([x2-x1,y2-y1])
	mat.append([x3-x2,y3-y2])
	[a,b],[c,d]=mat
	det = a*d-b*c
	if det>0:
		return 'CCW'
	return 'CW'

def coilinear(e,x,y):
	(x1,y1),(x2,y2)=e
	a,b,c,d = x2-x1,y2-y1,x1-x,y1-y
	return a*d==b*c

def intersect_right(e,x,y):
	(x1,y1),(x2,y2)=sorted(e)
	if not x1<=x<=x2:
		return False
	if x1==x2:
		return max(y1,y2)>=y
	t=(x-x2)/float(x1-x2)
	yint = t*y1+(1-t)*y2
	return yint>=y


def inside(pt,polygon):
	x,y=pt
	edges=[]
	for i in xrange(len(polygon)-1):
		edges.append(polygon[i:i+2])
	if len(polygon)>=3:
		edges.append([polygon[0],polygon[-1]])
	count=0
	for e in edges:
		if coilinear(e,x,y):
			(x1,y1),(x2,y2)=e
			x1,x2=sorted([x1,x2])
			return x1<=x<=x2
		if intersect_right(e,x,y):
			count+=1
	return count&1



def poly_area(polygon):
	area = 0.0
	p1,p2 = (polygon.pop(0) for _ in [0,0])
	subpoly = [p1,p2]
	for p3 in polygon:
		if inside(p3,subpoly):
			area-=tri_area(p1,p2,p3)
		else:
			area+=tri_area(p1,p2,p3)
		subpoly.append(p3)
		p2 = p3
	return area

'''

def cross(a,b):
	xa,ya=a
	xb,yb=b
	return xa*yb-ya*xb

def signed_area(polygon):
	polygon.append(polygon[0])
	area=0.0
	for i in xrange(len(polygon)-1):
		area+= cross(polygon[i],polygon[i+1])
	return area/2.0


n=int(raw_input())

while n:
	polygon = [map(int,raw_input().split()) for _ in xrange(n)]
	area = signed_area(polygon)
	print 'CCW' if area>=0 else 'CW', '%.1f'%abs(area)
	n=int(raw_input())


