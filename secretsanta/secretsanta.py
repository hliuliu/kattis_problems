import math
eps=1E-11

def der_prob(n):
	limit=1/math.e
	ans=0.0
	curr=2
	term=-1.0
	err=limit
	while curr<=n and abs(err)>=eps:
		term*=(-1.0)/curr
		ans+=term
		err-=term
		curr+=1
	return ans

n=int(raw_input())
print 1-der_prob(n)




