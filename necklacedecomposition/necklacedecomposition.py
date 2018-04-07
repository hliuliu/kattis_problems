


from __future__ import print_function



def decompose(bstr):
	zinds = [i for i in xrange(len(bstr)) if bstr[i]=='0']
	if not zinds:
		print ('({})'.format(bstr))
		return
	diff = [zinds[i]-zinds[i-1]-1 for i in xrange(1,len(zinds))]
	diff.insert(0,zinds[0])
	diff.append(len(bstr)-zinds[-1]-1)
	aggr = []
	if diff[0]:
		print('({})'.format('1'*diff.pop(0)), end='')
	else:
		diff.pop(0)
	for x in diff:
		if not aggr or aggr[-1][-1]>x:
			aggr.append([])
		aggr[-1].append(x)


	change = True
	while change:
		change = False
		aggr2=[]
		for group in aggr:
			if aggr2 and aggr2[-1]<=group:
				aggr2[-1].extend(group)
				change = True
			else:
				aggr2.append(group)
		aggr = aggr2


	for group in aggr:
		print ('(',end='')
		for x in group:
			print ('0'+'1'*x,end='')
		print (')',end='')
	print ()





n = int(raw_input())

for _ in xrange(n):
	decompose(raw_input())




