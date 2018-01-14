
from math import sqrt

d,n=map(float,raw_input().split())

n=int(n)

def dist(p1,p2):
	x1,y1=p1
	x2,y2=p2
	return sqrt((x1-x2)**2+(y1-y2)**2)

while n:
	hives=[map(float,raw_input().split()) for _ in xrange(n)]
	sour=[False]*n
	for i in xrange(n):
		for j in xrange(i+1,n):
			if dist(hives[i],hives[j])<=d:
				sour[i]=True
				sour[j]=True
	ns=sour.count(True)
	print ns,'sour,',n-ns,'sweet'
	d,n=map(float,raw_input().split())
	n=int(n)



