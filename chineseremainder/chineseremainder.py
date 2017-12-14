

def egcd(m,n):
	if m<n:
		(d,y,x)=egcd(n,m)
		return d,x,y
	if n==0:
		return m,1,0
	q,r = divmod(m,n)
	d,a,b = egcd(n,r)
	return d,b,a-b*q


t= int(raw_input())

for _ in xrange(t):
	a,n,b,m = map(int,raw_input().split())
	d,x,y = egcd(n,m)
	x*=(b-a)
	k=m*n
	print (n*x+a)%k,k


