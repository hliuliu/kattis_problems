


n= int(raw_input())

prices=[int(raw_input()) for _ in xrange(n)]

prices.sort(reverse=True)
for i in xrange(2,n,3):
	prices[i]=0

print sum(prices)



