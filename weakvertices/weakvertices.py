


n=int(raw_input())



def isweak(v,adjlist):
	start=0
	value=adjlist[v]
	while value:
		if value&1:
			end=start+1
			temp=value>>1
			while temp:
				if temp&1:
					if adjlist[start]&(1<<end):
						return start,end
				temp>>=1
				end+=1
		value>>=1
		start+=1
	return True





while n>=0:
	adjlist=[0]*n
	for i in xrange(n):
		l= map(int,raw_input().split())
		for r,j in enumerate(l):
			adjlist[i]^=(j<<r)
	weak=[]
	notweak=set()
	for i in xrange(n):
		if i in notweak:
			continue
		res=isweak(i,adjlist)
		if res==True:
			weak.append(i)
		else:
			j,k=res
			notweak.add(j)
			notweak.add(k)
	print ' '.join(map(str,weak))
	n=int(raw_input())





