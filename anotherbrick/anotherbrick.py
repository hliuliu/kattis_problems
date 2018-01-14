

h,w,n=map(int,raw_input().split())

bs=map(int,raw_input().split())


for i in xrange(h):
	s=0
	while s<w:
		if not bs:
			print 'NO'
			break
		s+=bs.pop(0)
	else:
		if s>w:
			print 'NO'
			break
		continue
	break
else:
	print 'YES'

