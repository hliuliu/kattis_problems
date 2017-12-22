

n=int(raw_input())

before=raw_input()
after=raw_input()

if n&1:
	if all((i!=j for i,j in zip(before,after))):
		print 'Deletion succeeded'
	else:
		print 'Deletion failed'

else:
	if before==after:
		print 'Deletion succeeded'
	else:
		print 'Deletion failed'


