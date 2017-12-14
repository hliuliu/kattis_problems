

#tle 
#import time,sys


#start=time.time()

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

results={p:(p,1) for p in primes}

def compute(n,results):
	count=0
	nold=n
	factorsum=0
	if n in results:
		m,count=results[n]
		#results[nold]=(m,count)
		return m,count
	m=n
	while n>1:
		for p in primes:
			while n%p==0:
				n//=p
				factorsum+=p
			if n<p:
				break
	if factorsum==m:
		results[nold]=(m,count)
		return m,count
	n=factorsum
	m,count=compute(n,results)
	results[nold]=(m,count+1)
	return results[nold]
	#n=int(raw_input())


for n in xrange(2,200):
	if n!=4:
		compute(n,results)


for n in xrange(200,1000001,100):
	compute(n,results)

n=int(raw_input())
while n!=4:
	m,count=compute(n,results)
	print m,count
	#print 0,0
	n=int(raw_input())


#end=time.time()

#print >> sys.stderr, end-start


