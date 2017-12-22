

def cnt1(s):
	n=0
	for c in s:
		if c=='1':
			n+=1
	return n 


cache={0:0}

def maxbits(x):
	if x in cache:
		return cache[x]
	ans=max(maxbits(x//10),cnt1(bin(x)))
	cache[x]=ans
	return ans






t=int(raw_input())

for _ in xrange(t):
	x=int(raw_input())
	print maxbits(x)


