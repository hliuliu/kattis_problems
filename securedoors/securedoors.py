
n=int(raw_input())

inside=set()


for _ in xrange(n):
	action,emp=raw_input().split()
	if action=='entry':
		print emp,'entered',
		if emp in inside:
			print '(ANOMALY)'
		else:
			print
		inside.add(emp)
	else:
		print emp,'exited',
		if emp not in inside:
			print '(ANOMALY)'
		else:
			print
		inside.discard(emp)





