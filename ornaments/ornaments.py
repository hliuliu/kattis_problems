
from math import sqrt, acos, pi

while 1:
	r,h,s = map(int, raw_input().split())
	if r==0:
		break
	theta = acos(r/float(h))
	l = 2*(1+s/100.)*(pi*r-theta*r+sqrt(h*h-r*r))
	print '%.2f'%l



