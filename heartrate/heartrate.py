

n = int(raw_input())

for _ in xrange(n):
	b,p = map(float, raw_input().split())
	tmax = p/(b-1)
	bmin = 60/tmax
	bpm = 60*b/p
	tmin = p/(b+1)
	bmax = 60/tmin
	print bmin,bpm,bmax




