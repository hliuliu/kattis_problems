
n=int(raw_input())

for _ in xrange(n):
	line=raw_input().split()
	sign=1
	if line.pop(0)=='B':
		sign=-1
	d,h,m=map(int,line)
	m+=(sign*d)%60
	h+=(sign*d)/60
	if m>=60:
		m-=60
		h+=1
	elif m<0:
		m+=60
		h-=1
	h%=24
	print h,m



