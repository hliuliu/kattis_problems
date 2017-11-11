

n = int(raw_input())
k = int(raw_input())

items = {}

for _ in xrange(k):
	num, obj = raw_input().split()
	num= int(num)
	if obj not in items:
		items[obj] = []
	items[obj].append(num)

for _, ls in items.iteritems():
	ls.sort()

m= int(raw_input())
bought = [raw_input() for _ in xrange(m)]

try:
	seq = []
	curr =0
	for obj in bought:
		while items[obj][0]<curr:
			items[obj].pop(0)
		curr = items[obj].pop(0)
		seq.append(curr)
except:
	print 'impossible'
else:
	maxindex = float('inf')
	while seq:
		item = bought.pop()
		if items[item] and items[item][0]<=maxindex:
			print 'ambiguous'
			break
		maxindex = seq.pop()
	else:
		print 'unique'

