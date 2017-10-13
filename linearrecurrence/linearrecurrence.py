


n = int(raw_input())

coefs = map(int, raw_input().split())

xs = map(int, raw_input().split())




A = [[0]*(n+1) for _ in xrange(n+1)]

A[0][0] = 1
A[1][:] = coefs

for i in xrange(2,n+1):
	A[i][i-1] = 1

# print A
xs.append(1)
xs.reverse()

# print xs


def vecmult(A,v,m):
	u =[]
	for row in A:
		u.append(sum([(i*j)%m for i,j in zip(row,v)])%m)
	return u

def matmult(A,B,m):
	B= list(zip(*B))
	C= [vecmult(A,v,m) for v in B]
	for i in xrange(len(C)):
		for j in xrange(i):
			C[i][j], C[j][i] = C[j][i],C[i][j]
	return C


def matexp(A, e, m):
	if e==0:
		return [[int(i==j)%m for j in xrange(len(A))] for i in xrange(len(A))]
	if e==1:
		return [[entry%m for entry in row] for row in A]
	B = matexp(A,e>>1,m)
	B = matmult(B,B,m)
	if e&1:
		B= matmult(B,A,m)
	return B




def query(t,m):
	if t<n:
		return xs[-(t+1)]%m
	M = matexp(A,t-n+1, m)
	v= vecmult(M, xs, m)

	# print M
	# print v

	return v[1]


# print matmult(A,A,23)

q = int(raw_input())

for _ in xrange(q):
	print query(*(map(int, raw_input().split())))



