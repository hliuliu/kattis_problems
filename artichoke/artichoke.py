
from math import sin,cos

p,a,b,c,d,n=map(int,raw_input().split())


def price(k):
	return p*(sin(a*k+b)+cos(c*k+d)+2)


prices=[price(i+1) for i in xrange(n)]

maxp=[0]

for pr in prices:
	maxp.append(max(pr,maxp[-1]))

maxp.pop(0)

print max((i-j for i,j in zip(maxp,prices)))





