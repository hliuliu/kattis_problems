


n,t=map(float,raw_input().split())
n=int(n)

while n or t:
	wins=[0]*(n+1)
	wins[n]=1<<n
	for i in xrange(n-1,-1,-1):
		cut = (1<<i)/float(wins[i+1])
		if t<cut:
			wins[i]=(cut-t)/(1-t)*(1<<i)+wins[i+1]*(1-cut)/(1-t)*(cut+1)/2.0
		else:
			wins[i]=wins[i+1]*(t+1)/2.0
	print '%.3f'%wins[0]
	n,t=map(float,raw_input().split())
	n=int(n)



