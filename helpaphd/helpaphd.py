
n = int (raw_input())

for _ in xrange(n):
	line = raw_input()
	print 'skipped' if line == 'P=NP' else sum(map(int, line.split('+')))
