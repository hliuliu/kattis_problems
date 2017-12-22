


def mincars(cars):
	nemp=len(cars)
	count=0
	while cars:
		ps=cars.pop()
		nemp-=ps
		count+=1
		if nemp<=0:
			return count
	if nemp>0:
		return 'IMPOSSIBLE'
	return count


def calc_case(n,t,e,towns):
	nums=[0]*(n+1)
	for i in xrange(1,n+1):
		if i!=t:
			mc=mincars(towns[i])
			if mc=='IMPOSSIBLE':
				return mc
			nums[i]=mc
	nums.pop(0)
	return ' '.join(map(str,nums))


c=int(raw_input())

for i in xrange(1,c+1):
	n,t=map(int,raw_input().split())
	e=int(raw_input())
	towns = [[] for _ in xrange(n+1)]
	for _ in xrange(e):
		h,p=map(int,raw_input().split())
		towns[h].append(p)
	for cars in towns:
		cars.sort()
	print 'Case #%d:'%i, calc_case(n,t,e,towns)





