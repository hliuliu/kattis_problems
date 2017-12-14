from math import pi
r,m,c=map(float,raw_input().split())
#m,c=map(int,[m,c])

while any([r,m,c]):
	print pi*r**2,c/m*4*r**2
	r,m,c=map(float,raw_input().split())



