

primes = []

for i in xrange(2,25):
	for p in primes:
		if not i%p:
			break
	else:
		primes.append(i)




def decomp(t,dv, incr=True):
	for p in primes:
		while not t%p:
			t//=p
			dv[p] += 1 if incr else -1
	if t>1:
		dv[t] = dv.get(t,0)+ (1 if incr else -1)
	



while 1:
	try:
		n,k = map(int, raw_input().split())
	except EOFError:
		break
	else:
		if k*2>n:
			k=n-k
		dv = {p:0 for p in primes}
		for i in xrange(k):
			decomp(n-i,dv)
			decomp(i+1,dv,False)
		ans = 1
		for v in dv.itervalues():
			ans *= v+1
		print ans





