

from fractions import Fraction as frac


def gcd2(x,y):
	y,x=sorted([x,y])
	while y:
		r=x%y
		x,y=y,r
	return x

def gcd(xs):
	d=0
	for x in xs:
		d=gcd2(d,x)
	return d



def nonzeroes(A,b):
	for row in A:
		for entry in row:
			if entry:
				yield entry
	for entry in b:
		if entry:
			yield entry



row=map(int,raw_input().split())

while row!=[0]*3:
	A=[row]
	for _ in [1,2]:
		A.append(map(int,raw_input().split()))
	b=map(int,raw_input().split())
	raw_input()
	A.append(b)
	for r in A:
		r[:]=map(frac,r)
	rref(A)

	row=map(int,raw_input().split())



