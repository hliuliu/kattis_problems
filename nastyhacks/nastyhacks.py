
n = int(raw_input())

for _ in xrange(n):
	r,e,c = map(int, raw_input().split())
	if e>r+c:
		print 'advertise'
	elif e==r+c:
		print 'does not matter'
	else:
		print 'do not advertise'

