

t=int(raw_input())

for _ in xrange(t):
	n,m=map(int,raw_input().split())
	val=0
	prizes=[]
	for i in xrange(n):
		line=map(int,raw_input().split())
		line.pop(0)
		cash=line.pop()
		prizes.append((line,cash))
	earnings=[0]+map(int,raw_input().split())
	for line,cash in prizes:
		val+=cash*(min((earnings[i] for i in line)))
	print val







