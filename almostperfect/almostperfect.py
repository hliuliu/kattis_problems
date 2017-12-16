


def tosqrtprimes(n):
	rootn=1
	odd=1
	osum=1
	while osum<n:
		rootn+=1
		odd+=2
		osum+=odd
	sieve=[True]*(rootn+1)
	primes=[]
	p=2
	while p<=rootn:
		if not sieve[p]:
			p+=1
			continue
		primes.append(p)
		i=p*p
		while i<=rootn:
			sieve[i]=False
			i+=p
		p+=1
	return primes


primes=tosqrtprimes(10**9)


while 1:
	try:
		n=int(raw_input())
		m=n
		factors={}
		for p in primes:
			while n%p==0:
				n//=p
				factors[p]=factors.get(p,0)+1
			if n<p:
				break
		sd=1
		for p,k  in factors.iteritems():
			sd*=(p**(k+1)-1)//(p-1)
		sd=sd-m
		diff=abs(m-sd)
		print m, ('perfect' if diff==0 else 'almost perfect' if diff<=2 else 'not perfect')
	except EOFError:
		break







