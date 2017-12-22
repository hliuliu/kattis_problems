

a,b,c,d=map(int,raw_input().split())


def determine(a,b,c,d):
	if (a,b)==(1,2):
		if (c,d)==(1,2):
			return 0
		return 1
	if (c,d)==(1,2):
		return 2
	if (a,b)==(c,d):
		return 0
	if a==b:
		if c==d:
			return 1 if a>c else 2
		return 1
	if c==d:
		return 2
	return 1 if 10*b+a>10*d+c else 2



while any((a,b,c,d)):
	a,b=sorted([a,b])
	c,d=sorted([c,d])
	res=determine(a,b,c,d)
	if not res:
		print 'Tie.'
	else:
		print 'Player %d wins.'%res
	a,b,c,d=map(int,raw_input().split())



