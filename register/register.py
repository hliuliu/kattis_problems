



ps=[2,3,5,7,11,13,17,19]
prod=[1]
for p in ps:
	prod.append(prod[-1]*p)

state=map(int,raw_input().split())

count=0
for i in xrange(8):
	count+=prod[i]*(ps[i]-state[i]-1)

print count



