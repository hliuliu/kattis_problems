
from math import floor,ceil

def nz(n):
	if n==0:
		return 1
	ans= 0
	while n:
		if n%10==0:
			ans+=1
		n//=10
	return ans

def f(a,b):
	if a>b:
		return 0
	if b<10:
		return int(a==0)
	if a==0:
		return 1+ f(10,b)
	if a<10:
		return f(10,b)
	ans  = 0

	if b-a<=10:
		for i in xrange(a,b+1):
			ans+=nz(i)
		return ans

	while a%10:
		ans+=nz(a)
		a+=1
	while b%10:
		ans+=nz(b)
		b-=1
	ans+=f(a/10,b/10-1)*10
	ans+=b/10-a/10+nz(b)
	return ans



a,b = map(int,raw_input().split())

while a>=0:
	print f(a,b)
	a,b = map(int,raw_input().split())





