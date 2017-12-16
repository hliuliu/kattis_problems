

winner=0
pts=0

for i in xrange(1,6):
	score=sum(map(int,raw_input().strip().split()))
	if score>pts:
		pts=score
		winner=i

print winner,pts




