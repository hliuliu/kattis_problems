


def findnum(n):
	if n==1:
		return '1'
	if n==2:
		return '11'
	nd=0
	acc=0
	while acc<n:
		nd+=1
		acc+=1<<((nd-1)>>1)
	if acc>=n:
		acc-=1<<((nd-1)>>1)
	n-=acc
	n-=1
	nb=bin(n)[2:]
	#print bin(n),n
	nb=('0'*(((nd-1)>>1)-len(nb)))+nb
	nb=''.join(reversed(nb))
	if nd&1:
		return '1'+(''.join(reversed(nb[1:])))+nb+'1'
	return '1'+(''.join(reversed(nb)))+nb+'1'


print int(findnum(int(raw_input())),base=2)


