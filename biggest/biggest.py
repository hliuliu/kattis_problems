
from math import pi

t = int(raw_input())

for _ in xrange(t):
	r,n,d,m,s = map(int, raw_input().split())
	theta = 3600*d+60*m+s # in unit of 1/3600 degrees
	cut=set()
	curr = 0
	for __ in xrange(n):
		if curr in cut:
			break
		cut.add(curr)
		curr+=theta
		curr%=360*3600
	cut =  sorted(cut)
	cut.append(cut[0]+360*3600)
	cutdiff=[cut[i+1]-cut[i] for i in xrange(len(cut)-1)]
	maxdiff= max(cutdiff)
	maxdiff/=3600.0 # in degrees
	maxdiff*= pi/180 # in radians
	print maxdiff/2*r**2



