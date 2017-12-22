


n= int(raw_input())

si = map(int,raw_input().split())


sieve=[True]*(n*1000+1)

sieve[0] = False
sieve[1] = False

for i in xrange(2,len(sieve)):
	if i**2>=len(sieve):
		break
	if not sieve[i]:
		continue
	for j in xrange(i**2,len(sieve),i):
		sieve[j]=False



distinctpf=[0]*(len(sieve))

for i in xrange(2,len(sieve)):
	if not sieve[i]:
		continue
	for j in xrange(i,len(sieve),i):
		distinctpf[j]+=1




partition= [0]*n

numparts = [1]*n

def revenue(partition,si):
	sprops = [0]*numparts[-1]
	for i in xrange(n):
		sprops[partition[i]]+=si[i]
	return sum([distinctpf[s] for s in sprops])

def next_partition(partition,index):
	if index==0:
		return False
	if partition[index]==numparts[index-1]:
		# last element all by itself
		# get next subpartition
		if not next_partition(partition,index-1):
			return False
		partition[index]=0
		numparts[index]=numparts[index-1]
		return True
	partition[index]+=1
	if numparts[index]==partition[index]:
		numparts[index]+=1
	return True


		





ans= revenue(partition,si)

while next_partition(partition,n-1):
	ans= max(ans,revenue(partition,si))

print ans



