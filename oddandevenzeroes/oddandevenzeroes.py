

# pof5=[1]
# pof5not=[]

# p=1
# v=5
# while v<=10**18:
# 	pof5not.append(v//5-pof5[-1])
# 	if p&1:
# 		pof5.append(5*pof5[-1])
# 	else:
# 		pof5.append(3*pof5[-1]+2*(pof5not[-1]))
# 	p+=1
# 	v*=5

# print pof5

def ntz_parity(n):
	p=0
	h=5
	logh=1
	while h<=n:
		p+=n//h
		p&=1
		h*=5
		logh+=1
	return p

def get_index(n):
	return ((n&1)<<1)+ntz_parity(n)

def calc(n):
	L=[0]*4
	if n<=4:
		for k in xrange(n+1):
			L[get_index(k)]+=1
		return L
	q,r=divmod(n,5)
	M=calc(q-1)
	L[3]=3*M[2]+2*M[1]
	L[2]=3*M[3]+2*M[0]
	L[1]=3*M[1]+2*M[2]
	L[0]=3*M[0]+2*M[3]
	for k in xrange(5*q,n+1):
		L[get_index(k)]+=1
	return L




n=int(raw_input())
while n>=0:
	L=calc(n)
	print L[0]+L[2]
	n=int(raw_input())


