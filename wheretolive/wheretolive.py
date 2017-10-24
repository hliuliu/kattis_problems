

def sqdist(x,y,a,b):
	return (x-a)**2+(y-b)**2

def sumdist(x,y,pts):
	return sum([sqdist(x,y,a,b) for a,b in pts])






n = int(raw_input())

while n:
	pts = [map(int,raw_input().split()) for _ in xrange(n)]
	sx,sy = map(sum,zip(*pts))
	ax = sx/n
	ay = sy/n
	cd = float('inf')
	cx,cy = ax,ay

	for x in xrange(ax,ax+2):
		for y in xrange(ay,ay+2):
			d= sumdist(x,y,pts)
			if d<cd:
				cx,cy = x,y
				cd = d

	print cx, cy
	n= int(raw_input())





