
n=int(raw_input())


for j in xrange(n):
	raw_input()
	ropes=raw_input().split()
	b,r=[],[]
	for i in ropes:
		if i[-1]=='B':
			b.append(int(i[:-1]))
		else:
			r.append(int(i[:-1]))
	b.sort()
	r.sort()
	ans=0
	count=0
	while b and r:
		ans+=b.pop()
		ans+=r.pop()
		count+=2
	ans-=count
	print 'Case #%d:'%(j+1),ans



