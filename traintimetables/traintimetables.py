
SIM_TIME = 24*60

def to_minute(tm):
	h,m = map(int,tm.split(':'))
	return h*60+m


def add_to_dict(d,v):
	d[v] = d.get(v,0)+ 1

def simulate(i):
	t = int(raw_input())
	na,nb= map(int,raw_input().split())
	depA,depB = {},{}
	arrA,arrB = {},{}
	for _ in xrange(na):
		start,end = raw_input().split()
		add_to_dict(depA, to_minute(start))
		add_to_dict(arrB,(to_minute(end)+t))
	for _ in xrange(nb):
		start,end = raw_input().split()
		add_to_dict(depB,to_minute(start))
		add_to_dict(arrA,to_minute(end)+t)
	readyA,readyB = 0,0
	needA,needB = 0,0

	for moment in xrange(SIM_TIME):
		if moment in arrA:
			readyA += arrA[moment]
		if moment in arrB:
			readyB += arrB[moment]
		if moment in depA:
			readyA -= depA[moment]
			needA -= min(readyA,0)
			readyA = max(readyA,0)
		if moment in depB:
			readyB -= depB[moment]
			needB -= min(readyB,0)
			readyB = max(readyB,0)
	print 'Case #%d:'%i , needA, needB



s= int(raw_input())

for i in xrange(s):
	simulate(i+1)





