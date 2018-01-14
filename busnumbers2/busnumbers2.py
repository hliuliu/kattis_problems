m= int(raw_input())

n= int(m**(1./3))

cubes = [i**3 for i in xrange(1,n+1)]

cubesums = [[i+j for i in cubes] for j in cubes]

counts = {}

for i in xrange(n):
	for j in xrange(i+1):
		counts[cubesums[i][j]] = counts.get(cubesums[i][j],0) + 1

for num in counts.keys():
	if counts[num]==1:
		del counts[num]

for num in sorted(counts,reverse=True):
	if num<=m:
		print num
		break
else:
	print 'none'
