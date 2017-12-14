
modval=1000000007

bits=[1]

for _ in xrange(500001):
	bits.append((bits[-1]<<1)%modval)

line=raw_input()
n=len(line)

nz=[0]*n
nq=[0]*n

i=n-2

while i>=0:
	if line[i+1]=='0':
		nz[i]=nz[i+1]+1
	else:
		nz[i]=nz[i+1]
	if line[i+1]=='?':
		nq[i]=nq[i+1]+1
	else:
		nq[i]=nq[i+1]
	i-=1

ans=0
for i in xrange(n-2,-1,-1):
	if line[i]!='0':
		if line[i]=='?':
			ans<<=1
			ans%=modval
		ans+=nz[i]*(bits[nq[i]])%modval
		if nq[i]:
			ans+=nq[i]*(bits[nq[i]-1])%modval
		ans%=modval

print ans




