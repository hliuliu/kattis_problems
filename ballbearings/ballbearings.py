

from math import acos,pi


n=int(raw_input())

for _ in xrange(n):
	D,d,s=map(float,raw_input().split())
	print int(2*pi/acos(1-2*(d+s)**2/(D-d)**2))


