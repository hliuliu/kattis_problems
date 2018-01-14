

def tobase(n,b):
	digits=[]
	while n:
		digits.append(str(n%b))
		n/=b
	digits.reverse()
	if not digits:
		return '0'
	return ''.join(digits)


line = raw_input().split()

while len(line)==3:
	b,p,m = line
	b=int(b)
	p=int(p,b)
	m=int(m,b)
	p%=m
	print tobase(p,b)
	line = raw_input().split()


