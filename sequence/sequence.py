

n=int(raw_input())

lengths=[0]

def smallest_pf(n):
	i=2
	while True:
		if not n%i:
			return i
		i+=1

sieve=[0]*(n+1)

for nextnum in xrange(2,n+1):
	if sieve[nextnum]!=0:
		continue
	i=nextnum
	incr=nextnum*(nextnum-1)
	while i<n+1:
		if sieve[i]==0:
			sieve[i]=nextnum
		i+=incr

lengths.append(1)

for i in xrange(2,n+1):
	lengths.append(lengths[i/sieve[i]]+1)


def sequence(n):
	if n==1:
		return [1]
	l=sequence(n/sieve[n])
	l.append(n)
	return l

m= max(lengths) 

while lengths[n]<m:
	n-=1

print m
print ' '.join(map(str,sequence(n)))



