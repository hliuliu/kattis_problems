
from random import randint as rint

n,r,w,h = 10**5,10,10**9,10**9

print n,r,w,h

pair = set()

for _ in xrange(n):
	while 1:
		x, y= rint(0,w), rint(1,h)
		if (x,y) not in pair:
			print x,y
			pair.add((x,y))
			break


