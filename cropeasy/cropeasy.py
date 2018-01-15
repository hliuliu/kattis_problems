

t = int(raw_input())



def valid(i,j,k):
	pts = [trees[t] for t in [i,j,k]]
	return all([sum([l[index] for l in pts])%3==0 for index in [0,1]])


for casenum in xrange(1,t+1):
	n,a,b,c,d,x,y,m = map(int, raw_input().split())
	trees = [(x,y)]
	for _ in xrange(n-1):
		x = (a*x+b)%m
		y = (c*y+d)%m
		trees.append((x,y))

	ct =0
	for i in xrange(n-2):
		for j in xrange(i+1, n-1):
			for k in xrange(j+1, n):
				if valid(i,j,k):
					ct +=1
	print 'Case #{}: {}'.format(casenum,ct)



