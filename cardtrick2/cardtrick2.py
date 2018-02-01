
def incr(curr,i,n,order):
	while i:
		curr= (curr+1)%n
		if order[curr]==0:
			i-=1
	return curr


t= int(raw_input())

for _ in xrange(t):
	n= int(raw_input())
	order= [0]*n
	curr =0
	for i in xrange(1,n+1):
		curr = incr(curr,i,n,order)
		order[curr]=i
		curr = (curr+1)%n
	print ' '.join(map(str,order))



