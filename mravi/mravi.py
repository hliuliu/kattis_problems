


from math import sqrt


n= int(raw_input())

parent = [0]*(n+1)

perc = [0]*(n+1)

issuper = [0]*(n+1)


for _ in xrange(n-1):
	a,b,x,t = map(int, raw_input().split())
	parent[b]=a
	perc[b] = x
	issuper[b] = t


needs = [0]+map(int, raw_input().split())


best = 0

for i in xrange(1,n+1):
	if needs[i]>=0:
		ans = needs[i]
		while i>1:
			if issuper[i]:
				ans = sqrt(ans)
			ans *= 100.0
			ans /= perc[i]
			i = parent[i]
		best = max(best,ans)


print best


