
from datetime import datetime


n= int(raw_input())

strtodate=lambda x: datetime.strptime(x,'%Y/%m/%d')

for i in xrange(n):
	name,beginps,born,courses= (f(x) for f,x in zip(
		[str,strtodate,strtodate,int],raw_input().split()
		))
	if beginps.year>=2010 or born.year>=1991:
		print name,'eligible'
	elif courses>=41:
		print name,'ineligible'
	else:
		print name,'coach petitions'




