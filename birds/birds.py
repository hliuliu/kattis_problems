

l,d,n=map(int,raw_input().split())

if l<12:
	print 0
else:
	pos=[]
	for _ in xrange(n):
		pos.append(int(raw_input()))
	pos.sort()
	count=0
	if n==0:
		count=(l-12)//d +1
	else:
		for i in xrange(n-1):
			count+=(pos[i+1]-pos[i])//d -1
		count+=(pos[0]-6)//d
		count+=(l-6-pos[-1])//d
	print count


