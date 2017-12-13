
from math import cos,pi

h,v  = map(int, raw_input().split())

theta = abs(v-270)

if theta>=90:
	print 'safe'
else:
	d = int(h/cos(theta*pi/180))
	print d


