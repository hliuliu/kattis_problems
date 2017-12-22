

p = int(raw_input())

for _ in xrange(p):
	data=map(int,raw_input().split())
	k=data.pop(0)
	count=0
	while data:
		i=data.index(min(data))
		count+=i
		del data[i]
	print k,count







