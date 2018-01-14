from math import sqrt

t = int(raw_input())

while t:
	t-=1
	x,y = map(int, raw_input().split())
	h= x+y-sqrt(x*x+y*y-x*y)
	h/=6
	print h*(x-2*h)*(y-2*h)


