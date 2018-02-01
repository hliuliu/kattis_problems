

# Accepted :)

n = int(raw_input())
first = True

while n:
	if not first:
		print 
	records = [raw_input() for _ in xrange(n)]
	records.sort(key = lambda x: x[:2])
	print '\n'.join(records)
	n = int(raw_input())
	first = False


