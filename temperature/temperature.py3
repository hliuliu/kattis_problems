

x,y=map(int,input().split())

if y==1:
	if x==0:
		print ('all good'.upper())
	else:
		print ('impossible'.upper())
else:
	print (x/(1-y))


