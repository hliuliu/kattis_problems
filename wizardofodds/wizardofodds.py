

n, k = map(int, raw_input().split())

ct =0
while n>1:
	ct += 1
	n = n-(n>>1)

if ct<=k:
	print 'Your wish is granted!'
else:
	print 'You will become a flying monkey!'

