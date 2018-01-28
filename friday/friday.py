

t=int(raw_input())

for _ in xrange(t):
	#m,d=map(int,raw_input().split())
	raw_input()
	days=map(int,raw_input().split())
	start=0
	count=0
	for d in days:
		if d>=13 and (start+5)%7==5:
			count+=1
		start=(start+d)%7
	print count





