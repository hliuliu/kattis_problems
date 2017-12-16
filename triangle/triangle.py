
import math

log3_10=math.log(10,3)
log2_10=math.log(10,2)

casenum=1
while 1:
	try:
		i=int(raw_input())
		nd=(i+1)/log3_10-i/log2_10
		nd=math.ceil(nd)
		print 'Case %d:'%casenum, int(nd)
		casenum+=1

	except EOFError:
		break


