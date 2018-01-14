

def binomial(n,r):
	if r>n-r:
		r=n-r
	ans=1
	for i in xrange(r):
		ans*=n-i
		ans/=i+1
	return ans



catalan=[1]
n=0
while n<=5000:
	catalan.append(2*(2*n+1)*catalan[-1]//(n+2))
	n+=1




q=int(raw_input())


for _ in xrange(q):
	x=int(raw_input())
	print catalan[x]

