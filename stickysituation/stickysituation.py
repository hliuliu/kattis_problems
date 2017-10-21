

n= int(raw_input())

sticks = map(int,raw_input().split())

sticks.sort()


for i in xrange(n-2):
	for j in xrange(i+1,n-1):
		if sticks[j+1]<sticks[i]+sticks[j]:
			print 'possible'
			break
	else:
		continue
	break

else:
	print 'impossible'



