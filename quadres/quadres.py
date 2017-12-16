


def modexp(a,n,p):
	if n==0:
		return 1
	ans=modexp(a,n>>1,p)
	ans**=2
	ans%=p
	if n&1:
		ans=(ans*a)%p
	return ans





def hassol(a,p):
	if p==2 or not a:
		return True
	n=(p-1)//2
	return modexp(a,n,p)==1



msg= {False:'no',True:'yes'}

n= int(raw_input())

for _ in xrange(n):
	a,p=map(int,raw_input().split())
	a=a%p
	print msg[hassol(a,p)]




