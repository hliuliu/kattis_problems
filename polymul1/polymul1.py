
t = int(raw_input())

for _ in xrange(t):
	raw_input()
	p1 = map(int, raw_input().split())
	raw_input()
	p2 = map(int,raw_input().split())

	p = [0]*(len(p1+p2)-1)

	for i in xrange(len(p1)):
		for j in xrange(len(p2)):
			p[i+j]+= p1[i]*p2[j]

	print len(p)-1
	print ' '.join(map(str,p))


