

def horner(poly,val):
	if not poly:
		return 0
	constant=poly.pop()
	ans=constant+val*horner(poly,val)
	poly.append(constant)
	return ans

Cs=[]
coefs=[]

poly=map(int,raw_input().split())
n=poly.pop(0)

Cs.append(poly[-1])
coefs.append(1)


for i in xrange(1,n+1):
	Cs.append(horner(poly,i)-sum((a*b for a,b in zip(coefs,Cs))))
	coefs.append(coefs[-1]+1)
	for j in xrange(i-1,0,-1):
		coefs[j]+=coefs[j-1]


print ' '.join(map(str,Cs))




