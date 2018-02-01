



x,y=map(int,raw_input().split())

n=int(raw_input())

if not n:
	print float(x)/y


else:

	bounds=[]
	freqs={}

	for _ in xrange(n):
		l,u,f= [tp(val) for tp,val in zip(
			[int,int,float],
			raw_input().split()
			)]
		bounds.append(l)
		bounds.append(u)
		freqs[l]=f

	bounds.sort()

	if bounds[0]!=0:
		bounds.insert(0,0)
	if bounds[-1]!=y:
		bounds.append(y)
	bp=list(zip(bounds[:-1],bounds[1:]))
	wt=0.0
	for l,u in bp:
		wt+=(u-l)*freqs.get(l,1)
	print x/wt











