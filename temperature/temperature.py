

x,y=map(int,raw_input().split())

if y==1:
	if x==0:
		print 'all good'.upper()
	else:
		print 'impossible'.upper()
else:
	print float(x)/(1-y)


