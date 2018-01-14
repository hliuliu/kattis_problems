

fibs=[0,1]

threshold = 10**18

while fibs[-1]<threshold:
	fibs.append(fibs[-2]+fibs[-1])

# print fibs[-1],len(fibs)

n,k=map(int,raw_input().split())

if n>len(fibs):
	if (n-len(fibs)+1) &1:
		n=len(fibs)
	else:
		n=len(fibs)-1





while n>=3:
	if k<=fibs[n-2]:
		n-=2
	else:
		k-=fibs[n-2]
		n-=1

print 'N' if n==1 else 'A'
		








