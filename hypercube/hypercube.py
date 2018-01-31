


def position(n,s):
	if n==1:
		return int(s)
	l,s=s[0],s[1:]
	recpos=position(n-1,s)
	if l=='0':
		return recpos
	return (1<<n)-1-recpos




n,a,b=raw_input().split()
n=int(n)


print position(n,b)-position(n,a)-1






