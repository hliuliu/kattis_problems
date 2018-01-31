


LIM=32000

sieve=[True]*LIM

for i in xrange(2,LIM):
	if not sieve[i]:
		continue
	for j in xrange(i*i,LIM,i):
		sieve[j]=False




def goldb(x):
	count=0
	reps=[]
	for i in xrange(2,x//2+1):
		if sieve[i] and sieve[x-i]:
			reps.append((i,x-i))
			count+=1
	return count,reps




n=int(raw_input())

for _ in xrange(n):
	x=int(raw_input())
	num,seq=goldb(x)
	print '%d has %d representation(s)'%(x,num)
	for a,b in seq:
		print '%d+%d'%(a,b)
	print


