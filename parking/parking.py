

prices=map(int,raw_input().split())

hours=[0]*101

for _ in xrange(3):
	s,e=map(int,raw_input().split())
	for i in xrange(s,e):
		hours[i]+=1


cost=0

for h in hours:
	if h:
		cost+=h*prices[h-1]

print cost


