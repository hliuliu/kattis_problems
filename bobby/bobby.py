
import sys
from fractions import Fraction as frac

n=int(raw_input())

def comb(n,r):
	for i in [n,r]:
		if type(i) not in [int,long]:
			raise TypeError
		if i<0:
			return 0
	if r>n:
		return 0
	if r==n:
		return 1
	nhalf=n/2
	if r<nhalf:
		r=n-r
	ans=1
	for i in xrange(r+1,n+1):
		ans*=i
		ans/=(i-r)
	return ans

def probfn(r,s,x,y,w):
	p=frac()
	for i in xrange(x,y+1):
		p+=comb(y,i)*(frac(s-r+1,s))**i*(frac(r-1,s))**(y-i)
	pf=frac(1)-p
	return p*(w-1)-pf>0

for i in xrange(n):
	r,s,x,y,w=map(int,raw_input().split())
	a=probfn(r,s,x,y,w)
	print 'yes' if a else 'no'
