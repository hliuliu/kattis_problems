
n=int(raw_input())

for _ in xrange(n):
	words=raw_input().split()
	used=set()
	line=raw_input().split()[-1]
	while line[-1]!='?':
		used.add(line)
		line=raw_input().split()[-1]
	print ' '.join((w for w in words if w not in used))


