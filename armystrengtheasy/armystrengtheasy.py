


def kill(g,mg):
	while 1:
		if not g:
			yield -1
		elif not mg:
			yield 1
		else:
			if g[0]>=mg[0]:
				mg.pop(0)
			else:
				g.pop(0)
			yield 0





t=int(raw_input())

for _ in xrange(t):
	raw_input()
	raw_input()
	g=map(int,raw_input().split())
	mg=map(int,raw_input().split())
	g.sort()
	mg.sort()
	for res in kill(g,mg):
		if res:
			print ('Mecha' if res<0 else '')+'Godzilla'
			break




