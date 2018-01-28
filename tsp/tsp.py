
def GreedyTour(n):
	tour=[0]*n
	used=[False]*n
	used[0] = True
	print 0
	for i in xrange(1,n):
		best = -1
		for j in xrange(n):
			if not used[j] and (best == -1 or dist(pts[tour[i-1]],pts[j]) < dist(pts[tour[i-1]],pts[best])): 
				best = j
		tour[i] = best
		print best
		used[best] = True
	return tour


n=int(raw_input())

pts=[]

def dist(p1,p2):
	(x1,y1),(x2,y2)=p1,p2
	return (x2-x1)**2+(y2-y1)**2

for i in xrange(n):
	pts.append(map(float,raw_input().split()))
GreedyTour(n)




