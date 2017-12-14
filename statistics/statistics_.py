num=1
import sys
for line in sys.stdin:
	data=map(int,line.split())
	data.pop(0)
	a,b=min(data),max(data)
	print 'Case %d:'%num, a, b, b-a
	num+=1
