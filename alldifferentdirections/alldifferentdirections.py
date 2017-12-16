

from math import sin,cos,pi,sqrt

n=int(raw_input())

def torad(angle):
	return pi*angle/180


def avg(dests):
	ax,ay=0,0
	for x,y in dests:
		ax+=x
		ay+=y
	return (i/len(dests) for i in [ax,ay])

def distsq(x1,y1,x2,y2):
	return (x1-x2)**2+(y1-y2)**2


while n:
	dests=[]
	for _ in xrange(n):
		dirs=raw_input().split()
		currx,curry=map(float,(dirs.pop(0) for __ in [0,0]))
		dirs.pop(0)
		currangle=float(dirs.pop(0))
		while dirs:
			com,num=dirs.pop(0),float(dirs.pop(0))
			if com=='start':
				currangle=num
			elif com=='turn':
				currangle+=num
			else:
				arad=torad(currangle)
				dx,dy=cos(arad),sin(arad)
				currx+=dx*num
				curry+=dy*num
		dests.append((currx,curry))
	ax,ay=avg(dests)
	print ax,ay,sqrt(max([distsq(x,y,ax,ay) for x,y in dests]))
	n=int(raw_input())



