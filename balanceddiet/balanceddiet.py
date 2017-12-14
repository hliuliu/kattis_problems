


def getsum(descriptor,cans):
	s=0
	for i in xrange(len(cans)):
		if descriptor&1:
			s+=cans[i]
		descriptor>>=1
	return s


bits={}
b=1
for i in xrange(21):
	bits[b]=i
	b<<=1

lbits=sorted(bits)



def optimize(descriptor,index,cans,target,cache={}):
	if (descriptor,index) in cache:
		return cache[(descriptor,index)]
	if index==len(cans):
		cache[(descriptor,index)]=getsum(descriptor,cans)
		return cache[(descriptor,index)]
	m0=optimize(descriptor,index+1,cans,target,cache)
	m1=optimize(descriptor+(1<<index),index+1,cans,target,cache)
	m0,m1=sorted([m0,m1])
	cache[(descriptor,index)]= min([m0,m1],key=lambda x: abs(target-x))
	return cache[(descriptor,index)]





'''
cans=map(int,raw_input().split())

while cans.pop(0):
	s=sum(cans)
	cals=optimize(0,0,cans,s//2,{})
	x,y = sorted([s-cals,cals])
	print y,x
	cans=map(int,raw_input().split())
'''


cans=map(int,raw_input().split())

while cans.pop(0):
	s=sum(cans)
	combs=[0]*(1<<len(cans))
	for b in lbits:
		if b>=len(combs):
			break
		combs[b]=cans[bits[b]]
	for i in xrange(2,len(combs)):
		if combs[i]==0:
			rbit=i&-i
			combs[i]=combs[rbit]+combs[i-rbit]
	cals=min(combs,key=lambda v: abs(v-s//2))
	x,y = sorted([s-cals,cals])
	print y,x
	cans=map(int,raw_input().split())


