


n=int(raw_input())

while n:
	p1,p2=0,0
	for _ in xrange(n):
		action,m=raw_input().split()
		m=int(m)
		if action=='DROP':
			p2+=m
			print 'DROP 2',m
		else:
			if p1>=m:
				print 'TAKE 1',m
				p1-=m
			else:
				if p1:
					print 'TAKE 1',p1
					m-=p1
				print 'MOVE 2->1',p2
				p1,p2=p2,0
				print 'TAKE 1',m
				p1-=m

	n=int(raw_input())
	if n:
		print



