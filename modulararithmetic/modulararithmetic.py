

def get_tokens(toks):
	r,s,t=toks
	return int(r),s,int(t)

def extgcd(a,b):
	if not b:
		return 1,0,a
	s,r,d=extgcd(b,a%b)
	return r,s-r*(a//b),d

n,t=map(int,raw_input().split())

while n or t:
	for _ in xrange(t):
		x,op,y=get_tokens(raw_input().split())
		if op=='+':
			print (x+y)%n
		elif op=='-':
			print (x-y)%n
		elif op=='*':
			print (x*y)%n
		else:
			s,yinv,d=extgcd(n,y)
			if d>1:
				print -1
			else:
				print (x*yinv)%n
	n,t=map(int,raw_input().split())



