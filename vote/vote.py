

def tally(votes):
	m=0
	mc=0
	mi=-1
	for i,v in enumerate(votes):
		if v>m:
			m=v
			mc=1
			mi=i
		elif m==v:
			mc+=1
	if mc==1:
		return mi
	return 0




t=int(raw_input())

for _ in xrange(t):
	n=int(raw_input())
	votes=[0]+[int(raw_input()) for i in xrange(n)]
	winner=tally(votes)
	if not winner:
		print 'no winner'
	elif votes[winner]*2>sum(votes):
		print 'majority winner',winner
	else:
		print 'minority winner', winner



