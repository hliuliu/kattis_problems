

ci=[1]

for i in xrange(1,1001):
	ci.append(2*(2*i-1)*ci[-1]//(i+1))

print ci[-1]>10**18

def nextp(pref,used,n):
	if used==0:
		pref.extend('()')
		return pref,1
	if used<n:
		end = pref.pop()
		pref.extend('()')
		pref.append(end)
		return pref,used+1
	i=len(pref)-1
	lcount=0
	while i>=0 and (lcount==0 or pref[i]=='('):
		if pref[i]=='(':
			lcount+=1
		i-=1
	if i<0:
		return 'error',-1 # shouldn't reach here
	lcount = used-lcount
	if i==lcount:
		pref[i]='('
		pref[i+1:]=[]
		used = len(pref)
		pref.extend(')'*used)
		return pref,used
	pref[i]='('
	lcount+=1
	i+=1
	rcount = i-lcount
	while rcount<lcount:
		pref[i]=')'
		i+=1
		rcount+=1
	pref[i:]=[]
	used=lcount
	return pref,used
	







def gen(n,m):
	if n==0:
		return ''
	if n==1:
		return '()'
	counter = ci[n]
	pref = []
	used = 0
	while m<=counter:
		pref,used = nextp(pref,used,n)
		counter -= ci[n-used]
		# print ''.join(pref)
		# print n
		# print isbal(pref)
		# print pref,n
	m-=counter
	# print used
	return ''.join(pref)+gen(n-used,m)


def isbal(paren):
	stack = 0
	for p in paren:
		stack+= 1 if p=='(' else -1
	return stack==0


n,m = map(int,raw_input().split())

print gen(n/2,m)




