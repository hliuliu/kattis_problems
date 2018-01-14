
from datetime import datetime as dt

# line=raw_input()

def totime(st):
	h,m,s=map(int,st.split(':'))
	d,h=divmod(h,24)

	return dt(1990,1,d+1,h,m,s)

ct=totime('00:00:00')
cs=0
cd=0

def gethours(tdel):
	sec=tdel.seconds
	d=tdel.days
	return 24*d+sec/3600.0

while 1:
	try:
		line=raw_input().strip()
		if not line:
			break
	except EOFError:
		break
	if ' ' in line:
		assert line!=' '
		t,sp=line.split()
		t=totime(t)
		sp=int(sp)
		cd+=cs*gethours(t-ct)
		cs=sp
		ct=t
	else:
		assert line!=''
		print line,
		t=totime(line)
		print '%.2f'%(cd+cs*gethours(t-ct)),'km'



