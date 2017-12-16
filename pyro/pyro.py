


L = []
S= set()

n = int(raw_input())

while n>=0:
	L.append(n)
	S.add(n)
	n= int(raw_input())

def nb(x):
	ans =0
	while x:
		x = x ^ (x&(-x))
		ans +=1
	return ans

for v in L:
	count = 0
	for i in xrange(20):
		tmp = v^(1<<i)
		if tmp>v and tmp in S:
			count +=1
		for j in xrange(i):
			tmp2 = tmp^(1<<j)
			if tmp2>v and tmp2 in S:
				count+=1
	print '{}:{}'.format(v,count)






