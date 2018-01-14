



t=int(raw_input())

for _ in xrange(t):
	raw_input()
	ncs,ne=map(int,raw_input().split())
	iqs=[]
	while len(iqs)<ncs+ne:
		iqs.extend(map(int,raw_input().split()))
	ics,ie=iqs[:ncs],iqs[ncs:]
	avcs=sum(ics)/float(ncs)
	ave=sum(ie)/float(ne) if ne else 0
	count =0
	for s in ics:
		if ave<s<avcs:
			count+=1
	print count




