

c,n = map(int,raw_input().split())

np =0

for leave,enter,stay in [map(int, raw_input().split()) for 
_ in xrange(n)]:
	if leave>np:
		print 'impossible'
		break
	np -= leave
	if enter>c-np or (stay>0 and enter+np<c):
		print 'impossible'
		break
	np += enter
else:
	if np>0 or stay>0:
		print 'impossible'
	else:
		print 'possible'





